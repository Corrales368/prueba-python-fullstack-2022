# Import django
from django.db import models
from django.conf import settings

# Import self app
from .choices import TYPE_FILM
from .manager import FilmManager


class Category(models.Model):
    """
    Model for categories
    """
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Film(models.Model):
    """
    Model for film
    """
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    type = models.CharField(max_length=10, choices=TYPE_FILM)

    def __str__(self) -> str:
        return self.name
    
    objects = FilmManager()


class FilmUser(models.Model):
    """
    Model for film and user
    """
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()
    watched = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['film', 'user'], name='algunnombre')
        ]
    
    def __str__(self) -> str:
        return f'{self.film} - {self.user} - {self.rating}'
    