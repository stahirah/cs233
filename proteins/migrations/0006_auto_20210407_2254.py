# Generated by Django 3.1.7 on 2021-04-08 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proteins', '0005_proteinimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proteinimage',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='proteinimage',
            name='protein',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='proteins.protein'),
        ),
    ]
