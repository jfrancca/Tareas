from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}} # No mostrar la clave al responder

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)