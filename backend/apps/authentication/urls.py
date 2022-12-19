# Import django
from django.urls import path

# Import self app
from .views import login_project

app_name = 'authentication'

urlpatterns = [
    path('login', login_project, name='login')
]
