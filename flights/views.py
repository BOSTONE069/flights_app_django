from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights":Flight.objects.all()
    })

def flight(request, flight_id): #this is for checking the passengrs with the given flights
    flight =Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html",{
        "flight":flight,
        "passenger": flight.passenger.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()

    })

def book(request, flight_id): #this is a function for booking a flight 
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id) #pk represent the primary key
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id, )))
