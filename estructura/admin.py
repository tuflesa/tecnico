from django.contrib import admin
from .models import Direcciones, Empresa, Zona, Seccion, Equipo

admin.site.register(Empresa)
admin.site.register(Zona)
admin.site.register(Seccion)
admin.site.register(Equipo)
admin.site.register(Direcciones)