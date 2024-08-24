from django import forms
from django.forms import ModelForm # type: ignore
from .models import *
from django.contrib.auth.models import User

class CourseAllocationForm(forms.ModelForm):
    class Meta:
        model = CourseAllocation
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs['class'] = 'form-control'
        
class CSVUploadForm(forms.Form):
    file = forms.FileField()
        
        