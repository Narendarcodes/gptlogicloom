
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('editprofile/profileedithandle',views.profileedithandle,name="profileedithandle"),
    path('editprofile/change_password',views.change_password,name="change_password"),
     path('badges/', views.badges, name='badges'),
     path('recent_badge/', views.recent_badge, name='recent_badge'),

]