from django.contrib import admin
from .models import Conocimientos_Adicionales, Curriculum, Estudios, Experiencia_Laboral


admin.site.register(Curriculum)
admin.site.register(Conocimientos_Adicionales)
admin.site.register(Estudios)
admin.site.register(Experiencia_Laboral)
