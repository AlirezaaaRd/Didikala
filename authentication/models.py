from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    national_code = models.CharField(max_length=10, null=True)
    card_no = models.CharField(max_length=16 , null=True)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)  # Removed default value
    phone_number = models.CharField(max_length=15, null=True)  # Removed default value
    state = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
