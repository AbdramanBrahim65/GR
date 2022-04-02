from django.db import models

# Create your models here.

class EtudiantModel(models.Model):
    matricule = models.CharField(max_length = 112,null=True)
    nom = models.CharField(max_length = 200,null=True)
    prenom = models.CharField(max_length = 200,null=True)
    date_naissance = models.DateField(auto_now_add = False)
    lieu_naissance = models.CharField(max_length = 200,null=True)
    
    choix=(
        ('H','Homme'),
        ('F','Femme'),
    )
    sexe = models.CharField(max_length=1,choices=choix)
    class Meta:
        ordering = ['nom']

    def __str__(self):
        return self.matricule
    
    
