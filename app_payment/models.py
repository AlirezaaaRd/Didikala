from django.db import models
from django.contrib.auth import get_user_model
from mainapp.models import DigitalProduct

User = get_user_model()

Transaction_choices= (
    (False , 'Failed'),
    (True , 'Success'),
)

class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    transaction = models.OneToOneField('Transaction' , on_delete=models.CASCADE)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(DigitalProduct, on_delete=models.CASCADE)
    count = models.IntegerField()

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(DigitalProduct, on_delete=models.CASCADE)
    count = models.IntegerField()

class Transaction(models.Model):
    status = models.BooleanField(default=False , choices= Transaction_choices)
    ref_code = models.CharField(max_length=255)
    price = models.IntegerField()
# Create your models here.
