from rest_framework import generics
from rest_framework import viewsets

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

'''
API V1
'''
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id = self.kwargs.get('curso_pk'))

        return self.queryset.all()
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'): # Se vinher um pk de curso na URL, então:
            return generics.get_object_or_404(
                self.get_queryset(),
                curso_id = self.kwargs.get('curso_pk'),
                pk = self.kwargs.get('avaliacao_pk')
            )

        return generics.get_object_or_404(self.get_queryset(), pk = self.kwargs.get('avaliacao_pk'))

'''
API V2
'''

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer