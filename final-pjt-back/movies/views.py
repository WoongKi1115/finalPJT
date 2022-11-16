from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer
from .models import Movie

# Create your views here.

@api_view(['GET'])
def get_movies_list(request):
    movies = Movie.objects.all()
    for movie in movies:
        genres = [genre.name for genre in movie.genres.all()]
        movie.genre_ids = genres
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
   