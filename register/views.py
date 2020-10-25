from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse
# from django.forms import inlineformset_fectory


# Create your views here.
def register_view(response):
    form = UserCreationForm()
    if response.method == 'POST':
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(response, 'register.html', context)


def logout_view(response):
    logout(response)
    return redirect('home')


def home_view(request, *args, **kwargs):
    return render(request, "home.html")