# Generated by Django 4.2.2 on 2023-06-21 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='visivel',
            field=models.BooleanField(default=False, verbose_name='Ativo'),
        ),
    ]