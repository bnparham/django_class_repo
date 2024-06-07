from django.shortcuts import render

# Create your views here.
def login(req):
    return render(
        req,
        'account/login.html'
    )

def register(req):
    return render(
        req,
        'account/register.html'
    )