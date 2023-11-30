from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()
    access_type = models.CharField(max_length=10)
    location = models.CharField(max_length=25)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()
    access_type = models.CharField(max_length=10)
    car_model = models.CharField(max_length=30)
    car_plateNo = models.CharField(max_length=15)
    car_BodyColor = models.CharField(max_length=15)
    price_rate = models.CharField(max_length=10)
    rating = models.IntegerField(null=True, blank=True)
    reviews = models.TextField(blank=True)
    order_id = models.CharField(max_length=25, default="None")
    location = models.CharField(max_length=25)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    buyer_name = models.CharField(max_length=50)
    seller_name = models.CharField(max_length=50)
    price_rate = models.CharField(max_length=10)
    delivery_fee = models.IntegerField()
    total_amount = models.IntegerField()
    origin = models.CharField(max_length=25)
    destination = models.CharField(max_length=25)
    time_engagement = models.CharField(max_length=30)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.pk + "   " + self.seller_name + ":" + self.buyer_name
