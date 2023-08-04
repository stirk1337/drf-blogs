from rest_framework import serializers
from .models import Blog, Author


class BlogSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    class Meta:
        model = Blog
        fields = ('title', 'description', 'category', 'authors')
