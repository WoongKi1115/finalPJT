from django.urls import path 
from . import views 

urlpatterns=[
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/del/', views.article_delete),
    path('<int:article_pk>/comment_list_create/', views.comment_list_create),
    path('<int:comment_pk>/comment_delete/', views.comment_delete),
]