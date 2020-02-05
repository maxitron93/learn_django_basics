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
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'message': 'Passwords do not match'})  
    else:
        # Go to sign up page
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        # Try to authenticate. If authenticated, returns valid User object
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'message': 'Wrong username or password'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
