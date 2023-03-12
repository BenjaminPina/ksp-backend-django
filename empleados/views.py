from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import filters, status
from django_filters.rest_framework import DjangoFilterBackend

from .models import Empleado, Beneficiario
from .serializers import EmpleadoSerializer, BeneficiarioSerializer


class EmpleadoViewSet(ModelViewSet):
    queryset = Empleado.objects.filter(estatus=True).all()
    serializer_class = EmpleadoSerializer
    search_fields = ['nombre_completo']
    ordering_fields = ['nombre_completo']
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]

    def destroy(self, request, *args, **kwargs):
        """
        Se sobreescribe el método para evitar el eliminado físico e
        implementar el eliminado lógico.
        """
        instance: Empleado = self.get_object()
        instance.estatus = False
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class BeneficiarioViewSet(ModelViewSet):
    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer
    search_fields = ['nombre_completo']
    ordering_fields = ['nombre_completo']
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
