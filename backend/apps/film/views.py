# Import django
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Import 
from random import choice

# Import self app
from .models import Film, Category, FilmUser
from .forms import FilmForm, CategoryForm, FilmRateItForm


class RandomFilmTemplateView(TemplateView):
    """
    View for get random film
    """
    template_name = 'film/film/random.html'

    def get_context_data(self, **kwargs):
        """
        Override method get_context_data for get random film
        """
        context = super().get_context_data(**kwargs)
        # get all films
        all_films = Film.objects.all()
        # validate that data exists
        if all_films:
            # get all films only pk as list
            all_films_pk_list = all_films.values_list('pk', flat=True)
            # get id random with function choice from random
            random_pk = choice(all_films_pk_list)
            # get film with random_pk
            random_film = all_films.filter(pk=random_pk).first()
            context['film'] = random_film
            return context
        return context



class FilmCreateView(CreateView):
    """
    Create new film
    """
    template_name = 'film/film/create.html'
    model = Film
    form_class = FilmForm


class FilmListView(ListView):
    """
    List all films
    """
    template_name = 'film/film/list.html'
    model = Film

    def get_queryset(self):
        """
        Override method get_queryset for change query a custom manager
        """
        return self.model.objects.get_average()


class FilmUpdateView(UpdateView):
    """
    Update a film
    """
    template_name = 'film/film/update.html'
    model = Film
    form_class = FilmForm


class FilmDeleteView(DeleteView):
    """
    Delete a film
    """
    template_name = 'film/film/delete.html'
    model = Film
    success_url = reverse_lazy('category:list')

    def get(self, request, *args, **kwargs):
        """
        Override get method for delete film without confirmation and template
        """
        return self.delete(request, *args, **kwargs)


class FilmDetailView(DetailView):
    """
    Detail a film
    """
    template_name = 'film/film/detail.html'
    model = Film

    def get_queryset(self):
        """
        Override method get_queryset for change query a custom manager
        """
        return self.model.objects.get_average()

    def get_context_data(self, **kwargs):
        """
        Override metho get_context_data for include form
        """
        context = super().get_context_data(**kwargs)
        context['form_rate_it'] = FilmRateItForm(instance=FilmUser.objects.get_by_user_and_film(self.request.user, kwargs['object']))
        return context
        
    def post(self, request, pk):
        form = FilmRateItForm(request.POST, instance=FilmUser.objects.get_by_user_and_film(self.request.user, pk))
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.film = Film.objects.get(pk=pk)
            instance.save()
            return HttpResponseRedirect(reverse_lazy('film:list-film'))
        else:
            return render(request, self.template_name, {'object' : self.get_object(), 'form_rate_it' : form,'errors' : form.errors})


class RatingCreateOrUpdate(TemplateView):
    """
    Rate it film get or create
    """
    def post(self, request):
        print(request.POST)
        form = FilmRateItForm(request.POST, instance=FilmUser.objects.get_by_user_and_film(self.request.user, self.kwargs['object']))
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.film = self.kwargs['object']
            instance.save()
        return 

    def get(self):
        pass


class CategoryCreateView(CreateView):
    """
    Create a new category
    """
    template_name = 'film/category/create.html'
    model = Category
    form_class = CategoryForm


class CategoryListView(ListView):
    """
    List all categories
    """
    template_name = 'film/category/list.html'
    model = Category


class CategoryUpdateView(UpdateView):
    """
    Update a category
    """
    template_name = 'film/category/update.html'
    model = Category
    form_class = CategoryForm


class CategoryDeleteView(DeleteView):
    """
    Delete a category
    """
    template_name = 'film/category/delete.html'
    model = Category
    success_url = reverse_lazy('category:list')

    def get(self, request, *args, **kwargs):
        """
        Override get method for delete category without confirmation and template
        """
        return self.delete(request, *args, **kwargs)

    
class CategoryDetailView(DetailView):
    """
    Detail a category
    """
    template_name = 'film/category/detail.html'
    model = Category