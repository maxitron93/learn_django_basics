from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product) # Need to do this to see it in the admin site
