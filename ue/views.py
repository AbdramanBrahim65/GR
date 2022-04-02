from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from ue.models import UeModel
from ue.forms import UeForms
# Create your views here.

def home_ue(request):
    dataset = UeModel.objects.all()
    context = {
        'dataset':dataset,
    }
    return render(request,'home_ue.html',context)

def ajouter_ue(request):
    form = UeForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home_ue')
    context = {
        'form':form,    
    }
    return render(request,"ajouter_ue.html",context)

def detail_ue(request,pk):
    data = UeModel.objects.get(id=pk)
    context = {
        'data':data,
    }
    return render(request,'detail.html',context)

def modifier_ue(request,pk):
    data = UeModel.objects.get(id=pk)
    form = UeForms(instance = data)
    if request.method == 'POST':
        form = UeForms(request.POST,instance = data)
        if form.is_valid():
            form.save()
            return redirect('home_ue')
    context = {
        'form':form,
    }
    return render(request,'ajouter_ue.html',context)

def supprimer_ue(request,pk):
    data = UeModel.objects.get(id=pk)
    data.delete()
    return redirect('/')
    context = {
        'data':data,
    }
    return render(request,'home_ue.html',context)