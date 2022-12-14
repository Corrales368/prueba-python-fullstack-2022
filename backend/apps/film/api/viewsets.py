# Import django
from rest_framework import viewsets

# Import self app
from apps.film.models import Film
from .serializers import FilmSerializer

class RandomFilm(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    http_method_names = ['get']

