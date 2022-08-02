from django.shortcuts import render
from .models import logo


# Create your views here.
def home(request):

    images = logo.objects.all()
        
    return render(request,'home.html', {'images':images})