from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude = ('created', 'updated')
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('created', 'updated')
        # fields = "__all__"
