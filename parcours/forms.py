from django import forms
from parcours.models import ParcoursModel

class ParcoursForms(forms.ModelForm):
    
    class Meta:
        model = ParcoursModel
        fields = '__all__'