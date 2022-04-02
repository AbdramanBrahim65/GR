from django.shortcuts import render
from niveau.models import NiveauModel
from niveau.forms import NiveauForms
# Create your views here.

def home_niveau(request):
    dataset = NiveauModel.objects.all()
    context = {
        'dataset':dataset
    }
    return render(request,'home_niveau.html',context)

def ajouter_niveau(request):
    data = NiveauForms(request.POST)
    if data.is_valid():
        data.save()
        return redirect('home_niveau')
    context = {
        'data':data,
    }
    return render(request,'ajouter_niveau.html',context)

def modifier_niveau(request,pk):
    data = NiveauModel.objects.get(id=pk)
    form = NivauForms(instance = data)
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
