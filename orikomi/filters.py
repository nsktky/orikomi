from django_filters import filters
from django_filters import FilterSet
from .models import Orikomi, Area, Genre

class OrikomiFilter(FilterSet):
    class Meta:
        model = Orikomi
        fields = ['area', 'genre']