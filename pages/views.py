from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#def home_view(*args,**kwargs):
#    return HttpResponse("<h1>Hello World</h1>")   #String of html code


#return django HTML template
def home_view(request,*args,**kwargs):
    #print(args,kwargs)
    #print(request.user)
    return render(request, "home.html", {})



def contact_view(request,*args,**kwargs):
#    return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})


def about_view(request,*args,**kwargs):
    my_context = {
          "my_name":"Harry Zhou",
          "my_answer": False,
          "my_number":"02102236189",
          "my_list":[123,234,345,"abc"]
    }
    return render(request,"about.html", my_context)
