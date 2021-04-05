from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def explore(request):
    return render(request, 'explore.html', {})
