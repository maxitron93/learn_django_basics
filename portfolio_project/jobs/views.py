from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects # Get all the jobs from the database
    return render(request, 'jobs/home.html', {'jobs': jobs}) # template must be located in jobs/templates/jobs/home.html
