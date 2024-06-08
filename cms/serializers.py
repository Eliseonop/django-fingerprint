from rest_framework import serializers

from .models import UsuarioModel, FingerprintModel


# class PersonaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PersonaModel
#         fields = '__all__'


class RegistroSerializer(serializers.Serializer):
    email = serializers.EmailField()
    nombre = serializers.CharField(max_length=10)


class RegistroModelSerializer(serializers.Serializer):
    def save(self):
        usuarioNombre = self.validated_data.get('usuarioNombre')
        usuarioCorreo = self.validated_data.get('usuarioCorreo')
        usuarioTipo = self.validated_data.get('usuarioTipo')
        password = self.validated_data.get('password')
        is_superuser = self.validated_data.get('is_superuser')

        nuevoUsuario = UsuarioModel(usuarioNombre=usuarioNombre,
                                    usuarioCorreo=usuarioCorreo,
                                    usuarioTipo=usuarioTipo,
                                    is_superuser=is_superuser)

        nuevoUsuario.set_password(password)
        nuevoUsuario.save()
        return nuevoUsuario

    class Meta:
        model = UsuarioModel
        exclude = ['user_permissions',
                   'is_staff', 'groups', 'last_login', 'is_active']


class FingerPrintSerializer(serializers.ModelSerializer):
    # empleado = serializers.IntegerField()
    # template = serializers.CharField(max_length=1000000)

    class Meta:
        model = FingerprintModel
        fields = '__all__'

    # def save(self):
    #     template = self.validated_data.get('template')
    #     empleado = self.validated_data.get('empleado')
    #
    #     nuevoFingerprint = FingerprintModel(template=template, empleado=empleado)
    #     nuevoFingerprint.save()
    #     return nuevoFingerprint
