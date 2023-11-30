from .models import Buyer, Seller, Transaction
from rest_framework import serializers


class BuyerSerializer(serializers.Serializer):

    class Meta:
        model = Buyer
        fields = ('__all__')


class SellerSerializer(serializers.Serializer):

    class Meta:
        model = Seller
        fields = ('__all__')


class TransactionSerializer(serializers.Serializer):

    class Meta:
        model = Transaction
        fields = ('__all__')
