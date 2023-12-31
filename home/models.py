from django.db import models

class Amenities(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Hotels(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_description = models.TextField()
    hotel_image = models.CharField(max_length=500)
    hotel_price = models.IntegerField()
    amenities = models.ManyToManyField(Amenities)

    def __str__(self):
        return self.hotel_name

