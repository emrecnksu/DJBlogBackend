# auth/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from ..services.validators import (
    validate_required_fields,
    validate_min_lengths,
    validate_unique_fields,
    validate_login_credentials
)
from ..services.constants import AUTH_VALIDATION_MESSAGES
from ..rules.validation_rules import AUTH_VALIDATION_RULES

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(required=False, allow_blank=True, write_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def validate(self, data):
        validate_required_fields(
            data, 
            AUTH_VALIDATION_RULES["register_required_fields"], 
            AUTH_VALIDATION_MESSAGES
        )
        validate_min_lengths(
            data, 
            AUTH_VALIDATION_RULES["min_lengths"], 
            AUTH_VALIDATION_MESSAGES
        )
        validate_unique_fields(
            data, 
            AUTH_VALIDATION_RULES["unique_fields"], 
            AUTH_VALIDATION_MESSAGES
        )
        return data


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    def validate(self, data):
        validate_required_fields(
            data, 
            AUTH_VALIDATION_RULES["login_required_fields"], 
            AUTH_VALIDATION_MESSAGES
        )
        user = validate_login_credentials(data["username"], data["password"], AUTH_VALIDATION_MESSAGES)
        return {**data, "user": user}

