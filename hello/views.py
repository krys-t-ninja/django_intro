from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

# Create your views here.
from django.urls import path, include
# from django.contrib import admin 
urlpatterns = [
    path('', include('hello.urls')),
    #path('admin/', admin.sites.urls)
] 