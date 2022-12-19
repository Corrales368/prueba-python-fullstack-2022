# Import django
from django.db import models
from django.db.models import Q

class FilmManager(models.Manager):
    """
    Manager for model Film
    """
    def get_average(self):
        """
        Get average rating all records film
        """
        average = self.annotate(
            avg_rating=models.Avg('filmuser__rating')
        )
        return average

class FilmUserManager(models.Manager):
    """
    Manager for model Film
    """
    def get_by_user_and_film(self, user, film):
        """
        Get average rating all records film
        """
        query = self.filter(Q(user=user) & Q(film=film)).first()
        return query
        
