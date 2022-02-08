from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user/', views.user, name="user"),
    path('user/post/', views.post, name="post"),
    path('user/post/<int:post_id>', views.each, name="each"),
    path('user/like/', views.like, name="like"),
    path('user/save/', views.save, name="save"),
]