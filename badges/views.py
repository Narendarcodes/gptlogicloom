# badges/views.py

from django.shortcuts import render
from .models import UserProgress

def badges(request):
    user_progress, created = UserProgress.objects.get_or_create(user=request.user)
    user_progress.award_badges()
    badges_earned = user_progress.user.badges.all()
    return render(request, 'badges/badge.html', {'badges': badges_earned, 'user_progress': user_progress})
