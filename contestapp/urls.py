from django.urls import path
from . import views

urlpatterns = [
    path('', views.contest_page, name='contest_page'),
    path('leaderboard1/', views.leaderboard_page1, name='leaderboard_page1'),
    path('context2/', views.context2, name='context2'),
    path('context1/', views.context1, name='context1'),
]
