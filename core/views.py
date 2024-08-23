from django.http import HttpResponse
from django.shortcuts import render
from flask import request
from flask import request

def home(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')