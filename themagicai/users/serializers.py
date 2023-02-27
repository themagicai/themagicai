from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email"
        ]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "email"}
        }


class UserOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "name",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class GetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class LogOutSerializer(serializers.Serializer):
    refresh = serializers.CharField(max_length=255)
