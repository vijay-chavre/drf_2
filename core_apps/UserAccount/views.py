from django.shortcuts import render
from rest_framework import viewsets
from .models import UserAccount
from .serializers import UserAccountSerializer

# Create your views here.


class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
