from django.shortcuts import render
from rest_framework import generics
from .serializers import ClickSerializer
from .serializers import LocationSerializer
from .models import Click
from .models import Location

class ClickRead(generics.ListAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer    


class ClickCreate(generics.CreateAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer  
    

class ClickDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClickSerializer
    queryset = Click.objects.all()

class LocationRead(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer    


class LocationCreate(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer   

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()    
    
