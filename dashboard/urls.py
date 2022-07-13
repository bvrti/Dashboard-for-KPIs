from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('smt/', views.indexSmt, name = 'indexSmt'),
    path('cba/', views.indexCba, name = 'indexCba'),
    path('fa/', views.indexFa, name = 'indexFa'),
    path('upload/', views.uploadImg, name = 'uploadImg'),
    path('uploadSmt/', views.uploadImgSmt, name = 'uploadImgSmt'),
    path('uploadCba/', views.uploadImgCba, name = 'uploadImgCba'),
    path('uploadFa/', views.uploadImgFa, name = 'uploadImgFa'),
    path('logout/', views.logout, name = 'logout'),
    path('login/', include("django.contrib.auth.urls")),
]
