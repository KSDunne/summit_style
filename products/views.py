from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Star
from .forms import ProductForm, StarForm

# Create your views here.


def all_products(request):
    """
    A view to show all products, including sorting and search queries.

    Uses :model: `products.Product` and :model: `products.Category`

    **Context**

    ``products``
        A list of instances of :model:`products.Product`.
    ``search_term``
        The search query string entered by the user, if any.
    ``current_categories``
        A list of instances of :model:`products.Category` filtered
        by the user's selection.
    ``current_sorting``
        The current sorting method applied to the products list.

    **Template:**

    :template:`products/products.html`
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query))
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


@login_required
def product_detail(request, product_id):
    """
    A view to show individual product details.

    Uses :model: `products.Product` and :model: `reviews.Star`

    **Context**

    ``product``
        An instance of :model:`products.Product`.
    ``stars``
        A queryset of :model:`reviews.Star` instances related to the product.
    ``review_count``
        The count of reviews (instances of :model:`reviews.Star`) for
        the product.
    ``star_form``
        An instance of :form:`reviews.StarForm` for submitting a new review.
    ``liked``
        Indicates if the product is in the user's wishlist.

    **Template:**

    :template:`products/product_detail.html`
    """

    product = get_object_or_404(Product, pk=product_id)
    stars = Star.objects.filter(product=product)
    review_count = Star.objects.filter(product=product).count()
    liked = False

    if product.wishlist.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        star_form = StarForm(data=request.POST)
        if star_form.is_valid():
            star = star_form.save(commit=False)
            star.user = request.user
            star.product = product
            star.save()
            messages.success(request, "Review submitted successfully")
            return HttpResponseRedirect(
                reverse("product_detail",
                        kwargs={"product_id": star.product.pk}))

    else:
        star_form = StarForm()

    context = {
        "product": product,
        "stars": stars,
        "review_count": review_count,
        "star_form": star_form,
        "liked": liked,
    }

    return render(request, "products/product_detail.html", context)


class Wishlist(LoginRequiredMixin, View):
    """
    Add or remove a product from the wishlist.

    Uses :model: `products.Product`

    Redirects the user back to the product detail page with the liked status

    """

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.wishlist.filter(id=request.user.id).exists():
            product.wishlist.remove(request.user)
        else:
            product.wishlist.add(request.user)

        return HttpResponseRedirect(reverse("product_detail", args=[pk]))


class MyWishlist(LoginRequiredMixin, View):
    """
    Display wishlist for the logged-in user on the my_wishlist template.

    Uses :model: `products.Product`

    **Context**

    ``wishlist_products``
        Represents the products in the user's wishlist.

    **Template**

    :template:`products/my_wishlist.html`

    """

    def get(self, request):
        """
        Retrieves the wishlist products for the current user and
        renders the my_wishlist template.
        """
        wishlist_products = Product.objects.filter(wishlist=request.user)
        context = {
            "wishlist_products": wishlist_products,
        }
        return render(request, "products/my_wishlist.html", context)


"""
Credit: https://www.youtube.com/watch?v=JzDBCZTgVyw&list=PLXuTq6OsqZjbCSfi
LNb2f1FOs8viArjWy&index=14
Credit: https://github.com/Dee-McG/Recipe-Tutorial/blob/main/recipes
/views.py#L61
"""


class EditReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a review

    Uses :model: `product.Star`

    **Context**

    ``star``
        represents the review instance to be edited

     **Template**

    :template:`products/edit_review.html`

    """

    model = Star
    template_name = "products/edit_review.html"
    form_class = StarForm

    def get_success_url(self):
        """
        Returns the success URL after editing the review.
        Redirects the user back to the product detail page
        that they were already on.
        """
        star = self.get_object()
        return reverse_lazy("product_detail",
                            kwargs={"product_id": star.product.pk})

    def form_valid(self, form):
        form.instance.confirmed = False
        messages.success(
            self.request,
            "Your review has been updated!",
            extra_tags="alert alert-success alert-dismissible",
        )

        return super().form_valid(form)

    def test_func(self):
        """
        Checks if the logged-in user is the owner of the review.

        Returns:
            bool: True if the logged in user is the owner of the review
            False otherwise.
        """
        star = self.get_object()
        return self.request.user == star.user or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        """
        Add product detail URL to the context data.
        """
        context = super().get_context_data(**kwargs)
        star = self.get_object()
        product_detail_url = reverse('product_detail', args=[star.product.pk])
        context['product_detail_url'] = product_detail_url
        return context


"""
Credit: https://www.youtube.com/watch?v=nFa3lC105dM&list=
PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=13
Credit: https://github.com/Dee-McG/Recipe-Tutorial/blob/main/recipes
/views.py#L72
"""


class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Displays a new page to confirm deletion of a review

    Uses :model: `products.Star`

    **Context**

    ``star``
        Represents the review instance to be deleted.
        Comes from :model:`products.Star`

    **Template**

    :template:`products/review_confirm_delete.html`

    Redirects to success url which is "/products/"
    """

    model = Star

    def get_success_url(self):
        """
        Returns the success URL after deleting the review.
        Redirects the user back to the product detail page
        that they were already on.
        """
        star = self.get_object()
        return reverse_lazy("product_detail",
                            kwargs={"product_id": star.product.pk})

    def form_valid(self, form):
        """
        Called when the form is valid. Displays a success message.
        """
        messages.success(
            self.request,
            "Your review has been deleted successfully!",
            extra_tags="alert alert-success alert-dismissible",
        )

        return super().form_valid(form)

    def test_func(self):
        """
        Checks if the logged-in user is the owner of the review.

        Returns:
            bool: True if the logged in user is the owner of the review
            False otherwise.
        """
        star = self.get_object()
        return self.request.user == star.user or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        """
        Add product detail URL to the context data.
        """
        context = super().get_context_data(**kwargs)
        star = self.get_object()
        product_detail_url = reverse('product_detail', args=[star.product.pk])
        context['product_detail_url'] = product_detail_url
        return context


@login_required
def add_product(request):
    """
    Add a product to the store. This view allows
    superusers to add a new product to the store's
    inventory.

    Uses :form: `products.ProductForm`

    **Context**

    ``form``
        An instance of :form:`products.ProductForm` for adding a new product.

    **Template**

    :template:`products/add_product.html`

    **Redirects**

    Redirects to the home page if the user is not a superuser.
    Redirects to the product detail page after successful addition
    of the product.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product."
                + " Please ensure the form is valid."
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store. This view allows
    superusers to edit an existing product in the
    store's inventory.

    Uses :form: `products.ProductForm`

    **Context**

    ``form``
        An instance of :form:`products.ProductForm` for editing the product.
    ``product``
        An instance of :model:`products.Product` representing
        the product to be edited.

    **Template**

    :template:`products/edit_product.html`

    **Redirects**

    Redirects to the home page if the user is not a superuser.
    Redirects to the product detail page after successful
    editing of the product.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product."
                + "Please ensure the form is valid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store with confirmation. This
    view allows superusers to delete an existing product
    from the store's inventory. It displays a confirmation
    page before deletion.

    Uses :model: `products.Product`

    **Context**

    ``product``
        An instance of :model:`products.Product` representing the product
        to be deleted.

    **Template**

    :template:`products/product_confirm_delete.html`

    **Redirects**

    Redirects to the home page if the user is not a superuser.
    Redirects to the products page after successful deletion of the product.
    """

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        # If it is a POST request, it means the user has confirmed deletion.
        product.delete()
        messages.success(request, "Product deleted!")
        return redirect(reverse("products"))

    # If it's a GET request, render the confirmation page.
    return render(
        request, "products/product_confirm_delete.html", {"product": product})
