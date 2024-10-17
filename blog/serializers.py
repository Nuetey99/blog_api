from rest_framework import serializers
from .models import Post, Category, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'category', 'tags', 'published_date', 'created_at']
