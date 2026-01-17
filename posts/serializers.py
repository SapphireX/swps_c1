from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Topic, Post


class TopicSerializer(serializers.Serializer):
    """
    Serializer dla modelu Topic dziedziczący po serializers.Serializer.
    Wymaga ręcznej implementacji metod create() i update().
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=60)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Tworzy i zwraca nową instancję Topic na podstawie zwalidowanych danych.
        """
        return Topic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Aktualizuje i zwraca istniejącą instancję Topic.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer dla modelu Category dziedziczący po ModelSerializer.
    ModelSerializer automatycznie generuje pola na podstawie modelu.
    """
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer dla modelu Post dziedziczący po ModelSerializer.
    Pola created_at i updated_at są tylko do odczytu.
    Pole created_by jest nullable (zgodnie z definicją w modelu).
    """
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'topic', 'slug', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['id', 'created_at', 'updated_at']
