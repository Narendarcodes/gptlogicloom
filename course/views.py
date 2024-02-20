from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def course1(request):
   return HttpResponse("this is course1 page")
def index(request):
   return HttpResponse("this course index page")
    
