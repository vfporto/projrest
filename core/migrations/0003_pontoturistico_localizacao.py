# Generated by Django 2.2.6 on 2019-10-30 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacoes', '0001_initial'),
        ('core', '0002_pontoturistico_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='localizacao',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='localizacoes.Localizacao'),
        ),
    ]
