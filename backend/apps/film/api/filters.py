# Import django
import django_filters
from django import forms

# Import self app
from apps.film.models import Film


class OrderingByRating(django_filters.FilterSet):
    """
    Ordering custom for rating
    """
    order_by = django_filters.BooleanFilter(
        widget=forms.HiddenInput(),
        method='filter_order_by',
    )

    class Meta:
        model = Film
        fields = [
            'order_by'
        ]

    def filter_queryset(self, request, queryset, view):
        """
        Ordering custom for order_by rating
        """
        # get query_param
        ordering = request.query_params.get("ordering", None)
        if 'rating' == ordering:
            return self.Meta.model.objects.get_average().order_by('avg_rating')
        if '-rating' == ordering:
            return self.Meta.model.objects.get_average().order_by('-avg_rating')
        return queryset