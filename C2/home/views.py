from django.shortcuts import render

# Create your views here.
def home(req, name=''):

    age = 22
    students = [
        'ali', 'reza', 'parham', 'navid'
    ]

    return render(
        req,
        "home/home.html",
        context={
            "name": name,
            "age": age,
            "students": students,
        }
    )