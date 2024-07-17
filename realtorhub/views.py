from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User

# Create your views here.
@login_required(login_url='login')
def index(request):
    return HttpResponse('Hello, I am sanyam')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password= password)

        # If the user exist
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            return render(request, 'realtorhub/login.html', {
                'message': "Invalid username or password.",
            })
    else:
        return render(request, 'realtorhub/login.html')


def logout_view(request):
    logout(request)
    return redirect(index)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']

        # Ensure passwords match each other
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, 'realtorhub/register.html', {
                'message': 'Passwords must match.'
            })
        
        if not username or not password:
            return render(request, 'realtorhub/register.html', {
                'message': 'Must provide Username and Password'
            })

        try:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
        except IntegrityError:
            return render(request, 'realtorhub/register.html', {
                'message': 'Username already taken'
            })

        return redirect(index)

    else:
        return render(request, 'realtorhub/register.html')