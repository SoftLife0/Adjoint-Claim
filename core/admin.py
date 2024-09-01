from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CourseAllocation)
admin.site.register(Claim)
admin.site.register(ClaimSession)