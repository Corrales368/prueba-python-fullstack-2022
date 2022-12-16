# Import django
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter , SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Import 
from random import choice

# Import self app
from apps.film.models import Film
from .serializers import FilmSerializer
from .filters import OrderingByRating

class RandomFilmModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for get random film
    """
    serializer_class = FilmSerializer
    http_method_names = ['get']

    def get_queryset(self):
        """
        Override method get_queryset for get random film
        """
        # get all films
        all_films = self.get_serializer().Meta.model.objects.all()
        # validate that data exists
        if all_films:
            # get all films only pk as list
            all_films_pk_list = all_films.values_list('pk', flat=True)
            # get id random with function choice from random
            random_pk = choice(all_films_pk_list)
            # get film with random_pk
            random_film = all_films.filter(pk=random_pk)
            return random_film
        else:
            return all_films



class FilmModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for filter, order and search films
    """
    serializer_class = FilmSerializer
    http_method_names = ['get']
    queryset = Film.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, OrderingByRating, SearchFilter]
    filterset_fields = ['name']
    ordering = ['pk', 'name', 'category', 'type', ]
    search_fields = ['name', 'type', 'category__name']