from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import logo, quotes, Logoimage, Dailyquotes
from django.contrib import messages

# Create your views here.
def home(request):

    img = Logoimage.objects.all()
        
    return render(request,'home.html', {'img': img})

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:  
                user = User.objects.create_user(username=username, password1 = password1, password2=password2, first_name=first_name, last_name=last_name)
                user.save();
                print("User created")
                

        else:
            messages.info(request, "password not matching")
            return redirect('register')

        return redirect('/')

    else:
        return render(request,'register.html')


# def register(request):

#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 == password2:
#             user = User.objects.create_user(username=username, password1 = password1, password2=password2, first_name=first_name, last_name=last_name)
#             user.save();
#             print('user created')
#             return redirect('/')
#     else:
#         print('Password not matching')
#     return render(request, 'register.html')

def login(request):

    return render(request, 'login.html')

def base(request):

    quotes = Dailyquotes.objects.all()
    
    return render(request, "base.html", {'quotes': quotes})