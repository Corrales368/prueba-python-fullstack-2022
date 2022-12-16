# Import django
from django.db import models


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
        
