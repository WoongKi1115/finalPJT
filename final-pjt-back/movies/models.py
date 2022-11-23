from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Genre(models.Model):
    name = models.TextField()

class Actors(models.Model):
    name = models.TextField()

class Movie(models.Model):
    adult = models.BooleanField()
    backdrop_path = models.TextField(null=True)
    genre_ids = models.ManyToManyField(Genre, related_name='movies')
    original_language = models.CharField(max_length=50)
    original_title = models.CharField(max_length=50)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.TextField()
    release_date = models.DateField()
    title = models.CharField(max_length=50)
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.FloatField()
    actors = models.TextField()
    director = models.TextField()


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='ratings')
    rates = models.FloatField(
        default=3, validators=[MinValueValidator(0.5), MaxValueValidator(5)])
    movie_comment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
