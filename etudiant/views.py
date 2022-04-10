from django.shortcuts import render,redirect
from .models import EtudiantModel
from etudiant.forms import EtudiantForms
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

@login_required(login_url='accueil')
def home(request):
    etudiants = EtudiantModel.objects.all()
    context = {
        'etudiants':etudiants, 
    }
    return render(request,'liste_etudiants.html',context)

@login_required(login_url='accueil')
def ajout_views(request):
    form = EtudiantForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form':form,
    }
    return render(request,'ajouter.html',context)

@login_required(login_url='accueil')
def modifier_views(request,pk):
    data = EtudiantModel.objects.get(id=pk)
    form = EtudiantForms(instance = data)
    if request.method == 'POST':
        form = EtudiantForms(request.POST,instance = data)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form,
    }
    return render(request,"ajouter.html",context)

@login_required(login_url='accueil')
def details_views(request,pk):
    etudiant = EtudiantForms.objects.get(id=pk)
    context = {
        'etudiant':etudiant
    }
    return render(request,'details.html',context)

@login_required(login_url='accueil')
def supprimer_views(request,pk):
    etudiant = EtudiantForms.objects.get(id=pk)
    etudiant.delete()
    return redirect('/')
    context = {
        'etudiant':etudiant,
    }
    return render(request,'liste_etudiants.html',context)