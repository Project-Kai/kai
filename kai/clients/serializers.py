from clients.models import Client
from rest_framework import serializers

from dealers.models import Dealer
from dealers.serializers import DealerSerializer

class DealerField(serializers.RelatedField):

    def to_representation(self, value):
        return value

    def to_internal_value(self, value):
        return value

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('uuid', 'name', 'address', 'phone_number', 'email', 'dealer')
        

class ClientCreateSerializer(serializers.ModelSerializer):
    dealer = DealerField(queryset=Dealer.objects.values_list('name', flat=True))

    class Meta:
        model = Client
        fields = ('uuid','name', 'address', 'phone_number', 'email', 'dealer')

    def create(self, validated_data):
        dealer = Dealer.objects.get(name=validated_data.pop('dealer_name'))

        client = Client.objects.create(dealer=dealer, **validated_data)

        return client
