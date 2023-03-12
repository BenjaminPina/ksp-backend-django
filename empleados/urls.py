from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import EmpleadoViewSet


router_empleado = DefaultRouter()
router_empleado.register(prefix='empleados', viewset=EmpleadoViewSet)


urlpatterns = [
    path('', include(router_empleado.urls)),
]
