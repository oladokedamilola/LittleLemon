from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.title} - ${self.price}"


class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    booking_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.name} on {self.booking_date}"
