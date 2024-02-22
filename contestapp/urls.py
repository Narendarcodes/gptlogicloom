from django.urls import path
from . import views

urlpatterns = [
    path('', views.contest_page, name='contest_page'),
]
