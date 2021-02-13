from rest_framework.fields import SerializerMethodField
from comentarios.api.serializers import ComentarioSerializer
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from localizacao.api.serializers import LocalizacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    localizacao = LocalizacaoSerializer()
    comentario = ComentarioSerializer(many=True)
    avaliacao = AvaliacaoSerializer (many=True)

    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id','nome','descricao',
        'aprovado','foto','atracoes',
        'comentario','avaliacao','localizacao','descricao_completa','descricao_completa2']

    def get_descricao_completa(self,obj):
        return '%s - %s' % (obj.nome, obj.descricao)
