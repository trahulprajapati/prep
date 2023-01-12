#
from django.urls import path
from django.conf.urls import include, url
from .views import hello
from prep.apps.msapps.producers import views
urlpatterns = [
    path('', views.hello),
    #url('', hello, name='ad')
]

