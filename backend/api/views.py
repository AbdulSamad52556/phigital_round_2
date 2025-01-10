from django.shortcuts import render
from rest_framework.views import APIView, Response
from .permissions import IsAdmin, IsManagerWithRestrictedAccess
# Create your views here.

class FlightBookingPage(APIView):
    
    def get(self, request):
        return Response({'message':'This is FlightBookingPage'})

class HotelBookingPage(APIView):

    def get(self, request):
        return Response({'message':'This is Hotel Booking Page'})

class AssistantFlightBookingPage(APIView):
    permission_classes = [ IsAdmin | IsManagerWithRestrictedAccess ]
    
    def get(self, request):
        return Response({'message':'This is AssistantFlightBookingPage'})

class AssistantHotelBookingPage(APIView):
    permission_classes = [ IsAdmin | IsManagerWithRestrictedAccess ]

    def get(self, request):
        return Response({'message':'This is AssistantHotelBookingPage'})

