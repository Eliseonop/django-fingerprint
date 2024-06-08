# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import FingerprintModel
from .serializers import RegistroModelSerializer, FingerPrintSerializer


class FingerPrintView(ModelViewSet):
    serializer_class = FingerPrintSerializer
    queryset = FingerprintModel.objects.all()


# class PersonaControllers(ModelViewSet):
#     # sera el encargado de moldear los datos que se envian al cliente que llegan de la base de datos
#     # y formatearlos en un json
#     serializer_class = PersonaSerializer
#     queryset = PersonaModel.objects.all()
#
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#

class RegistroController(CreateAPIView):
    serializer_class = RegistroModelSerializer

    def post(self, request):
        print(request.data)
        data = self.serializer_class(data=request.data)
        print(data)
        if data.is_valid():
            nuevoUsuario = data.save()
            resultado = self.serializer_class(instance=nuevoUsuario)
            return Response({'message': 'Usuario creado exitosamente', 'usuario': resultado.data})
        else:
            return Response({'errores': data.errors})
