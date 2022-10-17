from django.urls import path
from .views import MoviesListView,rate_movie

urlpatterns = [
    path("", MoviesListView.as_view(), name="home_page"),
]
