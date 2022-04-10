from django import forms
from semestre.models import SemestreModel

class SemestreForms(forms.ModelForm):
    
    class Meta:
        model = SemestreModel
        fields = '__all__'