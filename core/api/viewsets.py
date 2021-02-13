from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

# ViewSets define the view behavior.
class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter,]
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ['nome', 'descricao']
    #lookup_field = 'nome'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao',None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(name__iexact=nome)

        if descricao:
            queryset = queryset.filter(name__iexact=descricao)
        return queryset

    def list(self, request, *args, **kwargs): # Sobrecrevendo get
        return super(PontoTuristicoViewSet,self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):# Sobrecrevendo Post
        return super(PontoTuristicoViewSet,self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):# Sobrecrevendo Delete
        return super(PontoTuristicoViewSet,self).destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):# Sobrecrevendo Put
        return super(PontoTuristicoViewSet,self).update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):# Sobrecrevendo log
        return super(PontoTuristicoViewSet,self).retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):# Sobrecrevendo path
        return super(PontoTuristicoViewSet,self).partial_update(request, *args, **kwargs)

        
    @action(methods=['get',""], detail=True)
    def denunciar(self,request, pk=None):
        pass