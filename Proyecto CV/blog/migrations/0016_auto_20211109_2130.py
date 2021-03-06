# Generated by Django 3.2.8 on 2021-11-10 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_curriculum_nacionalidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='instagram',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='linkedin',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='otros',
            field=models.CharField(blank=True, help_text='especifica red y usuario', max_length=50),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='twitter',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='foto',
            field=models.ImageField(upload_to='imagenes'),
        ),
        migrations.DeleteModel(
            name='Redes_Sociales',
        ),
    ]
