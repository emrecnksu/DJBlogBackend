# blog/auth/views.py

from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import UserRegisterSerializer, LoginSerializer
from ..services.handlers import handle_register, handle_login, handle_logout
from ..services.constants import SUCCESS_MESSAGES, ERROR_MESSAGES, AUTH_VALIDATION_MESSAGES

class AuthViewSet(viewsets.ViewSet):

    @action(detail=False, methods=["post"])
    def register(self, request):
        return handle_register(
            serializer_class=UserRegisterSerializer,
            request=request,
            success_msg=SUCCESS_MESSAGES["registered"],
            error_msg=ERROR_MESSAGES["register_failed"]
        )

    @action(detail=False, methods=["post"])
    def login(self, request):
        return handle_login(
            serializer_class=LoginSerializer,
            request=request,
            success_msg=SUCCESS_MESSAGES["logged_in"],
            error_msg=AUTH_VALIDATION_MESSAGES["login_failed"]
        )

    @action(detail=False, methods=["post"])
    def logout(self, request):
        return handle_logout(
            request=request,
            success_msg=SUCCESS_MESSAGES["logged_out"]
        )
