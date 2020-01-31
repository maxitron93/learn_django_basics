from django.contrib import admin
from .models import Blog

# Register your models here.
# Add models into here if you want to allow the superuser to manage it via the GUI site
admin.site.register(Blog)
