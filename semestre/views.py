from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from semestre.models import SemestreModel
from semestre.forms import SemestreForms
# Create your views here.

def home_semestre(request):
    dataset = SemestreModel.objects.all()
    context = {
        'dataset':dataset,
    }
    return render(request,'home_semestre.html',context)

def ajouter_semestre(request):
    form = SemestreForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home_semestre')
    context = {
        'form':form,    
    }
    return render(request,"ajouter_semestre.html",context)

def detail_semestre(request,pk):
    data = SemestreModel.objects.get(id=pk)
    context = {
        'data':data,
    }
    return render(request,'detail_semestre.html',context)

def modifier_semestre(request,pk):
    data = SemestreModel.objects.get(id=pk)
    form = SemestreForms(instance = data)
    if request.method == 'POST':
        form = SemestreForms(request.POST,instance = data)
        if form.is_valid():
            form.save()
            return redirect('home_semestre')
    context = {
        'form':form,
    }
    return render(request,'ajouter_semestre.html',context)

def supprimer_semestre(request,pk):
    data = SemestreModel.objects.get(id=pk)
    data.delete()
    return redirect('/')
    context = {
        'data':data,
    }
    return render(request,'home_semestre.html',context)