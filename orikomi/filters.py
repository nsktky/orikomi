from django_filters import filters
from django_filters import FilterSet
from .models import Orikomi, Area, Genre

class OrikomiFilter(FilterSet):

    area = filters.ChoiceFilter(label='地域', choices=Area.AREA_SELECT, lookup_expr='exact')
    genre = filters.ChoiceFilter(label='ジャンル', choices=Genre.GENRE_SELECT, lookup_expr='exact')

    class Meta:
        model = Orikomi
        fields = ('area', 'genre',)