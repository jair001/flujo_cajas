from django.db import models
from apps.flujo import properties


class Moneda(models.Model):
    pais = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)

# , blank=True, null=True, default=""


class Activo(models.Model):
    nombre_Activo = models.CharField(max_length=255)
    valor_activo = models.DecimalField(decimal_places=2)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE())
    tiempo = models.CharField(max_length=30, choices=properties.TIPO_TIEMPO)
    valor_tiempo = models.PositiveIntegerField()


class Acredor(models.Model):
    nombre = models.CharField(max_length=100)


class Obligaciones(models.Model):
    acredor_obligacion = models.ForeignKey(Acredor, on_delete=models.CASCADE)
    saldo_obligacion = models.DecimalField(decimal_places=2)
    cuota_obligacion = models.DecimalField(decimal_places=2)
    tiempo=models.CharField(max_length=30, choices=properties.TIPO_TIEMPO)
    valor_tiempo = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=500)
    tasa_obligacion = models.DecimalField(decimal_places=2)


class Categoria(models.Model):
    nombre= models.CharField(max_length=255)
    tipo=models.CharField(max_length=50,choices=properties.TIPO_CATEGORIA)


class SubCategoria(models.Model):
    nombre = models.CharField(max_length=255)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE())


class Movimiento(models.Model):
    fecha=models.DateField()
    nombre_dia=models.CharField(max_length=30, choices=properties.DIAS_SEMANA)
    valor=models.DecimalField(decimal_places=2, max_digits=10)
    subcategoria=models.ForeignKey(SubCategoria, on_delete=models.CASCADE())
