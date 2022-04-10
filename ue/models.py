from django.db import models
from niveau.models import ParcoursNiveauModel
from semestre.models import SemestreModel
# Create your models here.

class UeModel(models.Model):
    code = models.CharField(max_length = 255,null=False)
    intitule = models.CharField(max_length = 255 ,null=False)
    credit = models.IntegerField()
    code_p_n = models.ForeignKey(ParcoursNiveauModel,on_delete=models.CASCADE)
    code_semestre = models.ForeignKey(SemestreModel, on_delete=models.CASCADE)
    #code_module = models.ForeignKey()
    def __str__(self):
        return self.code