from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from clientes.serializers import ClienteSerializer
from clientes.models import Cliente


class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']
