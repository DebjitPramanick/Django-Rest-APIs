from django.conf.urls import url
from DjangoApp import views

urlpatterns = [
    url(r'^shop$', views.shopAPI),
    url(r'^shop/([0-9]+)$', views.shopAPI),
    url(r'^item$', views.itemAPI),
    url(r'^item/([0-9]+)$', views.itemAPI)
]