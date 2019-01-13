from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
from dealers.models import Dealer
from dealers.serializers import DealerSerializer

class DealerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows dealers to be viewed or edited.
    """

    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer

class DealerListView(ListAPIView):
    """
    API endpoint that lists dealers.
    """

    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer

class DealerCreateView(CreateAPIView):
    """
    API endpoint that creates dealers.
    """

    queryset = Dealer.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = DealerSerializer

class DealerDetailView(RetrieveUpdateDestroyAPIView):
    """
    API endpoint that views a specific dealer's details.
    """

    queryset = Dealer.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = DealerSerializer
    lookup_field = 'uuid'
