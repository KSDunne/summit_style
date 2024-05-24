from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Models for products app


class Category(models.Model):
    """
    This is a model representing a product category.

    Fields:
        - `name` (CharField): Name of the category.
        - `friendly_name` (CharField): A user-friendly
        name for the category (optional).

    Methods:
        - `get_friendly_name()`: Method to retrieve the
        friendly name of the category.

    Credit: https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob
    /5e595d250f0d7a408a7ccd40bfa25d24c000034d/products/models.py#L3
    """

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model for a product.

    Fields:
        - `category` (ForeignKey): Reference to the category this product belongs to (optional).
        - `sku` (CharField): Stock Keeping Unit for the product (optional).
        - `name` (CharField): Name of the product.
        - `description` (TextField): Description of the product.
        - `has_sizes` (BooleanField): Indicates whether the product comes in different sizes (optional).
        - `is_course` (BooleanField): Indicates whether the product is a course (optional).
        - `price` (DecimalField): Price of the product.
        - `image_url` (URLField): URL link to the product image (optional).
        - `image` (ImageField): Image of the product (optional).
        - `wishlist` (ManyToManyField): Reference to users who have added this product to their wishlist.

    Methods:
        - `__str__`: String representation of the product.
        - `average_rating()`: Calculates the average rating for the product.
        - `number_of_wishes()`: Counts the number of users who have added this product to their wishlist.

    Credit: https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob
    /5e595d250f0d7a408a7ccd40bfa25d24c000034d/products/models.py#L18
    I customised this model by adding a 'wishlist' field, a 'is_course' field
    and I set 'has_sizes' to a default of True.
    """

    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=True, null=True, blank=True)
    is_course = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    wishlist = models.ManyToManyField(User, related_name="product_wishlist", blank=True)

    def __str__(self):
        return self.name

    def average_rating(self) -> int:
        avg_rating = (
            Star.objects.filter(product=self).aggregate(Avg("rating"))["rating__avg"]
            or 0
        )
        return round(avg_rating)

    def number_of_wishes(self):
        return self.wishlist.count()


class Star(models.Model):
    """
    Model representing a star rating and review for a product.

    Fields:
        - `user` (ForeignKey): Reference to the user who submitted the rating and review.
        - `product` (ForeignKey): Reference to the product being rated and reviewed.
        - `rating` (IntegerField): Numeric rating given by the user, ranging from 1 to 5.
        - `title` (CharField): Title of the review.
        - `body` (TextField): Content of the review.
        - `created_on` (DateTimeField): Date and time when the review was created.
        - `updated_on` (DateTimeField): Date and time when the review was last updated.

    Meta:
        - `ordering`: Ordering for queries based on creation date.

    Methods:
        - `__str__`: String representation of the rating and review.

    Credit: https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(1, "Rating must be at least 1"),
            MaxValueValidator(5, "Rating must be a max of 5"),
        ],
    )
    title = models.CharField(max_length=180)
    body = models.TextField(
        validators=[
            MinLengthValidator(30, "Review must be greater than 30 characters")
        ],
        max_length=400,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.product.name} rated {self.rating} by {self.user}"
