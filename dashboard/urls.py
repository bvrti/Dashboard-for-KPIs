from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.uploadImg, name = 'uploadImg'),
    path('logout/', views.logout, name = 'logout'),
    path('login/', include("django.contrib.auth.urls")),
]
