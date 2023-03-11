from django.db import models


class Empleado(models.Model):
    foto = models.ImageField(blank=True, null=True, upload_to='fotos/')
    nombre_completo = models.CharField(max_length=255)
    puesto_trabajo = models.CharField(
        max_length=120,
        verbose_name='Puesto de trabajo',
    )
    salario = models.FloatField(default=0.0)
    estatus = models.BooleanField(default=True)
    fecha_contratación = models.DateField(verbose_name='Fecha de contratación')
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)


class Beneficiario(models.Model):
    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    empleado = models.OneToOneField(
        Empleado,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    nombre_completo = models.CharField(max_length=255, blank=True)
    parentesco = models.CharField(max_length=120, blank=True)
    fecha_nacimiento = models.DateField(
        verbose_name='Fecha de nacimiento',
        blank=True
    )
    sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
