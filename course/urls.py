
from django.urls import path
from . import views

urlpatterns = [
    path('checkanswer/<slug:slug>/',views.checkanswer,name="checkanswer"),
    path('course1/<slug:slug>/',views.course1,name="course1"),
    path('course2/<slug:slug>/',views.course2,name="course2"),    
]