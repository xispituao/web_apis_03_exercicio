from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.reverse import reverse

class ImportJson(APIView):
    def post(self, request, format=None):
        profiles = request.data['users']
        posts = request.data['posts']
        comments = request.data['comments']

        for profile in profiles:
            profile_serializer = ProfileSerializer(data=profile)
            if profile_serializer.is_valid():
                profile_serializer.save()

        for post in posts:
            post_serializer = PostSerializer(data=post)
            if post_serializer.is_valid():
                post_serializer.save()

        for comment in comments:
            comment_serializer = CommentSerializer(data=comment)
            if comment_serializer.is_valid():
                comment_serializer.save()

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'

class ProfilePostList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-list'

class ProfilePostDetail(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-detail'

class PostCommentList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    name = 'post-comment-list'

class PostCommentDetail(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    name = 'post-comment-detail'

class ApiRoot(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'profile': reverse(ProfileList.name, request=request),
            'profile-posts': reverse(ProfilePostList.name, request=request),
            'posts-comments': reverse(PostCommentList.name, request=request)
        })
