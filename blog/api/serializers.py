from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('created', 'updated')
