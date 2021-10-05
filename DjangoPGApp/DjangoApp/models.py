from django.db import models

# Create your models here.

class Item(models.Model):
    ItemId = models.AutoField(primary_key=True)
    ShopId = models.IntegerField()
    ItemName = models.CharField(max_length=60)
    ItemDescription = models.CharField(max_length=500)
    ItemPrice = models.IntegerField()
    ItemStock = models.IntegerField()
    ItemType = models.CharField(max_length=10)

class Shop(models.Model):
    ShopId = models.AutoField(primary_key=True)
    ShopName = models.CharField(max_length=20)
    ShopOwner = models.CharField(max_length=20)
    ShopDescription = models.CharField(max_length=500)
    ShopLocation = models.CharField(max_length=20)
    ShopType = models.CharField(max_length=10)