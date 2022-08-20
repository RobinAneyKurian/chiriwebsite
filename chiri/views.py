from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import logo, quotes, Logoimage, Dailyquotes, Videolink, Addsimage, Engmemes
from django.contrib import messages

# Create your views here.
def home(request):

    img = Logoimage.objects.all()
        
    return render(request,'home.html', {'img': img})

def malayalam(request):

        return render(request,'malayalam.html')

def english(request):

    engvideo = Videolink.objects.all()
    adds = Addsimage.objects.all()
    

    return render(request, 'english.html', {"engvideo": engvideo, "adds": adds})

def englishmemes(request):

    engmemes = Engmemes.objects.all()

    return render(request, 'englishmemes.html', {"engmemes": engmemes} )

def base(request):

    quotes = Dailyquotes.objects.all()
    
    return render(request, "base.html", {'quotes': quotes})