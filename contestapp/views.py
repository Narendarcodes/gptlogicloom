from django.shortcuts import render
from .models import Contest
from django.utils import timezone

def contest_page(request):
    upcoming_contests = Contest.objects.filter(start_date__gte=timezone.now())
    previous_contests = Contest.objects.filter(end_date__lt=timezone.now())
    return render(request, 'contests/contest_page.html', {'upcoming_contests': upcoming_contests, 'previous_contests': previous_contests})


def leaderboard_page1(request):
    # Your logic to fetch leaderboard data goes here
    return render(request, 'contests/leaderboard1.html')


def context1(request):
    # your view logic here
    return render(request, 'contests/context1.html')
def context2(request):
    # your view logic here
    return render(request, 'contests/context2.html')