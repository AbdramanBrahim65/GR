from django.db import models
from parcours.models import ParcoursModel
# Create your models here.

class NiveauModel(models.Model):
    code = models.CharField(max_length=12,null=True)
    title = models.CharField(max_length=255,null=True)
    description = models.CharField(max_length = 1000,null=True)
    class Meta:
        ordering = ['code']
    def __str__(self):
        return self.code

class ParcoursNiveauModel(models.Model):
    code_niveau = models.ForeignKey(NiveauModel,on_delete=models.CASCADE)
    code_parcours = models.ForeignKey(ParcoursModel,on_delete=models.CASCADE)

    description = models.CharField(max_length=144)
    
    def __str__(self):
        return f"{self.code_niveau}{self.code_parcours}"
    