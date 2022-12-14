from django import forms
from .models import Product

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['prod_name', 'prod_description', 'prod_price', 'category', 'image']
