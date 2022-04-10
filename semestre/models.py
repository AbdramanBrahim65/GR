from django.db import models

# Create your models here.

class SemestreModel(models.Model):
    code = models.CharField(max_length=12,null=True)
    title = models.CharField(max_length=255,null=True)
    description = models.CharField(max_length = 1000,null=True)
    class Meta:
        ordering = ['code']
    def __str__(self):
        return self.code
    