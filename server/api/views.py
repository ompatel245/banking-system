from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from bank.models import users, BankDetails
from .serializers import UserSerializer, BankDetailsSerializer, UserRegistrationSerializer

# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = users.objects.all()
    serializer_class = UserSerializer

class BankDetailsViewSet(ModelViewSet):
    queryset = BankDetails.objects.all()
    serializer_class = BankDetailsSerializer