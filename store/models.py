from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField

# Create your models here.
class Products(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'


     MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
     ]

     #sku = models.CharField(max_length=255, primary_key=True)
     title = models.CharField(max_length=255)   #varchar(255)
     description = models.TextField()
     price =models.DecimalField(max_digits=6,decimal_places=2)
     inventory = models.IntegerField()
     last_update = models.DateTimeField(auto_now=True)
     membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Customer(models.Model):
    first_name =  models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    phone = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)

class Order(models.Model):
    PENDING = 'P'
    COMPLETE = 'C'
    FAILED = 'F'

    PAYMENT_STATUS = [
        (PENDING, 'Pending'),
        (COMPLETE, 'Complete'),
        (FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=255, choices=PAYMENT_STATUS, default=PENDING)