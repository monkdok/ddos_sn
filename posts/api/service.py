from django_filters import rest_framework as filters, DateRangeFilter, DateFilter, NumberFilter, \
    DateTimeFromToRangeFilter, RangeFilter, DateFromToRangeFilter, IsoDateTimeFromToRangeFilter

from ..models import Like


class LikeFilter(filters.FilterSet):
    date_from = DateFilter(field_name='created', lookup_expr=('gt'), )
    date_to = DateFilter(field_name='created', lookup_expr=('lt'))

    class Meta:
        model = Like
        fields = ['post']
