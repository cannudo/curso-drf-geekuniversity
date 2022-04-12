'''
Um serializer pega um dado (ou uma estrutura de dados) Python
e o formata em JSON. O contrário também é verdadeiro.
'''

from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {
                'write_only': True # Só pega o e-mail na hora de gravar o registro
            }
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )


class CursoSerializer(serializers.ModelSerializer):
    '''
    Uma instância do serializer retorna os campos do model
    bem como seus respectivos tipos.
    '''
    avaliacoes = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'avaliacao-detail'
    ) # HyperLinked Related Relationships

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )