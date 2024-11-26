from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializer import *
from .models import Menu

# View for listing and creating menu items
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer 

# View for retrieving, updating, and deleting a single menu item
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for managing table bookings.
    """
    queryset = Booking.objects.all()  # Fetch all Booking objects
    serializer_class = BookingSerializer  # Use the BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
