from dealers.models import Dealer
from rest_framework import serializers


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ('uuid','name', 'address', 'phone_number', 'email')
