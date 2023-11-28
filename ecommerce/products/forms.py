from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

        # specify Widgets or labels if needed
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter product name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter product price', 'step': '1'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter product Description'}),
        }
        labels = {
            'name': 'Product Name',
            'price': 'Product Price',
        }