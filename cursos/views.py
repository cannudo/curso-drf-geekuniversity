from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

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

    @action(detail = True, methods = ['get']) # Cria uma nova rota
    def avaliacoes(self, request, pk = None): # View da nova rota
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(),
                                        many = True) #        1N relationship
                                                     # Curso tem uma lista de avaliações
        return Response(serializer.data) # Response() -> Binary string (content-type do 
                                         #               request header determina o for)
                                         #               mato da response


class AvaliacaoViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    Não retorna lista, apenas instâncias singulares
    '''
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
