from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index),
    path('recent/', views.recent),
    path('news/', views.news),
    path('story/', views.story),
    ]