# Generated by Django 3.1.6 on 2021-02-13 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
        ('core', '0007_pontoturistico_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='localizacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='localizacao.localizacao'),
        ),
    ]