from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    # Create new account
    if request.method == 'POST':
        # Check that password match
        if request.POST['password'] == request.POST['confirm_password']:
            # Check for existing username
            try:
                # return render(request, 'products/home.html')
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'message': 'Username already exists'})
            except User.DoesNotExist:
                # Create new user account
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return render(request, 'products/home.html', {'message': 'Account successfully created!'})
        else:
            return render(request, 'accounts/signup.html', {'message': 'Passwords do not match'})  
    else:
        # Go to sign up page
        return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'products/home.html')
