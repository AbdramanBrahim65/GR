from django import forms

from .models import EvalModel

class EvalForm(forms.ModelForm):
    
    class Meta:
        model = EvalModel
        fields = '__all__'