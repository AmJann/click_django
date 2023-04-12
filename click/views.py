from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ClickSerializer
from .models import Click

class ClickRead(generics.ListAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer    


class ClickCreate(generics.CreateAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer  
    

class ClickDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClickSerializer
    queryset = Click.objects.all()
