from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from .models import UserAccount
from .serializers import UserAccountSerializer, ChangePasswordSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


# Create your views here.

@extend_schema(tags=["User Management"])
class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]  # open for registration
        return [permissions.IsAuthenticated()]  # rest require auth


@extend_schema(tags=["Password"])
class ChangePasswordView(generics.UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)
