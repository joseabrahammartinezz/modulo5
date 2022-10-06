from email.policy import default
from wsgiref.validate import validator
from django.db import models
from .validators import validar_monto, validar_modalidad_ingreso
from django.core.validators import RegexValidator

class TipoCobro(models.TextChoices):
    EXTRA = 'E', 'EXTRA'
    MENSUAL = 'M', 'MENSUAL'   

class Servicio(models.Model):
    cod_servicio = models.CharField(primary_key=True, max_length=10, unique= True, validators=[RegexValidator('^SER-[0-9]+$','Error de formato: SER-###')])
    descripcion = models.CharField(max_length=255)
    desc_tarifa = models.CharField(max_length=255)
    obs = models.CharField(max_length=255, blank=True, null=True)
    multa_dia = models.FloatField( default=0)
    tipo_cobro = models.CharField(
        max_length=45, 
        choices = TipoCobro.choices,
        default="E"
    )

    class Meta:
        managed = False
        db_table = 'servicios'

    def __str__(self):
        return "Cod Servicio - %s" % self.cod_servicio + " " + self.descripcion

class Tarifa(models.Model):
    cod_tarifa = models.CharField(primary_key=True, max_length=15)
    cod_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='cod_servicio') 
    descripcion = models.CharField(max_length=100)
    monto_por_m3 = models.FloatField()
    porcentaje_m3 = models.FloatField()
    m3_inicio = models.FloatField()
    m3_fin = models.FloatField()
    monto_fijo = models.DecimalField(decimal_places=2, max_digits=10, validators=[validar_monto,])

    class Meta:
        managed = False
        db_table = 'tarifas'
        unique_together = (('cod_tarifa', 'cod_servicio'),)

    def __str__(self):
        return "Cod Tarifa - %s" % self.cod_tarifa + " " + self.descripcion

class Socio(models.Model):
    cod_socio = models.CharField(primary_key=True, max_length=15)
    codigo_anterior = models.CharField(max_length=45)
    ci = models.CharField(max_length=20, blank=True, null=True)
    nombres = models.CharField(max_length=255)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    celular = models.CharField(max_length=100, blank=True, null=True)
    nro_factura_luz = models.CharField(max_length=100, blank=True, null=True)
    modalidad_ingreso = models.CharField(max_length=55, validators=[validar_modalidad_ingreso,])
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=45)
    zona = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    manzano = models.CharField(max_length=100)
    lote = models.CharField(max_length=100)
    calle = models.CharField(max_length=255)
    frente_ml = models.FloatField()
    superficie = models.FloatField()
    rta = models.CharField(max_length=45)
    fecha_rta = models.DateField()
    codigo_catastral = models.CharField(max_length=55)
    obs = models.CharField(max_length=255)
    orden_manzano = models.IntegerField()
    categoria = models.CharField(max_length=45)
    generar_cobros = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'socios'
        unique_together = (('cod_socio', 'codigo_anterior'),)

    def __str__(self):
        return "Cod Socio - %s" % self.cod_socio + " " + self.nombres

class SociosServicio(models.Model):
    cod_socio =  models.ForeignKey('Socio', models.DO_NOTHING, db_column='cod_socio') 
    cod_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='cod_servicio') 
    obs = models.CharField(max_length=255, default=' ')

    class Meta:
        managed = False
        db_table = 'socios_servicios'
        unique_together = (('cod_socio', 'cod_servicio'),)

    def __str__(self):
        return "Cod Socio - %s" % self.cod_socio 