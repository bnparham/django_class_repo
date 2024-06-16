from django.shortcuts import render
from django.views import View

# Create your views here.
def home(req):

    data = [
        {
            "title": 'A',
            "subtitle": 'A subtitle',
            "text": '10'
        },
        {
            "title": 'B',
            "subtitle": 'B subtitle',
            "text": '20'
        },
        {
            "title": 'C',
            "subtitle": 'C subtitle',
            "text": '30'
        },
        {
            "title": 'D',
            "subtitle": 'D subtitle',
            "text": '40'
        },
        {
            "title": 'E',
            "subtitle": 'E subtitle',
            "text": '50'
        },
    ]

    return render(
        req,
        'home/index.html',
        {
            'data': data
        }
    )

class Main(View):
    def get(self):
        ...
    def post(self):
        ...