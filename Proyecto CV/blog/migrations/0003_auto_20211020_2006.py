# Generated by Django 3.2.8 on 2021-10-20 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211020_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculum',
            name='fecha_de_nacimiento',
        ),
        migrations.AddField(
            model_name='curriculum',
            name='Otros',
            field=models.CharField(blank=True, help_text='especificar idioma y nivel', max_length=20),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='nivel_de_idioma',
            field=models.CharField(choices=[('inicial', 'Inicial'), ('intermedio', 'Intermedio'), ('avanzado', 'Avanzado')], default='inicial', max_length=25),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='dni',
            field=models.CharField(help_text='ingresar el nro de corrido y sin puntos', max_length=8),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='idiomas',
            field=models.CharField(choices=[('ingles', 'Ingles'), ('frances', 'Francés'), ('italiano', 'Italiano'), ('alemán', 'Alemán'), ('ninguno', 'Ninguno')], default='ninguno', max_length=25),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='telefono',
            field=models.CharField(help_text='ingresar el nro sin 0 ni 15', max_length=10),
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(choices=[('ingles', 'Ingles'), ('frances', 'Francés'), ('italiano', 'Italiano'), ('alemán', 'Alemán'), ('ninguno', 'Ninguno')], default='ninguno', max_length=25)),
                ('nivel_de_idioma', models.CharField(choices=[('inicial', 'Inicial'), ('intermedio', 'Intermedio'), ('avanzado', 'Avanzado')], default='inicial', max_length=25)),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.curriculum')),
            ],
        ),
    ]
