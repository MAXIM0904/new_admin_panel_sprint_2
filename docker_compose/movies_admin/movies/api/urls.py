from django.urls import path
from django.urls import path, include

app_name = 'api'


urlpatterns = [
    path('v1/', include('movies.api.v1.urls')),
]
