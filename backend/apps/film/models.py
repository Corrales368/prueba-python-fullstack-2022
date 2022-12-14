# Import django
from django.db import models
from django.conf import settings
from django.db.models import Q
from django.core.exceptions import ValidationError

# Import self app
from .choices import TYPE_FILM


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


class FilmUser(models.Model):
    """
    Model for film and user
    """
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()
    watched = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.film} - {self.user}'
    
    # def save(self, *args, **kwargs):
    #     """
    #     Override method save for validate relation 
    #     """
    #     film_by_user = FilmUser.objects.filter(Q(user=self.user) and Q(film=self.film)).count()
    #     if film_by_user > 1:
    #         raise ValidationError(('Invalid value'), code='invalid')
    #     super(FilmUser, self).save(*args, **kwargs)