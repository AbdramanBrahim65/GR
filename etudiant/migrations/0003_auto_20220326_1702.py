# Generated by Django 3.2.8 on 2022-03-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0002_auto_20220326_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiantmodel',
            name='lieu_naissance',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='etudiantmodel',
            name='matricule',
            field=models.CharField(max_length=112, null=True),
        ),
        migrations.AlterField(
            model_name='etudiantmodel',
            name='nom',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='etudiantmodel',
            name='prenom',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
