from django.shortcuts import render,redirect
from niveau.models import NiveauModel,ParcoursNiveauModel
from niveau.forms import NiveauForms,NiveauParcoursForms
# Create your views here.

def home_niveau(request):
    dataset = NiveauModel.objects.all()
    context = {
        'dataset':dataset
    }
    return render(request,'home_niveau.html',context)

def ajouter_niveau(request):
    form = NiveauForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home_niveau')
    context = {
        'form':form,
    }
    return render(request,'ajouter_niveau.html',context)

def modifier_niveau(request,pk):
    data = NiveauModel.objects.get(id=pk)
    form = NiveauForms(instance = data)
    if request.method == 'POST':
        form = NiveauForms(request.POST,instance = data)
        if form.is_valid():
            form.save()
            return redirect('home_niveau')
    context = {
        'form':form,
    }
    return render(request,'ajouter_niveau.html',context)

def detail_niveau(request,pk):
    data = NiveauModel.objects.get(id=pk)
    context = {
        'data':data,
    }
    return render(request,'detail_niveau.html',context)

def supprimer_niveau(request,pk):
    data = NiveauModel.objects.get(id=pk)
    data.delete()
    return redirect('/')
    context = {
        'data':data,
    }
    return render(request,'home_niveau.html',context)


# Partie de Parcours Niveau

def home_Nparcours(request):
    dataset = ParcoursNiveauModel.objects.all()
    context = {
        'dataset':dataset
    }
    return render(request,'parcours_niveau/home_Nparcours.html',context)

def ajouter_Nparcours(request):
    form = NiveauParcoursForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home_Nparcours')
    context = {
        'form':form,
    }
    return render(request,'parcours_niveau/ajouter_Nparcours.html',context)

def modifier_Nparcours(request,pk):
    data = ParcoursNiveauModel.objects.get(id=pk)
    form = NiveauParcoursForms(instance = data)
    if request.method == 'POST':
        form = NiveauParcoursForms(request.POST,instance = data)
        if form.is_valid():
            form.save()
            return redirect('home_Nparcours')
    context = {
        'form':form,
    }
    return render(request,'parcours_niveau/ajouter_Nparcours.html',context)

def detail_Nparcours(request,pk):
    data = ParcoursNiveauModel.objects.get(id=pk)
    context = {
        'data':data,
    }
    return render(request,'parcours_niveau/detail_Nparcours.html',context)

def supprimer_Nparcours(request,pk):
    data = ParcoursNiveauModel.objects.get(id=pk)
    data.delete()
    return redirect('/')
    context = {
        'data':data,
    }
    return render(request,'parcours_niveau/home_Nparcours.html',context)