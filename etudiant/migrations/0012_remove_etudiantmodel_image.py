# Generated by Django 3.2.8 on 2022-04-12 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0011_auto_20220411_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiantmodel',
            name='image',
        ),
    ]