# Generated by Django 2.2.6 on 2019-11-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191030_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='comentarios',
            field=models.ManyToManyField(null=True, to='comentarios.Comentario'),
        ),
        migrations.AlterField(
            model_name='pontoturistico',
            name='reviews',
            field=models.ManyToManyField(null=True, to='reviews.Review'),
        ),
    ]
