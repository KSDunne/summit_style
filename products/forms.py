from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Star


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating product instances.

    **Fields**

    All fields from the Product model are included.
    """

    class Meta:
        model = Product
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"


class StarForm(forms.ModelForm):
    """
    Form for users to review a product.

    Uses :model:`products.Star`.

    **Fields**

        title: The title of the review.
        rating: The rating given by the user, ranging from 1 to 5.
        body: The main text of the review provided by the user.

    **Labels**

        title: "Review Title"
        rating: "Rating (1-5)"
        body: "Review Text"
    """

    class Meta:
        model = Star
        fields = (
            "title",
            "rating",
            "body",
        )

        labels = {
            "title": "Review Title",
            "rating": "Rating (1-5)",
            "body": "Review Text",
        }
