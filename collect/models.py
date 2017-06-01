from django.db import models

# Create your models here.

class Config(models.Model):
    pair = models.CharField(max_length = 10)
    series = models.CharField(max_length = 10)
    last = models.CharField(max_length = 100)

class Trades(models.Model):
    price = models.FloatField()
    volume = models.FloatField()
    time = models.FloatField()
    pair = models.CharField(max_length = 10)

class Spreads(models.Model):
    time = models.FloatField()
    bid = models.FloatField()
    ask = models.FloatField()
    pair = models.CharField(max_length = 10)

class OHLC1(models.Model):
    time = models.FloatField()
    o = models.FloatField()
    h = models.FloatField()
    l = models.FloatField()
    c = models.FloatField()
    pair = models.CharField(max_length = 10)

class OHLC5(models.Model):
    time = models.FloatField()
    o = models.FloatField()
    h = models.FloatField()
    l = models.FloatField()
    c = models.FloatField()
    pair = models.CharField(max_length = 10)

class OHLC15(models.Model):
    time = models.FloatField()
    o = models.FloatField()
    h = models.FloatField()
    l = models.FloatField()
    c = models.FloatField()
    pair = models.CharField(max_length = 10)

class OHLC60(models.Model):
    time = models.FloatField()
    o = models.FloatField()
    h = models.FloatField()
    l = models.FloatField()
    c = models.FloatField()
    pair = models.CharField(max_length = 10)

class OHLC240(models.Model):
    time = models.FloatField()
    o = models.FloatField()
    h = models.FloatField()
    l = models.FloatField()
    c = models.FloatField()
    pair = models.CharField(max_length = 10)

class OHLC1440(models.Model):
    time = models.FloatField()
    o = models.FloatField()
    h = models.FloatField()
    l = models.FloatField()
    c = models.FloatField()
    pair = models.CharField(max_length = 10)
