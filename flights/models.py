from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model): #this is for defining the parameters in a tablefor sql
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self): #this is defined to give a clean name of the flights in a string
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):#this a class for creating the passengers table in retaion to the flights
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passenger")

    def __str__(self):
        return f"{self.first} {self.last}"
