from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('home page')

def user(request):
    return HttpResponse('user page')

def hello(request, name):
    return HttpResponse(f'hello {name}')

def age(request, age):
    return HttpResponse(f'your age is : {age}')