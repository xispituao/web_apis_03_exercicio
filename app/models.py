from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    def __str__(self):
        return self.street

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.OneToOneField(Address, models.CASCADE, related_name='address')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    userId = models.ForeignKey(Profile, models.CASCADE, related_name='posts')

    def __str__(self):
        return self.body

class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    postId = models.ForeignKey(Post, models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name
