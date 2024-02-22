from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Profile

@login_required
def profile(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    if user_profile is None:
        return redirect('home')
    else:
        context = {'user_profile': user_profile}
        return render(request, 'profile/userprofile.html', context)
    
@login_required
def editprofile(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    if user_profile is None:
        return redirect('home')
    else:
        context = {'user_profile': user_profile}
        return render(request, 'profile/editprofile.html', context)



    
