from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:blog_id>/', views.detail, name="detail"),
    path('post/', views.post, name="post"),
    path('mainapp/create', views.create, name="create"),
    path('createpost/', views.createpost, name="createblog"),
]