from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
from .models import feedback
import re


# Create your views here.
def index(request):
    return render(request,'home/index.html')

def loginhandle(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['username']
        loginpassword=request.POST['password']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def logouthandle(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

def feedbackhandle(request):
    if request.method=="POST":
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if request.user.is_authenticated:
            email=request.user.email
        else:
            email = request.POST["email"]
        feedbackmsg = request.POST["feedback"]
        if not (re.match(email_regex, email) and email.endswith('@gmail.com')):
            messages.error(request,"Please Enter a valid Email")
            return redirect('home')
        if len(feedbackmsg) > 800 :
            messages.error(request,"feedback length should not be greater than 600 characters..try again")
            return redirect('home')
        if email and feedbackmsg :
            feedbackentry = feedback(email=email,feedback=feedbackmsg)
            feedbackentry.save()
            messages.success(request,"Feedback submitted successfully")
        else:
            messages.error(request,"Please fill out the fields")
        return redirect('home')
    else:
        return redirect('error404')
        
       
        


     