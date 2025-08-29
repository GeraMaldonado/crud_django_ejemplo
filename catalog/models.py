from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, unique= True)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    tmbd_id = models.IntegerField(unique=True)
    imdb_id = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    budget = models.BigIntegerField(null=True, blank=True)
    revenue = models.BigIntegerField(null=True, blank=True)
    popularity = models.FloatField(null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    homepage = models.URLField(max_length=1000, null=True, blank=True)
    poster_path = models.CharField(max_length=255, null=True, blank=True)

    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)

    def __str__(self):
        return self.title
