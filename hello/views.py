from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Team

def index(request):
    return HttpResponse("Hello, world!")

def home(request):
    team = Team.objects.all()
    return HttpResponse("Hello, " + team[0].name + "!")
    #return render(request, "index.html", {"team": team}