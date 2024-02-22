from django.shortcuts import render, redirect
from django.http import HttpResponse
from profilepage.models import Profile
from .models import Answers
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.



def course1(request,slug):
    return render(request,f"course/course1/{slug}.html")

def course2(request,slug):
    return render(request,f"course/course2/{slug}.html")

def checkanswer(request, slug):
    if request.method == 'POST':
        option1 = request.POST.get("q1")
        option2 = request.POST.get("q2")
        
        # Retrieve Answers object based on the slug, or return a 404 error if not found
        answer = get_object_or_404(Answers, topic=slug)
        
        # Print the object or its attributes for debugging
        if option1==answer.que1 and option2 == answer.que2 :
            user_profile = Profile.objects.filter(user=request.user).first()
            if answer.submission != True:
               user_profile.c2progress = user_profile.c2progress + 0.9
               answer.submission = True
               user_profile.save() 
            messages.success(request, "Well Done That was Awesome respnse")
            return redirect(f"../../course2/{slug}")
        else:
            messages.error(request, "Wrong Answers Try Again!`")
            return redirect(f"../../course2/{slug}")
            
        


    
