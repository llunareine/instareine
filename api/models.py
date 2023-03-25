from django.db import models
from django.contrib.auth.models import User
class User(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_account')
    username = models.CharField(max_length=100, unique=True)
    password = models.TextField()
    email = models.CharField(max_length=100, unique=True)
    avatar = models.ImageField
    # avatar = models.ImageField(upload_to='avatars/')
    description = models.TextField()
    title = models.TextField()
    subscribers = models.IntegerField
    followers = models.IntegerField
    # subscribers = models.IntegerField()
    # followers = models.IntegerField()
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Posts(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.IntegerField
    media_type = models.FileField

    def __str__(self):
        return f'{type(self).__name__}({self.text!r}, {self.likes!r})'


class Comments(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.IntegerField

    def __str__(self):
        return self.text

class Stories(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    stories_media = models.FileField
    time = models.TimeField
    likes = models.IntegerField

    def __str__(self):
        return self.time

class Likes(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    stories = models.ForeignKey('Stories', on_delete=models.CASCADE)
