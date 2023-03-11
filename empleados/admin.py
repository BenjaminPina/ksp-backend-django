from django.contrib import admin

from .models import Empleado, Beneficiario


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'estatus']
    list_filter = ['estatus']
    search_fields = ['nombre_completo']
    ordering = ['nombre_completo']


@admin.register(Beneficiario)
class Beneficiario(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['nombre_completo']
    ordering = ['nombre_completo']
