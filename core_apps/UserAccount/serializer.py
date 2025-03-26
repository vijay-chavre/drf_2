from rest_framework import serializers
from core_apps.UserAccount.models import UserAccount


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["id", "email", "first_name", "last_name", "username"]
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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["full_name"] = (
            f"{
            instance.first_name} {instance.last_name}"
        )
        return representation


class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["id", "email", "first_name", "last_name", "username"]
