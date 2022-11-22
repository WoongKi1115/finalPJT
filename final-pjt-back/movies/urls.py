from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_movies_list),
    path('<int:movie_pk>/moviecomment/',views.get_moviecommment_list)
]
