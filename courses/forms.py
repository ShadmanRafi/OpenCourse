from django import forms
from django.forms import ModelForm
from .models import Course, Enrolments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CourseForm(forms.ModelForm):
    class Meta:
        model =  Course
        fields = [
            'course_name'
        ]


class EnrolmentForm(forms.ModelForm):
    class Meta:
        model =  Enrolments
        fields = [
            'course', 'user_id', 'is_complete'
        ]


class EnrolmentNewForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    user_id = forms.IntegerField()
    is_complete = forms.BooleanField()