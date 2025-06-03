# blog/permissions.py

from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from blog.services.constants import PERMISSION_MESSAGES

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Post ve Comment objeleri üzerinde çalışırken kullanılıyor.
    Yalnızca objenin sahibi düzenleme ve silme işlemi yapabilir.
    (object-level) izin kontrolünde kullanılıyor
    Sadece update/delete işlemlerinde devreye girer. Get isteği için h

    """
    message = PERMISSION_MESSAGES["author_only"]

    def has_object_permission(self, request, view, obj):
        # Okuma izinlerine (GET, HEAD, OPTIONS) her kullanıcı erişebilir
        if request.method in permissions.SAFE_METHODS:
            return True
        # Diğer tüm işlemler için sadece objenin sahibi izinlidir
        return obj.author == request.user

class CustomIsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Post ve Comment gibi içeriklerin oluşturulması, güncellenmesi, silinmesi için kimlik doğrulama zorunlu.
    Okuma işlemleri (GET, HEAD, OPTIONS için giriş gerekmez.
    ViewSet'in tümünde uygulanıyor.
    Sadece yazma işlemleri (POST, PUT, PATCH, DELETE) için login kontrolü yapıyor.

    """
    message = PERMISSION_MESSAGES["authentication_required"]

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user or not request.user.is_authenticated:
            raise PermissionDenied(self.message)
        return True

class StrictIsAuthenticated(permissions.BasePermission):
    """
    GET dahil http istekleri için kimlik doğrulama zorunlu. (Comment için)
    """
    message = PERMISSION_MESSAGES["authentication_required"]

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            raise PermissionDenied(self.message)
        return True