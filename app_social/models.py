from django.db import models
from mainapp.models import DigitalProduct
from authentication.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField()
    description = models.TextField()
    suggest = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    point = models.ForeignKey('Point' , on_delete=models.CASCADE)
    isuseful = models.ForeignKey('IsUseful' , on_delete=models.CASCADE)

class Point(models.Model):
    type = models.CharField(max_length=255)
    description = models.TextField()

class IsUseful(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_useful = models.BooleanField()

class Category(models.Model):
    field = models.CharField(max_length=255)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
