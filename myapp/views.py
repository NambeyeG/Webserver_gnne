from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .models import Temperature
from .serializer import TemperatureSerializer
from django.shortcuts import get_object_or_404

def dashboard(request):
    return render(request, 'myapp/dashboard.html')

class TemperatureDetailView(generics.RetrieveAPIView):
    queryset = Temperature.objects.all().order_by('-timestamp')
    serializer_class = TemperatureSerializer

class TemperatureListView(generics.ListAPIView):
    queryset = Temperature.objects.all().order_by('-timestamp')
    serializer_class = TemperatureSerializer

class TemperatureCreateAPIView(generics.CreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer


def get_readings(request):
    # Fetch the latest reading (assuming the latest entry is the latest reading)
    latest_reading = Temperature.objects.order_by('-timestamp').first()
    
    if latest_reading:
        data = {
            'temperature': latest_reading.temperature,
            'humidity': latest_reading.humidity,
        }
    else:
        # If no data is found, return default values
        data = {
            'temperature': 0.0,
            'humidity': 0.0,
        }
    
    return JsonResponse(data)