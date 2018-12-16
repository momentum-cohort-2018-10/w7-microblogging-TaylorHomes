from rest_framework import serializers
from core.models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ("title", "user", "body")