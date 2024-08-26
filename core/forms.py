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
        

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['lecturer_name', 'course', 'academic_year', 'semester', 'month']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs['class'] = 'form-control'

class ClaimSessionForm(forms.ModelForm):
    class Meta:
        model = ClaimSession
        fields = ['date', 'course_taught', 'start_time', 'end_time']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs['class'] = 'form-control'