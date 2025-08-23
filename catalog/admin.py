from django.contrib import admin
from .models import Movie, Genre 

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "release_date", "vote_average")
    search_fields = ("title", "original_title", "imdb_id")
    list_filter = ("genres", "release_date")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
