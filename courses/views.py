from django.shortcuts import render, redirect
from .forms import CourseForm, EnrolmentForm,EnrolmentNewForm
from .models import Course, Enrolments


# Create your views here.
def course_create_view(response):
    form = CourseForm(response.POST)
    if response.method == 'POST':
        form = CourseForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(response, "courses/create_course.html", context)


def all_course_view(response):
    c_set = Course.objects.all()
    context = {
        'o_list': c_set
    }
    return render(response, "courses/all_course.html", context)


def my_courses_view(response):
    c_set = Enrolments.objects.all().filter(user_id = response.user.id)
    c_list = []
    for i in c_set:
        c_list.append({
            'name': str(i.course.course_name),
            'id': i.course.id,
        })
    context = {
        'o_list': c_list
    }
    return render(response, "courses/my_courses.html", context)


def course_view(response, id):
    c = Course.objects.get(id=id)
    name = c.course_name
    uid = response.user.id
    context = {
                'course': c,
                'user_id': 0,
                'is_complete': False
            }
    if response.method == 'GET':
        try:
            enrolment = Enrolments.objects.get(course = c, user_id=uid)
            context = {
                'course': c,
                'user_id': uid,
                'is_complete': enrolment.is_complete
            }
        except Enrolments.DoesNotExist:
            pass
        finally:
            v = {'data': context}
            return render(response, "courses/course_page.html", v)

    else:
        enrolment = Enrolments(course=c, user_id = uid, is_complete=False )
        enrolment.save()
        return redirect('home')