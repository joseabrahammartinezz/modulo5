from django.contrib import admin
from .models import Servicio, Tarifa, Socio, SociosServicio


class ServicioAdmin(admin.ModelAdmin):
    list_display = ("cod_servicio", "descripcion", "desc_tarifa", "tipo_cobro")
    ordering = ["cod_servicio"]
    search_fields = ["descripcion"]
    list_filter = ("cod_servicio","descripcion")

admin.site.register(Servicio, ServicioAdmin)

class TarifasAdmin(admin.ModelAdmin):
    list_display = ("cod_tarifa", "cod_servicio", "descripcion", "monto_por_m3", "monto_fijo", "porcentaje_m3", "m3_inicio", "m3_fin")
    ordering = ["cod_tarifa"]
    search_fields = ["descripcion"]
    list_filter = ("cod_tarifa","descripcion")

admin.site.register(Tarifa, TarifasAdmin)

class SociosAdmin(admin.ModelAdmin):
    list_display = ("cod_socio", "nombres","calle")
    ordering = ["cod_socio"]
    search_fields = ["nombres"]
    list_filter = ("cod_socio","nombres")

admin.site.register(Socio, SociosAdmin)

class SociosServicioAdmin(admin.ModelAdmin):
    list_display = ("cod_socio", "cod_servicio")
    ordering = ["cod_socio"]
    search_fields = ["cod_socio"]
    list_filter = ("cod_socio", "cod_servicio")

admin.site.register(SociosServicio, SociosServicioAdmin)