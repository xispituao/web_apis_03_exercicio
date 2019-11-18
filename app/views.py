from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class FileLoad(APIView):
    def post(self, request, format=None):
        profiles = request.data['users']
        posts = request.data['posts']
        comments = request.data['comments']

        for profile in profiles:
            profile_s = ProfileSerializer(data=profile)
            if profile_s.is_valid():
                profile_s.save()

        for post in posts:
            post_s = PostSerializer(data=post)
            if post_s.is_valid():
                post_s.save()

        for comment in comments:
            comment_s = CommentSerializer(data=comment)
            if comment_s.is_valid():
                comment_s.save()
