from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Audit(models.Model):
    createdAt = models.DateTimeField('createdAt', default=timezone.now)
    createdBy = models.IntegerField(default=0)
    modifiedAt = models.DateTimeField('modifiedAt', auto_now=True)
    modifiedBy = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Stock(Audit):
    stock_symbol = models.CharField(max_length=20)
    security_name = models.CharField(max_length=300)
    quantity = models.IntegerField(default=100)
    price = models.IntegerField(default=10)


class Functionality(models.TextChoices):
    BUY = 'buy'
    SELL = 'sell'
    ONGOING = 'ongoing'


class Transaction(Audit):
    Type = models.CharField(max_length=200, choices=Functionality.choices)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()


class UserProfile(Audit):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    transactions = models.ForeignKey(Transaction, on_delete=models.CASCADE)
