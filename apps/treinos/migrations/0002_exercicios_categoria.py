# Generated by Django 4.2.2 on 2023-07-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treinos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercicios',
            name='categoria',
            field=models.CharField(default=1, max_length=100, verbose_name='Categoria'),
            preserve_default=False,
        ),
    ]
