from django.urls import path
from . import views

urlpatterns = [
    path('', views.contest_page, name='contest_page'),
    path('leaderboard1/', views.leaderboard_page1, name='leaderboard_page1'),
]
