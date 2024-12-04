from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse


# Create your views here.
def get_temp(request):
    regform=RegisterForm()
    response=render(request,"app1/gettest.html",context={'regform':regform})
    return response
def getview(request):
    msg="this is get request"
    response=HttpResponse(msg)
    return response
def home(request):
    response=render(request,"app1/index.html")
    return response
def post_temp(request):
    regform=RegisterForm()
    response=render(request,"app1/posttest.html",context={'regform':regform})
    return response
def postview(request):
    msg="this is post view"
    response=HttpResponse(msg)
    return response