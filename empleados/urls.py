from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import EmpleadoViewSet, BeneficiarioViewSet


router_empleado = DefaultRouter()
router_empleado.register(prefix='empleados', viewset=EmpleadoViewSet)

router_beneficiario = DefaultRouter()
router_beneficiario.register(
    prefix='beneficiarios',
    viewset=BeneficiarioViewSet,
)


urlpatterns = [
    path('', include(router_empleado.urls)),
    path('', include(router_beneficiario.urls)),
]
