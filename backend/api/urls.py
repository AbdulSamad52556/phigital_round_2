from django.urls import path
from .views import AssistantFlightBookingPage, AssistantHotelBookingPage, FlightBookingPage, HotelBookingPage

urlpatterns = [
    path('flightbooking', FlightBookingPage.as_view(), name='flightbooking'),
    path('hotelbooking', HotelBookingPage.as_view(), name='hotelbooking'),
    path('assistantflightbooking', AssistantFlightBookingPage.as_view(), name='assistantflightbooking'),
    path('assistanthotelbooking', AssistantHotelBookingPage.as_view(), name='assistanthotelbooking')
]
