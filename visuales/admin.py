from django.contrib import admin
from .models import (
    Cicloproduccion,
    Alimento,
    Mortalidad,
    imagenes_calificacion,
    metasIP,
)

# from .models import Ciclo_produccion_Form, Alimento_Form, Mortalidad_Form
from import_export.admin import ImportExportModelAdmin



class CicloproduccionAdmin(ImportExportModelAdmin):
    list_display =('id','productor','ciclo','dias_ciclo','lote','raza','sexo')


class AlimentoAdmin(ImportExportModelAdmin):
    list_display =('id','productor','ciclo','sexo','semana')


class MortalidadAdmin(ImportExportModelAdmin):
    list_display =('id','productor','ciclo','sexo','semana')

class MetasIPAdmin(ImportExportModelAdmin):
    list_display =('meta_IP_excelente','meta_IP_bueno','meta_IP_regular')


admin.site.register(Cicloproduccion, CicloproduccionAdmin)
admin.site.register(Alimento, AlimentoAdmin)
admin.site.register(Mortalidad, MortalidadAdmin)
#admin.site.register(imagenes_calificacion)
admin.site.register(metasIP, MetasIPAdmin)