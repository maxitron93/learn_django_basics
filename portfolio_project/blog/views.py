from django.shortcuts import render
from django.shortcuts import get_object_or_404 # Gets an object from the database or 404 if not found
from .models import Blog

# Create your views here.
def allBlogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allBlogs.html', {'blogs': blogs})

def blogDetails(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blogDetails.html', {'blog': blog})
