# from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter, )
    # permission_classes = (IsAdminUser, )
    # authentication_classes = (TokenAuthentication, )
    search_fields = ('nome', 'descricao')

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('nome', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if descricao:
            queryset = queryset.filter(descricao=descricao)

        return queryset

    # com o action voce pode escolher uma ação para usar em uma determinado endpoint
    # precisa ser importado de rest_framework.decorators import action
    # em methods apenas escolhas os methods get, post, delete, path, put ...
    # se for para usar no endpont completo, apenas coloque detail=False, e não precisa passar pk

    # @action(methods=['get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     pass