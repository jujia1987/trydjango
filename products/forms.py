from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
     class Meta:
        model = Product
        fields = [
             'title',
             'description',
             'price',
             'summary',
             'featured'
        ]
#Compared with the class above, the ways is raw.
#The above way is better as it can make sure the value types for the form are same as the model defined.

class RawProductForm(forms.Form):       
     title         = forms.CharField()
     description   = forms.CharField()
     price         = forms.DecimalField()

