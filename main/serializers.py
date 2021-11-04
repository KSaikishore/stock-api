from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import UserProfile, Stock, Transaction


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['stock_symbol', 'security_name']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        exclude = ('createdBy', 'createdAt', 'modifiedBy', 'modifiedAt',)


class UserProfileSerializer(serializers.ModelSerializer):
    transactions_set = TransactionSerializer(read_only=True, many=True)

    class Meta:
        model = UserProfile
        exclude = ('createdBy', 'createdAt', 'modifiedBy', 'modifiedAt',)
