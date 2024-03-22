from django.urls import path
from .views import badges

urlpatterns = [
    path('', badges, name='badges'),
]