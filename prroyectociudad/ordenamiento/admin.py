from django.contrib import admin

# Importar los modelos
from ordenamiento.models import Parroquia, Barrio

# Register your models here.
class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo',)
    search_fields = ('nombre',)


class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre',
        'numero_viviendas',
        'numero_parques',
        'numero_edificios_residenciales',
        'parroquia')
    search_fields = ('nombre', 'parroquia__nombre')


admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Barrio, BarrioAdmin)
