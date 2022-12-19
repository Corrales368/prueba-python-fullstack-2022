# Import django
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'


class ExploreTemplateView(TemplateView):
    template_name = 'home/explore.html'