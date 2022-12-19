# Import django
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter , SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Import project apps
from apps.shared.api.pagination import MediumPagination

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
        return self.get_serializer().Meta.model.objects.get_random_film()


class FilmModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for filter, order and search films
    """
    serializer_class = FilmSerializer
    http_method_names = ['get']
    queryset = Film.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, OrderingByRating, SearchFilter]
    filterset_fields = ['name']
    ordering = ['pk', 'name', 'category', 'type']
    search_fields = ['name', 'type', 'category__name']
    pagination_class = MediumPagination