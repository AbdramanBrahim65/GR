from django import forms
from ue.models import UeModel

class UeForms(forms.ModelForm):
    
    class Meta:
        model = UeModel
        fields = '__all__'