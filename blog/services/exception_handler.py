# services/exception_handler.py

from rest_framework.views import exception_handler
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError, AuthenticationFailed
from django.http import Http404
from blog.services.constants import GENERAL_MESSAGES, PERMISSION_MESSAGES, AUTH_VALIDATION_MESSAGES

def custom_exception_handler(exc, context):
    # Django Http404 hatasını DRF NotFound'a çeviriyoruz:
    if isinstance(exc, Http404):
        exc = NotFound()

    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, NotFound):
            view_name = context['view'].__class__.__name__

            model_specific_messages = {
                "PostViewSet": GENERAL_MESSAGES.get("post_not_found"),
                "CommentViewSet": GENERAL_MESSAGES.get("comment_not_found"),
                "CategoryViewSet": GENERAL_MESSAGES.get("category_not_found"),
            }

            default_message = GENERAL_MESSAGES.get("default_not_found")
            response.data['detail'] = model_specific_messages.get(view_name, default_message)

        elif isinstance(exc, PermissionDenied):
            response.data['detail'] = str(exc)

        elif isinstance(exc, AuthenticationFailed):
            response.data['detail'] = AUTH_VALIDATION_MESSAGES.get("login_failed")

        elif isinstance(exc, ValidationError):
            pass

        else:
            response.data['detail'] = GENERAL_MESSAGES.get("unexpected_error")

    return response
