from django.http import HttpResponse
from django.shortcuts import render
from flask import request
from flask import request

def home(request):
    return render(request, 'home.html')