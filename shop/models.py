from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
