from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from hotels.models import Hotel,Reservation,Client



def index(request):
    hotels = Hotel.objects.filter(etoiles__gt=2,description__icontains='ville').order_by('nom')
    hotels = Hotel.objects.order_by('nom')
    data = {
        'hotels' : hotels,
        'title': 'liste des hotels',
    }
    return render(request , 'index.html',data)

class HotelList(ListView):
    model = Hotel
class HotelCreate(CreateView):
    model = Hotel
    fields = ['nom','description','etoiles']
    success_url = '/hotels'
class HotelUpdate(UpdateView):
    model = Hotel
    fields = ['nom','description','etoiles']
    success_url = '/hotels'
class HotelDetail(DetailView):
    model = Hotel
    fields = ['nom','description','etoiles']
class HotelDelete(DeleteView):
    model = Hotel
    fields = ['nom','description','etoiles']
    success_url = '/hotels'


def reservations(request):

    reservations = Reservation.objects.all()
    data = {
        'reservations' : reservations,
        'title': 'liste des reservations',
    }
    return render(request , 'reservations.html',data)

class ReservationList(ListView):
    model = Reservation
class ReservationCreate(CreateView):
    model = Reservation
    fields = ['hotel','client','date_reservation']
    success_url = '/reservations'
class ReservationUpdate(UpdateView):
    model = Reservation
    fields = ['hotel','client','date_reservation']
    success_url = '/reservations'
class ReservationDetail(DetailView):
    model = Reservation
    fields = ['hotel','client','date_reservation']
class ReservationDelete(DeleteView):
    model = Reservation
    fields = ['hotel','client','date_reservation']
    success_url = '/reservations'

