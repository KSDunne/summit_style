from django.contrib import admin
from .models import Product, Category, Star

# Register models


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'average_rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    
class StarAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'rating',
    )

    def product_name(self, obj):
        return obj.product.name
    product_name.short_description = 'Product'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Star, StarAdmin)
