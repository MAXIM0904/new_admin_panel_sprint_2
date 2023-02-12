from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from movies.models import FilmWork
from movies.api.v1 import serializers
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def previous_number(self):
        numbers = self.page.number - 1 if self.page.number - 1 >= 1 else None
        return numbers

    def next_number(self):
        numbers = self.page.number + 1 if self.page.number + 1 <= self.page.paginator.num_pages else None
        return numbers

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'prev': self.previous_number(),
            'next': self.next_number(),
            'results': data
        })


class Movies(ListAPIView):

    serializer_class = serializers.FilmWorkSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        x = FilmWork.objects.all()
        print(x)
        y = self.serializer_class(x[0])
        print(y.data)
        return x