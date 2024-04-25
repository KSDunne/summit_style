from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Models for products app

'''
Credit: https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob
/5e595d250f0d7a408a7ccd40bfa25d24c000034d/products/models.py#L3
'''
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

'''
Credit: https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob
/5e595d250f0d7a408a7ccd40bfa25d24c000034d/products/models.py#L18
I changed this model by adding a field 'is_course' and I set
'has_sizes' to a default of True
'''
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=True, null=True, blank=True)
    is_course = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def average_rating(self) -> float:
        return Star.objects.filter(product=self).aggregate(Avg("rating"))["rating__avg"] or 0
    
    
class Star(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name}: {self.rating}"