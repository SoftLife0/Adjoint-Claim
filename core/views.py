from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import csv
from io import TextIOWrapper
from .forms import *
from .models import *

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')

def success(request):
    lecturer_name = request.session.get('lecturer_name', 'Lecturer')
    course = request.session.get('course', 'None')
    message = f"Thank you {lecturer_name}, for submitting your Adjunct claim for {course}."
    return render(request, 'success.html', {'message': message})

def claim(request):
    rows = range(1, 15) 

    if request.method == 'POST':
        claim_form = ClaimForm(request.POST)
        session_data = []

        # Gather session data from the form
        for i in rows:
            date = request.POST.get(f'date{i}')
            course_taught = request.POST.get(f'course{i}')
            time_range = request.POST.get(f'time_range{i}')
            if date and course_taught and time_range:
                session_data.append({
                    'date': date,
                    'course_taught': course_taught,
                    'time_range': time_range
                })

        if claim_form.is_valid() and session_data:
            claim = claim_form.save()

            # Save session data
            for session in session_data:
                ClaimSession.objects.create(
                    claim=claim,
                    date=session['date'],
                    course_taught=session['course_taught'],
                    time_range=session['time_range']
                )

            request.session['lecturer_name'] = claim.lecturer_name
            request.session['course'] = claim.course
            return redirect('success')

    else:
        claim_form = ClaimForm()

    return render(request, 'claim.html', {
        'claim_form': claim_form,
        'rows': rows,
    })

def upload_courses(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'This is not a CSV file')
                return redirect('upload-courses')
            
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
            return redirect('upload-courses')
    else:
        form = CSVUploadForm()

    return render(request, 'upload_courses.html', {'form': form})

def create_course(request):
    if request.method == 'POST':
        form = CourseAllocationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course created successfully')
            return redirect('create-course')
    else:
        form = CourseAllocationForm()

    return render(request, 'create_course.html', {'form': form})


def allcourses(request):
    courses = CourseAllocation.objects.all()
    course_count = courses.count()
    return render(request, 'allcourses.html', {'courses': courses, 'course_count':course_count})


def edit_course(request, course_code):
    courses = CourseAllocation.objects.all()
    course = CourseAllocation.objects.get(id=course_code)
    if request.method == 'POST':
        form = CourseAllocationForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully')
            return redirect('allcourses')
    else:
        form = CourseAllocationForm(instance=course)

    return render(request, 'create_course.html', {'form': form, 'courses':courses})