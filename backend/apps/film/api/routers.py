# Import django
from rest_framework.routers import DefaultRouter

# Import self app
from .viewsets import RandomFilm

router_film = DefaultRouter()
router_film.register('api/random-film', RandomFilm)
urlpatterns = router_film.urls