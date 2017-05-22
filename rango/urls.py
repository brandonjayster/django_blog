
from django.conf.urls import url, include
from rango import views

urlpatterns = [
url(r'^', views.index, name='index'),
]