from django.conf.urls import url
from TodoApp import views

urlpatterns=[
    url(r'^list$', views.listAPI),
    url(r'^list/([0-9]+)$', views.listAPI),
    url(r'^task$', views.taskAPI),
    url(r'^task/([0-9]+)$', views.taskAPI)
]