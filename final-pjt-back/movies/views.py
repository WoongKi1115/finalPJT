from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer, RatingSerializer
from .models import Movie, Rating

# Create your views here.


@api_view(['GET'])
def get_movies_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_moviecommment_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        moviecomments = movie.ratings.all()
        serializer = RatingSerializer(moviecomments, many=True)
        return Response(serializer.data)
    else:
        if not request.user.is_authenticated:
            return Response({"message": "no auth"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data)
