# Import django
from rest_framework.routers import DefaultRouter

# Import self app
from .viewsets import RandomFilmModelViewSet, FilmModelViewSet


# Declare router
router_film = DefaultRouter()

router_film.register('api/random-film', RandomFilmModelViewSet, basename='random-film')
router_film.register('api/films', FilmModelViewSet, basename='films')




urlpatterns = router_film.urls