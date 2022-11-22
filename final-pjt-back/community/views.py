from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({"message": "no auth"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['DELETE'])
def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if not request.user.is_authenticated:
        return Response({"message": "no auth"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        article.delete()
        return Response({'id':article_pk})

@api_view(['GET', 'POST'])
def comment_list_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        if not request.user.is_authenticated:
            return Response({"message": "no auth"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article)
            return Response(serializer.data)

@api_view(['DELETE'])
def comment_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if not request.user.is_authenticated:
        return Response({"message": "no auth"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        comment.delete()
        return Response({'id':comment_pk})
