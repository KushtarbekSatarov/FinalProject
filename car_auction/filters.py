from django_filters.rest_framework import FilterSet, NumberFilter
from .models import Car

class CarFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gt')
    max_price = NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = Car
        fields = ['category', 'car_make', 'model', 'min_price', 'max_price',]