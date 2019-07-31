from django.urls import path

from . import views

app_name = 'soasite'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/bookmark/', views.bookmark, name='bookmark')
]