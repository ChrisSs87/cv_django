# Generated by Django 3.2.8 on 2021-10-20 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211020_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculum',
            name='idiomas',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='nivel_de_idioma',
        ),
    ]
