from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import ExpressionWrapper
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from movies.models import FilmWork, GenreFilmWork, PersonFilmWork
from movies.api.v1 import serializers
from rest_framework.response import Response
from django.db.models import Q
from django.db.models import TextField
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


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
    queryset = FilmWork.objects.prefetch_related('genr', 'pers').all().annotate(genres=ArrayAgg('genr__name')).\
        annotate(actors=ArrayAgg('pers__full_name'),
                 filter=ExpressionWrapper(Q(personfilmwork__role__gt='actor'), output_field=TextField())).\
        annotate(writers=ArrayAgg('pers__full_name'),
                 filter=ExpressionWrapper(Q(personfilmwork__role__gt='writer'), output_field=TextField())).\
        annotate(directors=ArrayAgg('pers__full_name'),
                 filter=ExpressionWrapper(Q(personfilmwork__role__gt='director'), output_field=(TextField())))


class MoviesId(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        isinstance = FilmWork.objects.prefetch_related('genr', 'pers').filter(id=pk).\
            annotate(genres=ArrayAgg('genr__name')).\
            annotate(actors=ArrayAgg('pers__full_name'),
                     filter=ExpressionWrapper(Q(personfilmwork__role__gt='actor'), output_field=TextField())).\
            annotate(writers=ArrayAgg('pers__full_name'),
                     filter=ExpressionWrapper(Q(personfilmwork__role__gt='writer'), output_field=TextField())). \
            annotate(directors=ArrayAgg('pers__full_name'),
                     filter=ExpressionWrapper(Q(personfilmwork__role__gt='director'), output_field=(TextField())))
        if isinstance:
            serializer = serializers.FilmWorkSerializer(isinstance, many=True)
            return JsonResponse({'type': str(type(serializer)), 'required': serializer.data}, safe=False)
        else:
            return JsonResponse({'type': 'Запрос фильма по несуществующему UUID'},
                                json_dumps_params={'ensure_ascii': False})
