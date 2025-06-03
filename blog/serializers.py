# blog/serializers.py

from rest_framework import serializers
from .models import Post, Comment, Category
from .services.validators import validate_required_fields, validate_min_lengths, validate_required_categories
from .services.constants import POST_VALIDATION_MESSAGES, COMMENT_VALIDATION_MESSAGES
from .rules.validation_rules import POST_VALIDATION_RULES, COMMENT_VALIDATION_RULES

class AuthorFullNameField(serializers.RelatedField):
    def to_representation(self, value):
        full_name = f"{value.first_name} {value.last_name}".strip()
        return full_name if full_name else value.username

class BaseAuthorSerializer(serializers.ModelSerializer):
    author = AuthorFullNameField(read_only=True)

    class Meta:
        abstract = True

class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class PostSerializer(BaseAuthorSerializer):
    title = serializers.CharField(required=False, allow_blank=True)
    content = serializers.CharField(required=False, allow_blank=True)
    categories = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
        many=True,
        required=False
    )

    class Meta:
        model = Post
        fields = ['id','author', 'title', 'slug', 'content', 'categories', 'is_published']
        read_only_fields = ['id','author', 'slug', 'is_published', 'created_at']

    def validate(self, data):
        validate_required_fields(
            data,
            POST_VALIDATION_RULES["required_fields"],
            POST_VALIDATION_MESSAGES,
            self.instance
        )
        validate_min_lengths(
            data,
            POST_VALIDATION_RULES["min_lengths"],
            POST_VALIDATION_MESSAGES
        )
        validate_required_categories(
            data,
            POST_VALIDATION_MESSAGES,
            self.instance
        )
        return data

    def create(self, validated_data):
        categories = validated_data.pop('categories', [])
        post = Post.objects.create(**validated_data)
        post.categories.set(categories)
        return post

    def update(self, instance, validated_data):
        categories = validated_data.pop('categories', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if categories is not None:
            instance.categories.set(categories)
        return instance

class CommentSerializer(BaseAuthorSerializer):
    content = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'content', 'is_approved', 'created_at'] 
        read_only_fields = ['id', 'author', 'post', 'is_approved', 'created_at']

    def validate(self, data):
        validate_required_fields(
            data,
            COMMENT_VALIDATION_RULES["required_fields"],
            COMMENT_VALIDATION_MESSAGES,
            self.instance
        )
        validate_min_lengths(
            data,
            COMMENT_VALIDATION_RULES["min_lengths"],
            COMMENT_VALIDATION_MESSAGES
        )
        return data
