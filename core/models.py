from django.db import models

# Create your models here.
class CourseAllocation(models.Model):
    level = models.CharField(max_length=50, blank=True) 
    course_code = models.CharField(max_length=20, unique=True, blank=False, null=False)
    course_title = models.CharField(max_length=200, blank=False, null=False)
    credit_hours = models.PositiveIntegerField(blank=True, null=True)
    stream = models.CharField(max_length=100, blank=True)
    campus = models.CharField(max_length=100, blank=True)
    lecturer = models.CharField(max_length=200, blank=True)
    lecturer_title = models.CharField(max_length=100, blank=True)
    lecturer_status = models.CharField(max_length=100, blank=True)
    no_of_students = models.PositiveIntegerField(blank=True, null=True)
    department = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.course_title} ({self.course_code})"