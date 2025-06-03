# services/validators.py

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def validate_required_fields(data, required_fields, messages, instance=None):
    errors = {}
    for field in required_fields:
        value = data.get(field) if data.get(field) is not None else getattr(instance, field, None)
        if not value or not str(value).strip():
            errors[field] = messages.get(f"{field}_required")
    if errors:
        raise serializers.ValidationError(errors)
    return data

def validate_min_lengths(data, min_lengths, messages):
    errors = {}
    for field, min_length in min_lengths.items():
        value = data.get(field, "")
        if value and len(value.strip()) < min_length:
            errors[field] = messages.get(f"{field}_min")
    if errors:
        raise serializers.ValidationError(errors)
    return data

def validate_required_categories(data, messages, instance=None):
    categories = data.get('categories') if data.get('categories') is not None else getattr(instance, 'categories', None)
    if not categories or (hasattr(categories, '__len__') and len(categories) == 0):
        raise serializers.ValidationError({"categories": messages.get("categories_required")})

def validate_unique_fields(data, unique_fields, messages):
    errors = {}
    for field in unique_fields:
        value = data.get(field, "").strip()
        if value:
            if field == "username" and User.objects.filter(username=value).exists():
                errors[field] = messages.get("username_exists")
            if field == "email" and User.objects.filter(email=value).exists():
                errors[field] = messages.get("email_exists")
    if errors:
        raise serializers.ValidationError(errors)
    return data

def validate_login_credentials(username, password, messages):
    username = username.strip()
    password = password.strip()

    errors = {}
    if not username:
        errors["username"] = messages.get("username_required")
    if not password:
        errors["password"] = messages.get("password_required")

    if errors:
        raise serializers.ValidationError(errors)

    user = authenticate(username=username, password=password)
    if not user:
        raise serializers.ValidationError({"detail": messages.get("login_invalid")})

    return user
