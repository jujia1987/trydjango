from django.shortcuts import render


from .models import Customer
from .forms import CustomerForm,CustomerSearchForm
# Create your views here.
def customer_detail_view(request):
    #name = "Harry"
    obj = Customer.objects.get(first_name = "Harry")
    context = {
        'object':obj
    }
    return render(request,"customer_detail.html",context)



def customer_create_view(request):
    form = CustomerForm()
    if request.method == "POST":
       form = CustomerForm(request.POST or None)
       if form.is_valid():
          form.save()   #can be replaced with Customer.objects.create(**form.cleaned_data)
          print(form.cleaned_data)
          form = CustomerForm()   #request.GET doesn't have to be here
    else:
       print(form.errors)
    context = {
       "form":form
    } 
    return render(request,"customer_create.html",context)



def customer_search_view(request):
    search_form = CustomerSearchForm()
    if request.method == "GET":
       #search_form = CustomerSearchForm(request.GET)
       #name = search_form.data
       name = str(request.GET.get('first_name')).title()
       print(name)
       try: 
           obj = Customer.objects.get(first_name = name)
       except Customer.DoesNotExist:
           obj = None
    context = {
       "object":obj   #object is used in the HTML template
    }
    return render(request,"customer_detail.html",context)
