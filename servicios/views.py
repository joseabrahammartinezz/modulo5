from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Servicio, SociosServicio, Tarifa, Socio
from .forms import SocioForm
from .serializers import SocioSerializer, ServicioSerializer, TarifaSerializer, SociosServicioSerializer, ReporteServiciosSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
import logging

def index(request):
    return HttpResponse("Hola Mundo")

def contacto(request, nombre):
    return HttpResponse(f"Bienvenido {nombre} a la clase de Django")
"""
def categoria(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Categoria(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre__contains=filtro_nombre)
    else:
        categorias = Categoria.objects.all()
    print(categorias.query)
    return render(request, "categorias.html", {"categorias": categorias}) 
"""

def servicio(request):
    post_servicio = request.POST.get('servicio')
    if post_servicio:
        q = Servicio(cod_servicio=post_servicio)
        q.save()
    filtro_nombre= request.GET.get("servicio")
    if filtro_nombre:
        servicios = Servicio.objects.filter(cod_servicio__contains=filtro_nombre)
    else:
        servicios = Servicio.objects.all()
    return render(request, "form_servicios.html", {"servicios": servicios})

def tarifa(request):
    post_nombre = request.POST.get('tarifa')
    if post_nombre:
        q = Tarifa(cod_tarifa=post_nombre)
        q.save()
    filtro_nombre= request.GET.get('tarifa')
    if filtro_nombre:
        tarifas = Tarifa.objects.filter(cod_tarifa__contains=filtro_nombre)
    else:
        tarifas = Tarifa.objects.all()
    return render(request, "form_tarifas.html", {
        "Tarifas": tarifas
        })

def socio(request):
    post_nombre = request.POST.get('socio')
    if post_nombre:
        q = Socio(cod_socio=post_nombre)
        q.save()
    filtro_nombre= request.GET.get('socio')
    if filtro_nombre:
        socios = Socio.objects.filter(cod_socio__contains=filtro_nombre)
    else:
        socios = Socio.objects.all()
    return render(request, "form_socios.html", {
        "Socios": socios
        })

def socioFormView(request):
    form = SocioForm()
    socio = None
    
    id_socio = request.GET.get('cod_socio')
    if id_socio:
        # producto = Producto.objects.get(id=id_producto)
        socio = get_object_or_404(Socio, cod_socio=id_socio)
        form = SocioForm(instance=socio)

    if request.method == 'POST':
        if socio:
            form = SocioForm(request.POST, instance=socio)
        else:
            form = SocioForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "formulario_socios.html", {"form": form}) 

def socios_servicio(request):
    post_nombre = request.POST.get('socios_servicio')
    if post_nombre:
        q = SociosServicio(cod_socio=post_nombre)
        q.save()
    filtro_nombre= request.GET.get('socios_servicio')
    if filtro_nombre:
        servicios = SociosServicio.objects.filter(cod_socio__contains=filtro_nombre)
    else:
        servicios = SociosServicio.objects.all()
    return render(request, "form_socios_servicios.html", {
        "Servicios del socio": servicios
        })

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class TarifaViewSet(viewsets.ModelViewSet):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer

class SocioViewSet(viewsets.ModelViewSet):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer

class SocioServicioViewSet(viewsets.ModelViewSet):
    queryset = SociosServicio.objects.all()
    serializer_class = SociosServicioSerializer
   
class ServicioCreateAndList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

@api_view(["GET"])
def servicios_contador(request):
    """
    Cantidad de items en el modelo servicios
    """
    #logger.info("Cantidad servicios generada correctamente")
    try:
        cantidad = Servicio.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)


@api_view(["GET"])
def reporte_servicios_extra(request):
    """
    Reporte de Servicios Extras
    """
    try:
        servicios = Servicio.objects.filter(tipo_cobro='E')
        cantidad = servicios.count()

        return JsonResponse(
            ReporteServiciosSerializer({
                "cantidad": cantidad,
                "servicios": servicios
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)
   