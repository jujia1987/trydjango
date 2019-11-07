from django.contrib import admin

# Register your models here.

from .models import Customer
#admin.site.register(Customer)
#admin.site.unregister(Customer)
#@admin.register(Customer)

#Define the admin class
class CustomerAdmin(admin.ModelAdmin):
     list_display = ('first_name','last_name','age')
     list_filter = ('first_name','age')

#     pass
#Register the admin class with the associated model
admin.site.register(Customer, CustomerAdmin)
