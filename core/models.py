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
    

class Claim(models.Model):
    lecturer_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    academic_year = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    month = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.lecturer_name} - {self.course}"

class ClaimSession(models.Model):
    claim = models.ForeignKey(Claim, related_name='sessions', on_delete=models.CASCADE)
    date = models.DateField()
    course_taught = models.CharField(max_length=100)
    start_time = models.CharField(max_length=50, default="00:00")
    end_time = models.CharField(max_length=50, default="00:00")

    def __str__(self):
        return f"Session on {self.date} - {self.course_taught} - {self.start_time} - {self.end_time}"