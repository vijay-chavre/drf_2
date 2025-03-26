from rest_framework import viewsets, filters

from core_apps.UserAccount.models import UserAccount

from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
