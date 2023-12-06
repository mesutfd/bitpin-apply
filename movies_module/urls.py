from django.urls import path
from .views import MoviesListView,rate_movie, MovieDetailView

urlpatterns = [
    path("", MoviesListView.as_view(), name="home_page"),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
]
