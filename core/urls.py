# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('adjunct', views.home, name='home'),
    path('index', views.index, name='index'),
    path('search', views.search, name='search'),
    path('upload_courses/', views.upload_courses, name='upload-courses'),
    path('create_course/', views.create_course, name='create-course'),
    path('allcourses/', views.allcourses, name='allcourses'),
    path('edit_course/<str:course_code>', views.edit_course, name='edit-course'),
    path('claim', views.claim, name='claim'),
    path('allclaims', views.allclaims, name='allclaims'),
    path('claim_details/<int:pk>/', views.claim_details, name='claim-details'),
    path('success', views.success, name='success'),

]