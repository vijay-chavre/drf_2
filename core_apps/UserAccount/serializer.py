from django.urls import path, include
from rest_framework import serializers
from core_apps.UserAccount.models import UserAccount


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True}
        }  # Prevent password from being included in responses

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)  # Hash the password
        instance.save()
        return instance
