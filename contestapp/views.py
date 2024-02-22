from django.shortcuts import render
from .models import Contest
from django.utils import timezone

def contest_page(request):
    upcoming_contests = Contest.objects.filter(start_date__gte=timezone.now())
    previous_contests = Contest.objects.filter(end_date__lt=timezone.now())
    return render(request, 'contests/contest_page.html', {'upcoming_contests': upcoming_contests, 'previous_contests': previous_contests})