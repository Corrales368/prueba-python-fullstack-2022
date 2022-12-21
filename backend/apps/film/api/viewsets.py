# Import django
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter , SearchFilter
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Import project apps
from apps.shared.api.pagination import MediumPagination

# Import self app
from apps.film.models import Film, FilmUser
from .serializers import FilmSerializer, FilmUserSerializer
from .filters import OrderingByRating


class RandomFilmModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for get random film
    """
    serializer_class = FilmSerializer
    http_method_names = ['get']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Override method get_queryset for get random film
        """
        return self.get_serializer().Meta.model.objects.get_random_film()


class FilmModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for CRUD operations and filter, order and search films by 
    queryparams
    """
    serializer_class = FilmSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    queryset = Film.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, OrderingByRating, SearchFilter]
    filterset_fields = ['name']
    ordering = ['pk', 'name', 'category', 'type']
    search_fields = ['name', 'type', 'category__name']
    pagination_class = MediumPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class FilmUserModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for CRUD operations filmuser
    """
    serializer_class = FilmUserSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    queryset = FilmUser.objects.all()
    pagination_class = MediumPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

