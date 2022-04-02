from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def accueil(request):
    return render(request,"home_barbillard.html")

def barbillard_views(request):
    return render(request,"barbillard.html")

def synthese(request):
    return render(request,"synthese.html")

def ue(request):
    return render(request,"ue.html")