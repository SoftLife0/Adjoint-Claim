from django import forms
from django.forms import ModelForm # type: ignore
from .models import *
from django.contrib.auth.models import User

class AdjointForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        
        