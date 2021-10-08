from django.db.models import fields
from rest_framework import serializers
from DjangoApp.models import Shop, Item


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('ShopId', 'ShopName', 'ShopOwner', 'ShopDescription', 'ShopLocation', 'ShopType')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('ItemId', 'ShopId', 'ItemName', 'ItemDescription', 'ItemPrice', 'ItemType')