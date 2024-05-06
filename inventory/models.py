from enum import unique
from django.db import models
import uuid

class Product(models.Model):
    IN_STOCK= "IS"
    OUT_OF_STOCK= "OOS"
    BACKORDERED= "BO"

    STOCK_STATUS = {
        IN_STOCK: "In Stock",
        OUT_OF_STOCK: "Out Of Stock",
        BACKORDERED: "Back Ordered",

    }

    pid = models.CharField(max_length=255)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True)
    is_digital = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    stock_status = models.CharField(max_length=3, choices=STOCK_STATUS, default=OUT_OF_STOCK)

class ProductLine(models.Model):
    price = models.DecimalField()
    sku = models.UUIDField(default=uuid.uuid4)
    stock_qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    order = models.IntegerField()
    weight = models.FloatField()

class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()
    order = models.IntegerField()

class Cateogry(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=False)


class SeasonalEvents(models.Model):
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

