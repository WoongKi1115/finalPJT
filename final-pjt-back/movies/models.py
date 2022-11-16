from django.db import models

# Create your models here.
class Genre(models.Model):
	name = models.TextField()


class Movie(models.Model):
	adult = models.BooleanField()
	backdrop_path = models.TextField()
	genre_ids = models.ManyToManyField(Genre, related_name='movies')
	original_language = models.CharField(max_length=50)
	original_title = models.CharField(max_length=50)
	overview = models.TextField()
	popularity = models.FloatField()
	poster_path = models.TextField()
	release_date = models.DateField()
	title = models.CharField(max_length=50)
	video	= models.BooleanField()
	vote_average = models.FloatField()
	vote_count = models.FloatField()