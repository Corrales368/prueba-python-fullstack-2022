# Import django
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    """
    Home page 
    """
    template_name = 'home/home.html'


class ExploreTemplateView(TemplateView):
    """
    Section Explore
    """
    template_name = 'home/explore.html'