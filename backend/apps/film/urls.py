# Import django
from django.urls import path

# Import self app
from . import views 
app_name = 'film'

urlpatterns = [
    path('random-film', views.RandomFilmTemplateView.as_view() ,name='random-film'),
    path('rate-it', views.RatingCreateOrUpdate.as_view(), name='rate-it-film'),

    path('create-film', views.FilmCreateView.as_view(), name='create-film'),
    path('list-film', views.FilmListView.as_view(), name='list-film'),
    path('update-film/<pk>', views.FilmUpdateView.as_view(), name='update-film'),
    path('delete-film/<pk>', views.FilmDeleteView.as_view(), name='delete-film'),
    path('detail-film/<pk>', views.FilmDetailView.as_view(), name='detail-film'),

    path('create-category', views.CategoryCreateView.as_view(), name='create-category'),
    path('list-category', views.CategoryListView.as_view(), name='list-category'),
    path('update-category/<pk>', views.CategoryUpdateView.as_view(), name='update-category'),
    path('delete-category/<pk>', views.CategoryDeleteView.as_view(), name='delete-category'),
    path('detail-category/<pk>', views.CategoryDetailView.as_view(), name='detail-category'),
]


