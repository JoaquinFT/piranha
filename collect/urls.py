
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^trades$', views.trades, name='trades'),
    url(r'^spreads$', views.spreads, name='spreads'),
]
