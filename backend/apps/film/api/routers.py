# Import django
from rest_framework.routers import DefaultRouter

# Import self app
from .viewsets import RandomFilmModelViewSet, FilmModelViewSet


# Declare router
router_film = DefaultRouter()

router_film.register('random-film', RandomFilmModelViewSet, basename='random-film')
router_film.register('films', FilmModelViewSet, basename='films')




urlpatterns = router_film.urls