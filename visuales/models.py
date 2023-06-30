from django.db import models
from django.forms import ModelForm
#from django.contrib.auth.models import User
from accounts.models import CustomUser

# Create your models here.


class Cicloproduccion(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    productor = models.CharField(max_length=1000)
    ciclo = models.IntegerField()
    dias_ciclo = models.IntegerField()
    lote = models.CharField(max_length=1000)
    raza = models.CharField(max_length=1000)
    sexo = models.CharField(max_length=1000)
    aves_iniciales = models.IntegerField()
    aves_finales = models.IntegerField()
    peso_inicial_gramos = models.DecimalField(decimal_places=5, max_digits=1000)
    peso_final_gramos = models.DecimalField(decimal_places=5, max_digits=1000)
    consumo_total_ave_kilogramos = models.DecimalField(
        decimal_places=5, max_digits=1000
    )
    #tasa_mortalidad_total = models.DecimalField(decimal_places=5, max_digits=1000)
    #consumo_total_kilogramos = models.DecimalField(decimal_places=5, max_digits=1000)
    #total_bultos = models.DecimalField(decimal_places=5, max_digits=1000)
    #peso_vivo_total_kilogramos = models.DecimalField(decimal_places=5, max_digits=1000)
    conversion_acumulada = models.DecimalField(decimal_places=5, max_digits=1000)
    indice_productividad = models.DecimalField(decimal_places=5, max_digits=1000)
    #bodega = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "ciclos de produccion"

    # def __str__(self):
    #    return self.productor + self.ciclo +self.raza +self.sexo

    # def get_display_name(self):
    #    return self.productor + self.ciclo +self.raza +self.sexo


class Alimento(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    productor = models.CharField(max_length=1000)
    ciclo = models.IntegerField()
    sexo = models.CharField(max_length=1000)
    semana = models.IntegerField()
    consumo_ave = models.DecimalField(decimal_places=5, max_digits=1000)
    peso_ave = models.DecimalField(decimal_places=5, max_digits=1000)
    c_a_acum = models.DecimalField(decimal_places=5, max_digits=1000)

    class Meta:
        verbose_name_plural = "alimentos"


class Mortalidad(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    productor = models.CharField(max_length=1000)
    ciclo = models.IntegerField()
    sexo = models.CharField(max_length=1000)
    semana = models.IntegerField()
    total_semana = models.IntegerField(null=True)
    total_acumulada = models.IntegerField(null=True)
    acumulada_porcentaje = models.DecimalField(
        decimal_places=50, max_digits=1000, null=True
    )
    saldo_aves = models.IntegerField()

    class Meta:
        verbose_name_plural = "mortalidades"


class imagenes_calificacion(models.Model):
    clasificacion = models.CharField(max_length=20)
    image = models.ImageField(upload_to="visuales/images/")
    class Meta:
        verbose_name_plural = "imagenes de calificacion"


class metasIP(models.Model):
    meta_IP_excelente = models.IntegerField()
    meta_IP_bueno = models.IntegerField()
    meta_IP_regular = models.IntegerField()

    class Meta:
        verbose_name_plural = "Metas IP"
