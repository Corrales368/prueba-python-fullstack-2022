# Import django
from django.contrib import admin

# Import self app
from .models import Category, Film, FilmUser


admin.site.register(Category)
admin.site.register(Film)
admin.site.register(FilmUser)
