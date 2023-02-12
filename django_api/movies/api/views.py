from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django_api.movies.models import GenreFilmWork, FilmWork
from django.db import connection



class Movies(ListAPIView):
    permission_classes = (AllowAny,)
    paginate_by = 2
    model = FilmWork

    def get(self, request):
        connection.queries
        film = FilmWork.objects.all()
        print(len(connection.queries))
        return JsonResponse({"s": True})


# class CreateOrder(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#
#         connection.queries
#         film = FilmWork.objects.raw('SELECT id, age(creation_date) AS age FROM "content"."film_work"')[0]
#         print(film.title, film.age)
#         print(len(connection.queries))
#         return JsonResponse({"s": True})
