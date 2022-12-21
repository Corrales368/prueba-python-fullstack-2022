# Import django
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import ProtectedError

# Import self app
from .models import Film, Category, FilmUser
from .forms import FilmForm, CategoryForm, FilmRateItForm
from .filters import FilmFilterSet


class RandomFilmTemplateView(LoginRequiredMixin, TemplateView):
    """
    View for get random film
    """
    template_name = 'film/film/random.html'

    def get_context_data(self, **kwargs):
        """
        Override method get_context_data for get random film
        """
        context = super().get_context_data(**kwargs)
        context['random_film'] = Film.objects.get_random_film()
        return context


class FilmCreateView(LoginRequiredMixin, CreateView):
    """
    Create new film
    """
    template_name = 'film/film/create.html'
    model = Film
    form_class = FilmForm
    success_url = reverse_lazy('film:list-film')


class FilmListView(LoginRequiredMixin, ListView):
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


    def get_context_data(self, **kwargs):
        """
        Override method get_context_data for add form of filters
        """
        context = super().get_context_data(**kwargs)
        context['fomr_filter'] = FilmFilterSet(
            self.request.GET, queryset=self.get_queryset())
        context['object_list'] = context['fomr_filter'].qs
        return context


class FilmUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update a film
    """
    template_name = 'film/film/update.html'
    model = Film
    form_class = FilmForm
    success_url = reverse_lazy('film:list-film')


class FilmDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a film
    """
    template_name = 'film/film/delete.html'
    model = Film
    success_url = reverse_lazy('film:list-film')

    def get(self, request, *args, **kwargs):
        """
        Override get method for delete film without confirmation and template
        """
        return self.delete(request, *args, **kwargs)


class FilmDetailView(LoginRequiredMixin, DetailView):
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
        context['form_rate_it'] = FilmRateItForm(
            instance=FilmUser.objects.get_by_user_and_film(self.request.user, kwargs['object']))
        return context

    def post(self, request, pk):
        form = FilmRateItForm(
            request.POST, instance=FilmUser.objects.get_by_user_and_film(self.request.user, pk))
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.film = Film.objects.get(pk=pk)
            instance.save()
            return HttpResponseRedirect(reverse_lazy('film:list-film'))
        else:
            return render(request, self.template_name, {'object': self.get_object(), 'form_rate_it': form, 'errors': form.errors})


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new category
    """
    template_name = 'film/category/create.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('film:list-category')


class CategoryListView(LoginRequiredMixin, ListView):
    """
    List all categories
    """
    template_name = 'film/category/list.html'
    model = Category

    def get_queryset(self):
        """
        Override method get_queryset for change query a custom manager
        """
        return self.model.objects.get_films_by_category()


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update a category
    """
    template_name = 'film/category/update.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('film:list-category')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a category
    """
    template_name = 'film/category/delete.html'
    model = Category
    success_url = reverse_lazy('film:list-category')

    def post(self, request, *args, **kwargs):
        """
        Override method post for show message alert if instance have relations
        """
        try:
            self.object = self.get_object()
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(success_url)
        except ProtectedError as e:
            return render(request, self.template_name, {'object': self.get_object(), 'protected_objects': e.protected_objects, 'error' : e})


class CategoryDetailView(LoginRequiredMixin, DetailView):
    """
    Detail a category
    """
    template_name = 'film/category/detail.html'
    model = Category
