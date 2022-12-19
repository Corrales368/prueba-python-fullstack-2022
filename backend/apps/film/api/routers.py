# Import django
from rest_framework.routers import DefaultRouter

# Import self app
from .viewsets import RandomFilmModelViewSet, FilmModelViewSet, FilmUserModelViewSet


# Declare router
router_film = DefaultRouter()

router_film.register('random-film', RandomFilmModelViewSet, basename='random-film')
router_film.register('films', FilmModelViewSet, basename='films')
router_film.register('films-user', FilmUserModelViewSet, basename='films-user')

urlpatterns = router_film.urls
