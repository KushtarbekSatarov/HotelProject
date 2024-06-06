from django_filters.rest_framework import FilterSet, NumberFilter
from .models import RoomType


class RoomTypeFilter(FilterSet):
    # min_price = NumberFilter(field_name='price', lookup_expr='gt')
    # max_price = NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = RoomType
        fields = ['room_type', 'hotel']