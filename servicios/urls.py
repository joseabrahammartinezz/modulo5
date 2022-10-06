from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"servicios", views.ServicioViewSet)
router.register(r"tarifas", views.TarifaViewSet)
router.register(r"socios", views.SocioViewSet)
router.register(r"socioServicio", views.SocioServicioViewSet)

urlpatterns = [
    #path('contacto/<str:nombre>', views.contacto, name='contacto'),
   # path('', views.index, name='index'),
    #path('servicios/', views.servicio, name='servicios'),
    #path('tarifas/', views.tarifa, name='tarifas'),
    #path('socios/', views.socio, name='socios'),
    #path('ver_socios/', views.socioFormView, name='ver_socios'),
    #path('socioServicio/socios_servicio', views.socios_servicio, name='socios_servicio'),
    path('servicios/reporte_extras', views.reporte_servicios_extra),
    path('servicios/create_list', views.ServicioCreateAndList.as_view()),
    path('servicios/cantidad', views.servicios_contador),
    path('', include(router.urls)),
]
