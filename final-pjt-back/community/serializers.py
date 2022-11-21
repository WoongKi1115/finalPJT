from rest_framework import serializers
from .models import Article, Comment
from accounts.serializers import UserSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields = ('id', 'title', 'content', 'user', 'username')

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = ('id','user', 'article', 'content', 'created_at', 'updated_at', 'username')
        read_only_fields = ('user', 'article', 'created_at', 'updated_at')


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(
        source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', )

