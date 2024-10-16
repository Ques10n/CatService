from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Cat

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['name', 'age','breed','hair_type','id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user