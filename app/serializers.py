from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'email']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode']

class ProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Profile
        fields = ['pk','name', 'email', 'address']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        user_created = User.objects.create_user(username=validated_data['name'].split()[0],
                                                email=validated_data['email'],
                                                password='123456')
        address = Address.objects.create(**address_data)
        return Profile.objects.create(address=address, user=user_created, **validated_data)

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address = instance.address
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        address.street = address_data.get('street', address.street)
        address.suite = address_data.get('suite', address.suite)
        address.city = address_data.get('city', address.city)
        address.zipcode = address_data.get('zipcode', address.zipcode)
        instance.save()
        address.save()
        return instance

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['pk', 'userId', 'title', 'body']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'postId', 'name', 'email', 'body']

class ProfilePostSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['pk','name', 'email', 'address', 'posts']

class PostCommentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['userId', 'title', 'body', 'comments']
