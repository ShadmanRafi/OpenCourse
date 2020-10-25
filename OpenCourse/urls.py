"""OpenCourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from register import views as vr
from django.contrib.auth.views import LoginView
from courses import views as cv

urlpatterns = [
    path('home/', vr.home_view, name='home'),
    path('create/', cv.course_create_view, name='create'),
    path('all_course/', cv.all_course_view, name='all_course'),
    path('my_courses/', cv.my_courses_view, name='my_courses'),
    path('course/<int:id>', cv.course_view, name='course'),
    path('register/', vr.register_view , name='register'),
    path('logout/', vr.logout_view , name='logout'),
    path('login/', LoginView.as_view() , name='login'),
    path('admin/', admin.site.urls),
]
