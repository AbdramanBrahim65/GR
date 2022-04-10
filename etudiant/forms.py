from django import forms
from etudiant.models import EtudiantModel

class EtudiantForms(forms.ModelForm):
    class Meta:
        model = EtudiantModel
        fields = '__all__'

