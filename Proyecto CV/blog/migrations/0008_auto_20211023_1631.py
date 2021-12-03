# Generated by Django 3.2.8 on 2021-10-23 19:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211020_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiencia_laboral',
            name='periodo_trabajado',
        ),
        migrations.AddField(
            model_name='estudios',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='En caso que esté en curso, la fecha puede ser estimativa', verbose_name='Fecha de finalización'),
        ),
        migrations.AddField(
            model_name='experiencia_laboral',
            name='desde',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='experiencia_laboral',
            name='hasta',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='carta',
            field=models.TextField(blank=True, help_text='OPCIONAL', verbose_name='Carta de presentación'),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='edad',
            field=models.IntegerField(default=18, help_text='Debes ser mayor de 18 años para registrar un Curriculum'),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='fecha_de_nacimiento',
            field=models.DateField(help_text='El formato debe ser dd/mm/aaaa'),
        ),
        migrations.AlterField(
            model_name='estudios',
            name='comentarios',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='estudios',
            name='nivel',
            field=models.CharField(choices=[('Primario', 'Primario'), ('Secundario', 'Secundario'), ('Terciario', 'Terciario'), ('Universitario', 'Universitario')], default='Primario', max_length=15),
        ),
        migrations.AlterField(
            model_name='experiencia_laboral',
            name='descripcion',
            field=models.TextField(verbose_name='Descripción del puesto y tareas realizadas'),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='comentarios',
            field=models.TextField(blank=True),
        ),
    ]