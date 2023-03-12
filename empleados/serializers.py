from rest_framework import serializers

from .models import Empleado, Beneficiario


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = [
            'nombre_completo',
            'puesto_trabajo',
            'salario',
            'fecha_contratacion',
            'estatus',
            'foto',
        ]
