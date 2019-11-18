from rest_framework import serializers
from app.models import *

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode']

class ProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Profile
        fields = ['name', 'email', 'address']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        return Profile.objects.create(address=address, **validated_data)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['userId', 'title', 'body']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['postId', 'name', 'email', 'body']

class ProfilePostSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['name', 'email', 'address', 'posts']

class PostCommentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['userId', 'title', 'body', 'comments']
