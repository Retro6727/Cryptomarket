from rest_framework import serializers
from .models import CryptoConversion

class CryptConversionSerializer(serializers.Serializer):
    class Meta:
        model = CryptoConversion
        fields = ['id', 'amount', 'from_currency', 'to_currency', 'converted_amount']