# Generated by Django 4.1.7 on 2023-03-11 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos/')),
                ('nombre_completo', models.CharField(max_length=255)),
                ('puesto_trabajo', models.CharField(max_length=120, verbose_name='Puesto de trabajo')),
                ('salario', models.FloatField(default=0.0)),
                ('estatus', models.BooleanField(default=True)),
                ('fecha_contratación', models.DateField(verbose_name='Fecha de contratación')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='empleados.empleado')),
                ('nombre_completo', models.CharField(blank=True, max_length=255)),
                ('parentesco', models.CharField(blank=True, max_length=120)),
                ('fecha_nacimiento', models.DateField(blank=True, verbose_name='Fecha de nacimiento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
