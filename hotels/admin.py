from django.contrib import admin

# Register your models here.

# Register your models here.
#admin.site
from hotels.models import Hotel,Chambre,Client,Reservation
admin.site.register(Hotel)
admin.site.register(Chambre)
admin.site.register(Client)
admin.site.register(Reservation)