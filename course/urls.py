
from django.urls import path
from . import views

urlpatterns = [
    path('checkanswerc1/<slug:slug>/',views.checkanswerc1,name="checkanswerc1"),
    path('checkanswerc2/<slug:slug>/',views.checkanswerc2,name="checkanswerc2"),
    path('course1/<slug:slug>/',views.course1,name="course1"),
    path('course2/<slug:slug>/',views.course2,name="course2"),
    path('course1',views.course1content,name="course1content"),  
    path('course2',views.course2content,name="course1content"),  
]