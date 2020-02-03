from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def create_account(request):
    return

def login_account(request):
    return

def logout(request):
    return render(request, 'products/home.html')

