from django.shortcuts import render,redirect
from .models import EvalModel
from .forms import EvalForm
# Create your views here.
def home_eval(request):
    dataset = EvalModel.objects.all()
    context = {
        'dataset':dataset,
    }
    return render(request,'list_eval.html',context)

def ajouter_eval(request):
    form = EvalForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home_eval')
    context = {
        'form':form,    
    }
    return render(request,"ajout_eval.html",context)

def detail_eval(request,pk):
    dataset = EvalModel.objects.get(id=pk)
    context = {
        'dataset':dataset,
    }
    return render(request,'detail_eval.html',context)

def modifier_eval(request,pk):
    data = EvalModel.objects.get(id=pk)
    form = EvalForm(instance = data)
    if request.method == 'POST':
        form = EvalForm(request.POST,instance = data)
        if form.is_valid():
            form.save()
            return redirect('home_eval')
    context = {
        'form':form,
    }
    return render(request,'ajout_eval.html',context)

def supprimer_eval(request,pk):
    data = EvalModel.objects.get(id=pk)
    data.delete()
    return redirect('/')
    context = {
        'data':data,
    }
    return render(request,'list_eval.html',context)