# Import django
from django import forms

# Import third party apps
from apps.shared.forms import BaseModelForm

# Import self app
from .models import Film, Category, FilmUser


class FilmForm(BaseModelForm):
    """
    Form for model film
    """
    class Meta:
        model = Film
        fields = '__all__'
    

class CategoryForm(BaseModelForm):
    """
    Form for model category
    """
    class Meta:
        model = Category
        fields = '__all__'


class FilmRateItForm(forms.ModelForm):
    """
    Form for model filmuser
    """
    class Meta:
        model = FilmUser
        fields = ('rating', 'watched')
    