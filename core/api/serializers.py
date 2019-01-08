from rest_framework.serializers import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    descricao_completa = SerializerMethodField()
    endereco = EnderecoSerializer()


    def get_descricao_completa(self, obj):
        return '{} - {}'.format(obj.nome, obj.descricao)

    class Meta:
        model = PontoTuristico
        fields = (
            'id',
            'nome',
            'descricao',
            'fotos',
            'atracoes',
            'comentarios',
            'avaliacoes',
            'endereco',
            'descricao_completa'
        )
