# Generated by Django 3.2.8 on 2022-03-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0003_auto_20220326_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiantmodel',
            name='sexe',
            field=models.BooleanField(choices=[('H', 'Homme'), ('F', 'Femme')]),
        ),
    ]