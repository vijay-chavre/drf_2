from rest_framework import serializers
from core_apps.UserAccount.models import UserAccount, Books


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
        representation["full_name"] = f"{
            instance.first_name} {instance.last_name}"
        return representation


class BookSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserAccount.objects.all(), write_only=True)
    user_details = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Books
        fields = ["id", "title", "author", "description", "publication_date",
                  "isbn", "price", "cover_image", "user", "user_details"]
