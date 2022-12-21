# Import django
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


def login_project(request):
    """
    Login for project
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('home:explore'))
        else:
            return HttpResponseRedirect('/')
    else:
        return render(request, 'authentication/login/login.html')
