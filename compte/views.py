from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def accessPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Vous n'êtes pas admin ou bien les données sont mal saisie")
    
    return render(request,'home_compte.html')


def logoutUser(request):
    logout(request)
    return redirect('accueil')
    