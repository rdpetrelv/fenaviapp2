from django.contrib import admin
from django.urls import path, include
from visuales import views as visualesviews
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('conversion/', visualesviews.visual_Conversion_Alimenticia2, name = 'conversion'),
    path('mortalidad/', visualesviews.visual_Mortalidad2, name = 'mortalidad'),
    path('peso/', visualesviews.visual_Evolucion_Peso2, name = 'peso'),
    path('gananciapeso/', visualesviews.visual_Ganancia_Peso2, name = 'ganancia'),
    path('indiceproductividad/', visualesviews.visual_Indice_productividad2,name='indiceproductividad'),
    path('Resumenciclo', visualesviews.visual_Resumen, name = 'resumen'),
]

urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)