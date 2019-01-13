from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
from clients.models import Client
from clients.serializers import ClientSerializer, ClientCreateSerializer

class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientListView(ListAPIView):
    """
    API endpoint that lists clients.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientCreateView(CreateAPIView):
    """
    API endpoint that creates clients.
    """

    queryset = Client.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = ClientCreateSerializer

class ClientDetailView(RetrieveUpdateDestroyAPIView):
    """
    API endpoint that views a specific client's details.
    """

    queryset = Client.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = ClientSerializer
    lookup_field = 'uuid'
