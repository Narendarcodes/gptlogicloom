from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages

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

     