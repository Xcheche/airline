from django.shortcuts import render
from .models import Flight
import datetime
# Create your views here.


def index(request):
    return render(request, 'flights/index.html', {
        'flights': Flight.objects.all()
    })

def flight(request, flight_id):
    date = datetime.datetime.now()
    flight = Flight.objects.get(pk=flight_id)

    return render(request,'flights/flight.html',{
        'flight':flight,'date':date
    })