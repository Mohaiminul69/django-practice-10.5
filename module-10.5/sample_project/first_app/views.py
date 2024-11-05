from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def home(request):
    d = {
        "author": "rahim",
        "sentence": "How are you everybody?",
        "age": 4,
        "list": ["python", "is", "best"],
        "birthday": datetime.now(),
        "emptyValue": "",
        "courses": [
            {"id": 1, "name": "Python", "fee": 5000},
            {"id": 2, "name": "Django", "fee": 6000},
        ],
    }
    return render(request, "first_app/home.html", d)
