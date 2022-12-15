# Import django
from django.db import models


class FilmUserManager(models.Manager):
    """
    Manager for model FilmUser
    """
    def get_average(self):
        """
        Get average rating of all records filmuser 
        """
        average = self.aggregate(models.Avg('rating'))
        return average               