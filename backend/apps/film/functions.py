
def get_queryset(self):
    """
    Override method get_queryset for get random film
    """
    # get all films
    all_films = self.get_serializer().Meta.model.objects.all()
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