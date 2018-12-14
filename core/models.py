from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Follow(models.Model):
    following_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="follows_from")
    followed_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="follows_to")
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=255, null=True)
    voted_users = models.ManyToManyField(
        to=User, through='Vote', related_name='user_votes')
    score = models.IntegerField(default=0)


class Vote(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="vote")
    post = models.ForeignKey(
        to=Post, on_delete=models.SET_NULL, null=True, related_name="votes")
