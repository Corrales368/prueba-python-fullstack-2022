# Import django
from django.db import models

# Import 
from random import choice


class CategoryManager(models.Manager):
    """
    Manager for model Category
    """
    def get_films_by_category(self):
        """
        Get number of films by category
        """
        return self.annotate(
            count_film_by_category = models.Count('film')
        )


class FilmManager(models.Manager):
    """
    Manager for model Film
    """
    def get_average(self):
        """
        Get the average rating of all films records and count the views
        """
        average = self \
        .annotate(avg_rating=models.Avg('filmuser__rating')) \
        .annotate(count_watched=models.Count('filmuser__watched', filter=models.Q(filmuser__watched=True)))
        return average
    
    def get_random_film(self):
        # get all films
        all_films = self.all()
        # validate that data exists
        if all_films:
            # get all films only pk as list
            all_films_pk_list = all_films.values_list('pk', flat=True)
            # get id random with function choice from random
            random_pk = choice(all_films_pk_list)
            # get film with random_pk
            random_film = all_films.filter(pk=random_pk)
            return random_film
        else:
            return all_films

class FilmUserManager(models.Manager):
    """
    Manager for model Film
    """
    def get_by_user_and_film(self, user, film):
        """
        Get average rating all records film
        """
        query = self.filter(models.Q(user=user) & models.Q(film=film)).first()
        return query
        
