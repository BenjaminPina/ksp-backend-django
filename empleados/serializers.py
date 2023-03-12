from rest_framework import serializers

from .models import Empleado, Beneficiario


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = [
            'id',
            'nombre_completo',
            'puesto_trabajo',
            'salario',
            'fecha_contratacion',
            'estatus',
            'foto',
        ]
        read_only_fields = ['id']


class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = [
            'empleado',
            'nombre_completo',
            'parentesco',
            'fecha_nacimiento',
            'sexo',
        ]
