from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from DjangoApp.models import Shop, Item
from DjangoApp.serializers import ShopSerializer, ItemSerializer


# Create your views here.

@csrf_exempt
def shopAPI(request, id=0):
    if request.method == 'GET':
        shops = Shop.objects.all();
        shops_sl = ShopSerializer(shops, many = True)
        return JsonResponse(shops_sl.data, safe=False)

    elif request.method == 'POST':
        shop_data = JSONParser().parse(request)
        shop_sl = ShopSerializer(data = shop_data)
        if shop_sl.is_valid():
            shop_sl.save()
            return JsonResponse("Added.", safe=False)

    elif request.method == 'PUT':
        shop_data = JSONParser().parse(request)
        shop = Shop.objects.get(ShopId = shop_data['ShopId'])
        shop_sl = ShopSerializer(shop, data = shop_data)
        if shop_sl.is_valid():
            shop_sl.save()
            return JsonResponse("Updated.", safe=False)
        return JsonResponse("Failed to update.")

    elif request.method == 'DELETE':
        shop = Shop.objects.get(ShopId = id)
        shop.delete()
        return JsonResponse("Deleted", safe=False)


@csrf_exempt
def itemAPI(request, id=0):
    if request.method == 'GET':
        items = Item.objects.all();
        items_sl = ItemSerializer(items, many = True)
        return JsonResponse(items_sl.data, safe=False)

    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        item_sl = ItemSerializer(data = item_data)
        if item_sl.is_valid():
            item_sl.save()
            return JsonResponse("Added.", safe=False)
        return JsonResponse("Failed.", safe=False)

    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = Item.objects.get(ShopId = item_data['ItemId'])
        item_sl = ItemSerializer(item, data = item_data)
        if item_sl.is_valid():
            item_sl.save()
            return JsonResponse("Updated.", safe=False)
        return JsonResponse("Failed to update.")

    elif request.method == 'DELETE':
        item = Item.objects.get(ItemId = id)
        item.delete()
        return JsonResponse("Deleted", safe=False)