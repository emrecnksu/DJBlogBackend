#blog/views.py

from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import Category, Post, Comment
from .serializers import CategorySerializer, PostSerializer, CommentSerializer
from .permissions import StrictIsAuthenticated, IsAuthorOrReadOnly, CustomIsAuthenticatedOrReadOnly
from .services.constants import SUCCESS_MESSAGES, ERROR_MESSAGES, GENERAL_MESSAGES
from .services.handlers import handle_create, handle_update, handle_delete

class BaseOwnerViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomIsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class PostViewSet(BaseOwnerViewSet):
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def perform_destroy(self, instance):
        raise PermissionDenied(GENERAL_MESSAGES["post_delete_not_allowed"])

    def create(self, request, *args, **kwargs):
        return handle_create(self, request, SUCCESS_MESSAGES["post_created"], ERROR_MESSAGES["post_create_failed"])

    def update(self, request, *args, **kwargs):
        return handle_update(self, request, SUCCESS_MESSAGES["post_updated"], ERROR_MESSAGES["post_update_failed"], *args, **kwargs)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [StrictIsAuthenticated, IsAuthorOrReadOnly]

    def get_post(self):
        post_slug = self.kwargs.get('post_slug')
        return get_object_or_404(Post, slug=post_slug, is_published=True)

    def get_queryset(self):
        post = self.get_post()
        return Comment.objects.filter(post=post)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, email=self.request.user.email, post=post, is_approved=True)

    def create(self, request, *args, **kwargs):
        return handle_create(self, request, SUCCESS_MESSAGES["comment_created"], ERROR_MESSAGES["comment_create_failed"])

    def update(self, request, *args, **kwargs):
        return handle_update(self, request, SUCCESS_MESSAGES["comment_updated"], ERROR_MESSAGES["comment_update_failed"], *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return handle_delete(self, SUCCESS_MESSAGES["comment_deleted"])

