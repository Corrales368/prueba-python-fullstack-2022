# Import django
from django.urls import path

# Import self app
from .views import HomeTemplateView, ExploreTemplateView


app_name = 'home'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('explore', ExploreTemplateView.as_view(), name='explore')
]
