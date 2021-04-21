from django.shortcuts import render, redirect

# Create your views here.


def login_view(request):
    return render(request, 'login.html', {})


def sign_view(request):
    return render(request, 'register.html', {})
