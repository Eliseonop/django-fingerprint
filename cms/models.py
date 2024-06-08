from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from cms.auth_manager import UsuarioManager


# Create your models here.

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    TIPO_USUARIO = [
        (1, 'ADMIN'),
        (2, 'CLIENTE'),
        (3, 'EMPLEADO'),
    ]

    usuario_id = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='id')
    usuario_nombre = models.CharField(
        max_length=50,
        null=False,
        db_column='nombre',
    )
    usuario_correo = models.EmailField(
        unique=True,
        null=False,
        db_column='correo',
        verbose_name='Correo'
    )

    usuario_tipo = models.IntegerField(
        choices=TIPO_USUARIO,
        default=2,
        db_column='tipo')

    password = models.TextField()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'usuario_correo'

    REQUIRED_FIELDS = ['usuario_nombre', 'usuario_tipo']

    class Meta:
        db_table = 'usuarios'


# class PersonaModel(models.Model):
#     persona_id = models.AutoField(
#         primary_key=True,
#         unique=True,
#         db_column='id')
#     nombre = models.CharField(
#         max_length=50,
#         null=False,
#         db_column='nombre',
#     )
#     apellido = models.CharField(
#         max_length=50,
#         unique=False,
#         db_column='apellido')
#     correo = models.EmailField(
#         unique=True,
#         null=False,
#         db_column='correo')
#     nacimiento = models.DateField(
#         null=False,
#         db_column='nacimiento')
#
#     class Meta:
#         db_table = 'personas'
#         # unique_together = [['nombre', 'apellido']]
#         # unique_together  se utiliza para que no se repitan los valores de los campos especificados en la lista
#
#
# class VehiculoModel(models.Model):
#     vehiculo_id = models.AutoField(
#         primary_key=True,
#         unique=True,
#         db_column='id')
#     marca = models.CharField(
#         max_length=50,
#         null=False,
#         db_column='marca',
#     )
#     modelo = models.CharField(
#         max_length=50,
#         unique=False,
#         db_column='modelo')
#     anio = models.IntegerField(
#         null=False,
#         db_column='anio')
#     placa = models.CharField(
#         max_length=10,
#         null=False,
#         unique=True,
#         db_column='placa')
#     color = models.CharField(
#         max_length=20,
#         null=False,
#         db_column='color')
#     vehiculo_foto = models.ImageField(
#         null=True,
#         upload_to='vehiculos/',
#         db_column='foto')
#     persona = models.ForeignKey(
#         PersonaModel,
#         on_delete=models.CASCADE,
#         db_column='persona_id',
#     )
#
#     class Meta:
#         db_table = 'vehiculos'
#         unique_together = [['placa', 'anio']]
#         ordering = ['-anio']


class FingerprintModel(models.Model):
    id = models.AutoField(unique=True,
                          primary_key=True,
                          db_column='id')
    empleado = models.IntegerField(
        unique=True,
        db_column='empleado')
    template = models.TextField()

    class Meta:
        db_table = 'huellas'
        unique_together = [['id', 'empleado']]
