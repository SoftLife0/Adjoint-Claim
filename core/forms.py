from django import forms
from django.forms import ModelForm # type: ignore
from .models import *
from django.contrib.auth.models import User

class CourseAllocationForm(forms.ModelForm):
    class Meta:
        model = CourseAllocation
        fields = '__all__'
        
class CSVUploadForm(forms.Form):
    file = forms.FileField()
        
        