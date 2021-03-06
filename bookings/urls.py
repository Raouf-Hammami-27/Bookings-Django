"""bookings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from hotels import views as hv
from flights import views as fv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^hotels$',hv.index),
    url(r'^hotels$', hv.HotelList.as_view(), name="hotels-list"),
    url(r'^hotels/(?P<pk>\d+)$', hv.HotelDetail.as_view(), name="hotel-detail"),
    url(r'^hotel/create$', hv.HotelCreate.as_view(), name="hotel-create"),
    url(r'^hotel/update/(?P<pk>\d+)$', hv.HotelUpdate.as_view(), name="hotel-update"),
    url(r'^hotel/delete/(?P<pk>\d+)$', hv.HotelDelete.as_view(), name="hotel-delete"),
    url(r'^vols$', fv.index),

    url(r'^reservations$', hv.ReservationList.as_view(), name="reservations-list"),
    url(r'^reservations/(?P<pk>\d+)$', hv.ReservationDetail.as_view(), name="reservation-detail"),
    url(r'^reservation/create$', hv.ReservationCreate.as_view(), name="reservation-create"),
    url(r'^reservation/update/(?P<pk>\d+)$', hv.ReservationUpdate.as_view(), name="reservation-update"),
    url(r'^reservation/delete/(?P<pk>\d+)$', hv.ReservationDelete.as_view(), name="reservation-delete"),

    url(r'^login/$', views.login,{'template_name': 'registration/login.html'}, name="login"),
    url(r'^logout/$', views.logout, {'template_name': 'registration/logged_out.html'},name="logout"),
]
