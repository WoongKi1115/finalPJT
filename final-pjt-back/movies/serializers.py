from rest_framework import serializers
from .models import Movie, Rating

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields= '__all__'

class RatingSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Rating
        fields= '__all__'
        read_only_fields = ('user', 'movie', 'created_at', 'username')