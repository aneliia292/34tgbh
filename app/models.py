from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Likes(models.Model):
    isLikes = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.comment} написал {self.user.username}'


class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()
    category = models.ManyToManyField('Category')
    comments = models.ManyToManyField('Comments')
    like = models.ForeignKey('Likes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title



