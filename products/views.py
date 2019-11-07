from django.shortcuts import render

from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
      #'title': obj.title,
      #'description': obj.description,
      #'price':obj.price,
      #'summary':obj.summary,
      #'featured':obj.featured,
      'object':obj
    }
    return render(request,"product_detail.html",context)


#def product_create_view(request):
#    form = ProductForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = ProductForm()
#    context = {
#        'form':form
#    }
#    return render(request,"product_create.html",context)


def product_create_view(request):
    my_form = RawProductForm() # to get rid of the validation error.
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
             print(my_form.cleaned_data)
             Product.objects.create(**my_form.cleaned_data)  # save the data in the database
             my_form = RawProductForm()
#        else: 
#             print(my_form.errors)
    context = {
        "form":my_form
    }
    return render(request,"product_create.html",context)

