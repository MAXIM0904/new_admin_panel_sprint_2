from django.urls import path
from . import views

app_name = 'v1'


urlpatterns = [
    path('movies/', views.Movies.as_view(), name='movies'),
]
