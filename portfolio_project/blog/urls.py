from django.urls import path
from django.conf import settings # Import settings.py
from django.conf.urls.static import static # Static is an app in itself
from . import views

urlpatterns = [
    path('', views.allBlogs, name='allBlogs'),
    path('<int:blog_id>/', views.blogDetails, name='blog_detail') # look for an int that's identified as 'blog_id'
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # To serve media files
