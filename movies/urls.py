from django.urls import __path__
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movie_index'),
    path('<int:movie_id>', views.detail, name='movie_detail')
]
