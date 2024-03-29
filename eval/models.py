from django.db import models
from etudiant.models import EtudiantModel
from ue.models import UeModel
# Create your models here.
class EvalModel(models.Model):
    choix = (
        ('CC','CC'),
        ('TP','TP'),
        ('TPE','TPE'),
        ('EXAMEN','EXAMEN')
    )
    typeEval = models.CharField(max_length = 200,choices=choix)
    note = models.FloatField()
    matricule = models.ForeignKey(EtudiantModel,on_delete=models.CASCADE)
    code_ue = models.ForeignKey(UeModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.typeEval