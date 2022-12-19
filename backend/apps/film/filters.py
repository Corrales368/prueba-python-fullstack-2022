# Import third project apps
import django_filters

# Import self app
from .models import Film


class FilmFilterSet(django_filters.FilterSet):
    """
    FilterSet for name icontains, category, type
    """
    name = django_filters.CharFilter(lookup_expr='icontains')
    rating = django_filters.OrderingFilter(
        fields=(
            ('avg_rating', 'avg_rating'),
        ),
    )

    o = django_filters.OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('name', 'name'),
            ('category', 'category'),
            ('type', 'type'),
        ),

    )
    class Meta:
        model = Film
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Override method init for add class css bootstrap to forms
        """
        super().__init__(*args, **kwargs)
        for filter in self.filters:
            self.filters[filter].field.widget.attrs.update({'class': 'form-control'})



        

        
    
