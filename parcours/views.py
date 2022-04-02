from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from parcours.models import ParcoursModel
from parcours.forms import ParcoursForms
# Create your views here.

def home_parcours(request):
    dataset = ParcoursModel.objects.all()
    context = {
        'dataset':dataset,
    }
    return render(request,'home_parcours.html',context)

def ajouter_parcours(request):
    form = ParcoursForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home_parcours')
    context = {
        'form':form,    
    }
    return render(request,"ajouter_parcours.html",context)

def detail_parcours(request,pk):
    data = ParcoursModel.objects.get(id=pk)
    context = {
        'data':data,
    }
    return render(request,'detail_parcours.html',context)

def modifier_parcours(request,pk):
    data = ParcoursModel.objects.get(id=pk)
    form = ParcoursForms(instance = data)
    if request.method == 'POST':
        form = ParcoursForms(request.POST,instance = data)
        if form.is_valid():
            form.save()
            return redirect('home_parcours')
    context = {
        'form':form,
    }
    return render(request,'ajouter_parcours.html',context)

def supprimer_parcours(request,pk):
    data = ParcoursModel.objects.get(id=pk)
    data.delete()
    return redirect('/')
    context = {
        'data':data,
    }
    return render(request,'home_parcours.html',context)