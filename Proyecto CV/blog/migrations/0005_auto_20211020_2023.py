# Generated by Django 3.2.8 on 2021-10-20 23:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211020_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curriculum',
            old_name='Otros',
            new_name='otros',
        ),
        migrations.AddField(
            model_name='curriculum',
            name='fecha_de_nacimiento',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
