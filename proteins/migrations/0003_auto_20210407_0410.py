# Generated by Django 3.1.7 on 2021-04-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proteins', '0002_protein_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protein',
            name='protein_name',
            field=models.CharField(max_length=1000),
        ),
    ]
