from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('loginhandle',views.loginhandle,name='login'),
    path('logout',views.logouthandle,name='logout'),
    path('feedbackhandle',views.feedbackhandle,name='feedbackhandler'),
   
]
