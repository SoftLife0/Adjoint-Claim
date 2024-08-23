from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import csv
from io import TextIOWrapper
from .forms import *
from .models import *

def home(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def upload_courses(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'This is not a CSV file')
                return redirect('upload_courses')
            
            file_data = TextIOWrapper(csv_file, encoding='utf-8')
            reader = csv.DictReader(file_data)

            for row in reader:
                course_code = row['CourseCode']
                # Handle empty fields and convert to correct types
                try:
                    credit_hours = int(row['CreditHrs']) if row['CreditHrs'] else None
                    no_of_students = int(row['NoOfStudents']) if row['NoOfStudents'] else None
                except ValueError:
                    credit_hours = None
                    no_of_students = None

                # Update or create the course record
                CourseAllocation.objects.update_or_create(
                    course_code=course_code,
                    defaults={
                        'level': row['Level'],
                        'course_title': row['CourseTitle'],
                        'credit_hours': credit_hours,
                        'stream': row['Stream'],
                        'campus': row['Campus'],
                        'lecturer': row['Lecturer'],
                        'lecturer_title': row['LecturerTitle'],
                        'lecturer_status': row['LecturerStatus'],
                        'no_of_students': no_of_students,
                        'department': row['Department']
                    }
                )

            messages.success(request, 'CSV file has been processed successfully')
            return redirect('upload_courses')
    else:
        form = CSVUploadForm()

    return render(request, 'upload_courses.html', {'form': form})

def create_course(request):
    if request.method == 'POST':
        form = CourseAllocationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course created successfully')
            return redirect('home')
    else:
        form = CourseAllocationForm()

    return render(request, 'create_course.html', {'form': form})
