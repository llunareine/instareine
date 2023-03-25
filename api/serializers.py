from rest_framework import serializers
from django.contrib.auth import authenticate
from . import models

#
# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
#
#     class Meta:
#         model = models.User
#         fields = ('email', 'username', 'password')
#
#     def create(self, validated_data):
#         user = models.User.objects.create_user(
#             email=validated_data['email'],
#             username=validated_data['username'],
#             password=validated_data['password']
#         )
#         return user
#
#     def validate(self, data):
#         user = authenticate(email=data['email'], password=data['password'])
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Unable to login with provided credentials.")


from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import User
from rest_framework import serializers

from .models import Posts

import json
from django.db.models.fields.files import FieldFile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'user', 'text')

        def create(self, validated_data):
            post = Posts.objects.create_post(**validated_data)
            return post

    # class Meta:
    #     model = Posts
    #     fields = ['id', 'user', 'text', 'likes', 'media_type']
    #
    # media_type = serializers.SerializerMethodField()
    #
    # def get_media_type(self, obj):
    #     if obj.media_type:
    #         return obj.media_type.url
    #     return None

    # media_type_url = serializers.SerializerMethodField()

    # class Meta:
    #     model = Posts
    #     fields = ['id', 'user', 'text', 'likes', 'media_type', 'media_type_url']

    # def get_media_type_url(self, obj):
    #     if obj.media_type:
    #         return obj.media_type.url
    #     return None