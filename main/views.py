from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response

from main.serializers import UserSerializer, UserProfileSerializer, TransactionSerializer
from main.models import UserProfile, Stock
from rest_framework.generics import CreateAPIView, ListAPIView
import json
import requests


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfiler(ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.  
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # f = open('main/stocks.json')
        # data = json.load(f)
        # for i in data:
        #     print("stocks symbol and name: ",i["Stock Symbol"],i["Security Name"])
        #     stock=Stock(stock_symbol=i["Stock Symbol"],security_name=i["Security Name"])
        #     stock.save()
        return UserProfile.objects.filter(user=self.request.user)


class Buy(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = TransactionSerializer
    http_method_names = ['post', ]

    def post(self, request):
        return Response(({"result": "mission.status"}), status.HTTP_200_OK)


class Sell(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = TransactionSerializer
    http_method_names = ['post', ]

    def post(self, request):
        return Response(({"result": "mission.status"}), status.HTTP_200_OK)
