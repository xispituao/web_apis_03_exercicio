from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.ForeignKey(Address, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE, related_name="profile")

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    userId = models.ForeignKey(Profile, models.CASCADE, related_name='posts')

class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    postId = models.ForeignKey(Post, models.CASCADE, related_name='comments')
