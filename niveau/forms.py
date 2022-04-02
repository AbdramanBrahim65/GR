from django import forms
from niveau.models import NiveauModel

class NiveauForms(forms.ModelForm):
    class Meta:
        model = NiveauModel
        fields = '__all__'