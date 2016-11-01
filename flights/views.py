from django.shortcuts import render

# Create your views here.
from flights.models import Vol


def index(request):
    vols = Vol.objects().all
    data = {
        'vols': vols,
        'title':'liste des vols'
    }
    return render(request , 'vols.html',data)