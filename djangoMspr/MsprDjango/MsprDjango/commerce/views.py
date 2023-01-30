from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from commerce import forms
from commerce.forms import RegisterForm, SignInForm
from commerce.models import RegisteredUser


# def index(request):
#    return HttpResponse('Bienvenue rue du commerce')
# def index(request):
#    return HttpResponse("""
#   <!doctype html>
#   <html>
#   <head>
#     <title></title>
#   </head>
#   <body>
#   Welcome to Django!
#   </body>
#   </html>
#
# """)
def index(request):
    return render(request, 'home.html')


def aboutUS(request):
    return render(request, 'aboutUS.html')


def services(request):
    return render(request, 'services.html')


def contactUS(request):
    return render(request, 'contactUS.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('signin')
    else:
        form = RegisterForm()
        user_info = {'form': form}
        return render(request, 'register.html', user_info)


def signin(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            # authenticate user
            usr = request.POST['name']
            pwd = request.POST['password']
            try:
                user = RegisteredUser.objects.get(name=usr)
                if user.name == usr and user.password ==pwd:
                    request.session['user'] = user.name
                    return redirect('index')
                else:
                    messages.error(request, "Invalid username or password")
                    return redirect('signin')
            except RegisteredUser.DoesNotExist:
                messages.error(request, "Invalid username or password")
                return redirect('signin')
    else:
        form = SignInForm()
        user_info = {'form': form}
        return render(request, 'signin.html', user_info)

def commercial(request):
    return render(request, 'commercial.html')

def manager(request):
    return render(request, 'manager.html')

def salarie(request):
    return render(request, 'salaries.html')
