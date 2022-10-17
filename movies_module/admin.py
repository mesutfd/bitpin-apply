from django.contrib import admin
from .models import Movies, MoviesCategory,Rating

# Register your models here.

admin.site.register(Movies)
admin.site.register(Rating)
admin.site.register(MoviesCategory)
