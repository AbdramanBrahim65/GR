# Generated by Django 3.2.8 on 2022-03-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EtudiantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=12)),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=200)),
                ('sexe', models.BooleanField()),
            ],
            options={
                'ordering': ['matricule'],
            },
        ),
    ]
