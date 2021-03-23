from django_filters import filters
from django_filters import FilterSet
from .models import Orikomi

class OrikomiFilter(FilterSet):

    area = filters.ChoiceFilter(label='地域', choices=Orikomi.AREA_SELECT, lookup_expr='exact')
    genre = filters.ChoiceFilter(label='ジャンル', choices=Orikomi.GENRE_SELECT, lookup_expr='exact')

    class Meta:
        model = Orikomi
        fields = ('area', 'genre',)