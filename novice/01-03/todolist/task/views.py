from django.shortcuts import render


def index (req):
    return render (req, 'task/index.html')

# Create your views here.
