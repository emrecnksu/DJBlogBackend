# blog/services/handlers.py

from rest_framework import status
from rest_framework.authtoken.models import Token
from .responses import success_response, error_response

def handle_create(view, request, success_msg, error_msg):
    serializer = view.get_serializer(data=request.data)
    if not serializer.is_valid():
        return error_response(
            errors=serializer.errors,
            message=error_msg,
            status_code=status.HTTP_400_BAD_REQUEST
        )
    view.perform_create(serializer)
    return success_response(
        data=serializer.data,
        message=success_msg,
        status_code=status.HTTP_201_CREATED
    )

def handle_update(view, request, success_msg, error_msg, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = view.get_object()
    serializer = view.get_serializer(instance, data=request.data, partial=partial)
    if not serializer.is_valid():
        return error_response(
            errors=serializer.errors,
            message=error_msg,
            status_code=status.HTTP_400_BAD_REQUEST
        )
    view.perform_update(serializer)
    return success_response(data=serializer.data, message=success_msg)

def handle_delete(view, success_msg, *args, **kwargs):
    instance = view.get_object()
    view.perform_destroy(instance)
    return success_response(message=success_msg)

def handle_register(serializer_class, request, success_msg, error_msg):
    serializer = serializer_class(data=request.data)
    if not serializer.is_valid():
        return error_response(
            errors=serializer.errors,
            message=error_msg,
            status_code=status.HTTP_400_BAD_REQUEST
        )
    user = serializer.save()
    token, _ = Token.objects.get_or_create(user=user)
    return success_response(
        data={"token": token.key},
        message=success_msg,
        status_code=status.HTTP_201_CREATED
    )

def handle_login(serializer_class, request, success_msg, error_msg):
    serializer = serializer_class(data=request.data)
    if not serializer.is_valid():
        return error_response(
            errors=serializer.errors,
            message=error_msg,
            status_code=status.HTTP_400_BAD_REQUEST
        )
    user = serializer.validated_data["user"]
    token, _ = Token.objects.get_or_create(user=user)
    return success_response(
        data={"token": token.key},
        message=success_msg
    )

def handle_logout(request, success_msg):
    request.user.auth_token.delete()
    return success_response(message=success_msg)
