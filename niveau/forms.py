from django import forms
from .models import NiveauModel,ParcoursNiveauModel

class NiveauForms(forms.ModelForm):
    class Meta:
        model = NiveauModel
        fields = '__all__'


class NiveauParcoursForms(forms.ModelForm):
    class Meta:
        model = ParcoursNiveauModel
        fields = '__all__'