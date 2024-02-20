
from django.urls import path
from . import views

urlpatterns = [
    path('course1',views.course1,name='course1'),
    path('',views.index,name='index')
    
]