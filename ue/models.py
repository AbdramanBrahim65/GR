from django.db import models

# Create your models here.

class UeModel(models.Model):
    code = models.CharField(max_length = 255,null=False)
    intitule = models.CharField(max_length = 255 ,null=False)
    credit = models.IntegerField()


    def __str__(self):
        return self.code