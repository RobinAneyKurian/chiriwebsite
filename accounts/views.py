from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def malayalam(request):

    return render(request, 'malayalam.html')


def official(request):
    return render(request, 'official.html')