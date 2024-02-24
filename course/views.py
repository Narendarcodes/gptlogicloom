from django.shortcuts import render, redirect
from django.http import HttpResponse
from profilepage.models import Profile
from .models import Answers
from django.contrib import messages
from django.utils.html import escape, strip_tags


# Create your views here.
def course2content(request):
   return render(request,"course/course2/content.html")

def course1content(request):
   return render(request,"course/course1/content.html")


def course1(request,slug):
    return render(request,f"course/course1/{slug}.html")

def course2(request,slug):
    return render(request,f"course/course2/{slug}.html")


#
def checkanswerc2(request, slug):
    if request.method == 'POST':
        option1 = request.POST.get("q1")
        option2 = request.POST.get("q2")
        
        validslug = escape(slug)

        answers = Answers.objects.filter(topic=validslug).first()
        if answers.exists():
            # Print the object or its attributes for debugging
            if option1==answers.que1 and option2 == answers.que2:
              user_profile = Profile.objects.filter(user=request.user).first()
              user_profile.c2progress = answers.prgrscontribution
              user_profile.save() 
              messages.success(request, "Well Done That was an Awesome response")
              return redirect(f"../../course2/{slug}")
            else:
             messages.error(request, "Wrong Answers Try Again!`")
             return redirect(f"../../course2/{slug}")
        else:
           return redirect(request,"home/error404.html")
        
 #increasing progress for the first courese       
def checkanswerc1(request, slug):
    if request.method == 'POST':
        option1 = request.POST.get("q1")
        option2 = request.POST.get("q2")
        
        validslug = escape(slug)

        answers = Answers.objects.filter(topic=validslug).first()
        if answers.exists():
            # Print the object or its attributes for debugging
            if option1==answers.que1 and option2 == answers.que2:
              user_profile = Profile.objects.filter(user=request.user).first()
              user_profile.c1progress = answers.prgrscontribution
              user_profile.save() 
              messages.success(request, "Well Done That was an Awesome response")
              return redirect(f"../../course1/{slug}")
            else:
             messages.error(request, "Wrong Answers Try Again!`")
             return redirect(f"../../course1/{slug}")
        else:
           return redirect(request,"home/error404.html")
            
        
        
            
        


    
