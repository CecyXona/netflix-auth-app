# movies/urls.py
from django.urls import path
from .views import MovieListView

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie_list'),
]
