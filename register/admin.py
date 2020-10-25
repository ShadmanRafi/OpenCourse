from django.contrib import admin
from courses.models import Course, Enrolments

# Register your models here.
admin.site.register(Course)
admin.site.register(Enrolments)
