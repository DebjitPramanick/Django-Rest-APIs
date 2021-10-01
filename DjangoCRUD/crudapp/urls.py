from django.conf.urls import url
from crudapp import views


urlpatterns = [
    url(r'^batch$', views.batchAPI),
    url(r'^batch/([0-9]+)$', views.batchAPI),
    url(r'^student$', views.studentAPI),
    url(r'^student/([0-9]+)$', views.studentAPI)
]