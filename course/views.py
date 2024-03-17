from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.html import escape
from profilepage.models import Profile
from .models import Answers
from django.contrib.auth.models import AnonymousUser,User


def course2content(request):
    return render(request, "course/course2/content.html")

def course1content(request):
    return render(request, "course/course1/content.html")

def course1(request, slug):
    return render(request, f"course/course1/{slug}.html")

def course2(request, slug):
    return render(request, f"course/course2/{slug}.html")

def checkanswerc2(request, slug):
    if request.method == 'POST':
        option1 = request.POST.get("q1")
        option2 = request.POST.get("q2")
        
        validslug = escape(slug)

        answers = Answers.objects.filter(topic=validslug).first()
        if answers:
            if option1 == answers.que1 and option2 == answers.que2:
                if isinstance(request.user,AnonymousUser):
                 messages.warning(request,"Well Done! That was Awesome response Please Login to save your progress")
                elif isinstance(request.user,User):
                 user_profile = Profile.objects.filter(user=request.user).first()
                 if user_profile and user_profile.c2progress < answers.prgrscontribution :
                    user_profile.c2progress = answers.prgrscontribution
                    user_profile.save()
                 messages.success(request, f"Well Done! {user_profile.name} That was an Awesome response")
            else:  
                messages.error(request, "Wrong Answers. Try Again!")
        else:
            return redirect("home:error404")
        
        return redirect(f"../../course2/{slug}")

def checkanswerc1(request, slug):
   if request.method == 'POST':
        option1 = request.POST.get("q1")
        option2 = request.POST.get("q2")
        
        validslug = escape(slug)

        answers = Answers.objects.filter(topic=validslug).first()
        if answers:
            if option1 == answers.que1 and option2 == answers.que2:
                if isinstance(request.user,AnonymousUser):
                 messages.warning(request,"Well Done! That was Awesome response Please Login to save your progress")
                elif isinstance(request.user,User):
                 user_profile = Profile.objects.filter(user=request.user).first()
                 if user_profile and user_profile.c1progress < answers.prgrscontribution :
                    user_profile.c1progress = answers.prgrscontribution
                    user_profile.save()
                 messages.success(request, f"Well Done! {user_profile.name} That was an Awesome response")
            else:  
                messages.error(request, "Wrong Answers. Try Again!")
        else:
            return redirect("home:error404")
        
        return redirect(f"../../course1/{slug}")
    
