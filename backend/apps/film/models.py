# Import django
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Import self app
from .choices import TYPE_FILM
from .manager import CategoryManager, FilmManager, FilmUserManager


class Category(models.Model):
    """
    Model for categories
    """
    name = models.CharField(max_length=50)

    objects = CategoryManager()

    def __str__(self) -> str:
        return self.name


class Film(models.Model):
    """
    Model for film
    """
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    type = models.CharField(max_length=10, choices=TYPE_FILM)

    objects = FilmManager()
    
    def __str__(self) -> str:
        return self.name
    


class FilmUser(models.Model):
    """
    Model for film and user
    """
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    watched = models.BooleanField(default=False)

    objects = FilmUserManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['film', 'user'], name='unique_film_user')
        ]
    
    def __str__(self) -> str:
        return f'{self.film} - {self.user} - {self.rating} - {self.watched}'
    