from django.db import models
from apps.flujo import properties

# Create your models here.
class Moneda(models.Model):
    pais = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)


class Activo(models.Model):
    nombre_activo = models.CharField(max_length=255)
    valor_activo = models.DecimalField(decimal_places=2)
    moneda = models.ForeignKey(Moneda,on_delete=models.CASCADE)
    tiempo = models.CharField(max_length=30,choices=properties.TIPO_TIEMPO)
    valor_tiempo =  models.PositiveIntegerField()


class Acredor(models.Model):
    nombre = models.CharField(max_length=200)


class Obligaciones(models.Model):
    acredor_obligacion = models.ForeignKey(Acredor, on_delete=models.CASCADE)
    saldo_obligacion =models.DecimalField()
    cuota_obligacion = models.DecimalField()
    tiempo = models.CharField(max_length=30, choices=properties.TIPO_TIEMPO)
    valor_tiempo = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=500)
    tasa_obligacion = models.DecimalField(decimal_places=2)


class Categoria(models.Model):
    tipo = models.CharField(max_length=30, choices=properties.TIPO_MOVIMIENTO)
    nombre = models.CharField(max_length=200)


class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)


class Movimiento(models.Model):
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    fecha = models.DateField()
    nombre_dia = models.CharField(max_length=30, choices=properties.TIPO_DIA_SEMANA)
    nombre = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2,max_digits=10)