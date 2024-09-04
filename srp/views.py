from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import csv
from io import TextIOWrapper
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import JsonResponse, HttpResponse


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user = user.username
            messages.success(request, f'Welcome Back {user} 😊!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid login, please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


