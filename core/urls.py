# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('upload_courses/', views.upload_courses, name='upload-courses'),
    path('create_course/', views.create_course, name='create-course'),
    path('allcourses/', views.allcourses, name='allcourses'),

]