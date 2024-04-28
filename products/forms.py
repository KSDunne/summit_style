from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Star


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
            
class StarForm(forms.ModelForm):
    """
    Form class for users to review a product

    **Fields:**

    `body`: Text area where logged in users can write their reviews
    """

    class Meta:
        """
        Uses :model: `products.Star`
        """

        model = Star
        fields = ("title","rating","body",)
        
        labels = {
            "title": "Review Title",
            "rating": "Rating (1-5)",
            "body": "Review Text",
        }