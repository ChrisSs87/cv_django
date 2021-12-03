from django.db import models
from django.db.models.expressions import Value
from django.db.models.fields import CharField, NullBooleanField
from django.utils import timezone


otros = "Otros (especificar)"
ingles = "ingles"
frances = "frances"
italiano = "italiano"
aleman = "alemán"
inicial = "inicial"
intermedio = "intermedio"
avanzado = "avanzado"
idiomas_opciones = [
    (ingles, "Ingles"),
    (frances, "Francés"),
    (italiano, "Italiano"),
    (aleman, "Alemán"),
    (otros, "Otros (especificar)")
]
idiomas_nivel = [
    (inicial, "Inicial"),
    (intermedio, "Intermedio"),
    (avanzado, "Avanzado")
]
curso = "En curso"
finalizado = "Finalizado"
abandonado = "Abandonado"
primario = "Primario"
secundario = "Secundario"
terciario = "Terciario"
universitario = "Universitario"
estado_estudio_lista = [
    (curso, "En curso"),
    (finalizado, "Finalizado"),
    (abandonado, "Abandonado")
]
nivel_estudio_lista = [
    (primario, "Primario"),
    (secundario, "Secundario"),
    (terciario, "Terciario"),
    (universitario, "Universitario")
]
class Curriculum(models.Model):
    nombre_completo = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField(help_text="El formato debe ser dd/mm/aaaa")
    edad = models.IntegerField(default=18, help_text="Debes ser mayor de 18 años para registrar un Curriculum")
    nacionalidad = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, help_text="ingresar el nro de corrido y sin puntos")
    domicilio = models.CharField(max_length=250)
    localidad = models.CharField(max_length=250, help_text="Ingrese provincia y localidad")
    telefono = models.CharField(max_length=10, help_text = "ingresar el nro sin 0 ni 15")
    email = models.EmailField(max_length=254)
    foto = models.ImageField(upload_to="imagenes", max_length=100)
    hobbies = models.TextField(verbose_name="Hobbies y tiempo libre", help_text="OPCIONAL. Describa actividades que realiza por fuera de su actividad laboral", blank=True)
    carta = models.TextField(verbose_name="Carta de presentación", help_text="OPCIONAL", blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)
    otros = models.CharField(max_length=50, blank=True, help_text="especifica red y usuario")


class Estudios(models.Model):
    curriculum = models.ForeignKey(to=Curriculum, on_delete=models.CASCADE, related_name="estudios")
    nivel = models.CharField(
        max_length=15,
        choices=nivel_estudio_lista,
        default=primario
    )
    carrera = models.CharField(max_length=100)
    institucion = models.CharField(max_length=50)
    estado = models.CharField(
        max_length=15,
        choices=estado_estudio_lista,
        default=curso
    )
    fecha_de_inicio_estudio = models.DateField(default=timezone.now, verbose_name="Fecha de finalización", help_text="En caso que esté en curso, la fecha puede ser estimativa")


class Conocimientos_Adicionales(models.Model):
    curriculum = models.ForeignKey(to=Curriculum, on_delete=models.CASCADE, related_name="conocimientos")
    idioma = models.CharField(
        max_length = 25,
        choices = idiomas_opciones,
        default = ingles,
        blank = True
    )
    nivel_de_idioma = models.CharField(
        max_length = 25,
        choices = idiomas_nivel,
        default = inicial
    )
    comentarios = models.TextField(blank=True, help_text="Opcional")


class Experiencia_Laboral(models.Model):
    curriculum = models.ForeignKey(to=Curriculum, on_delete=models.CASCADE, related_name="experiencia")
    lugar = models.CharField(max_length=250, verbose_name="Lugar de trabajo (Empresa,Institución, etc)")
    puesto = models.CharField(max_length=50)
    desde = models.DateField(default=timezone.now)
    hasta = models.DateField(default=timezone.now)    
    nombre_completo = models.TextField(verbose_name="Descripción del puesto y tareas realizadas")
    referencias = models.CharField(max_length=10, help_text="Opcional. Ingresar TE de contacto sin 0 ni 15", blank=True)
    referencias2 = models.CharField(max_length=250, help_text="ingrese nombre y puesto de la referencia", verbose_name="Datos de referencia", blank=True)
    
    def __str__(self):
        return self.nombre_completo
