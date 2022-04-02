from django.shortcuts import render,redirect
from .models import EtudiantModel
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
    try :
        matricule = request.POST['matricule']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        date_naissance = request.POST['date_naissance']
        lieu_naissance = request.POST['lieu_naissance']
        sexe = request.POST['sexe']
    except MultiValueDictKeyError :
        sexe = False
    if request.method == 'POST':
        etudiant = EtudiantModel(matricule=matricule,nom=nom,prenom=prenom,date_naissance = date_naissance,lieu_naissance = lieu_naissance ,sexe = sexe)
        etudiant.save()
        return redirect('home')
    return render(request,'ajouter.html')

@login_required(login_url='accueil')
def modifier_views(request,pk):
    objet = EtudiantModel.objects.get(id=pk)
    
    return render(request,"ajouter.html")

@login_required(login_url='accueil')
def details_views(request,pk):
    etudiant = EtudiantModel.objects.get(id=pk)
    context = {
        'etudiant':etudiant
    }
    return render(request,'details.html',context)

@login_required(login_url='accueil')
def supprimer_views(request,pk):
    etudiant = EtudiantModel.objects.get(id=pk)
    
    etudiant.delete()
    return redirect('/')
    context = {
        'etudiant':etudiant,
    }
    return render(request,'liste_etudiants.html',context)

