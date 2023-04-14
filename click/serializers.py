from rest_framework import serializers
from .models import Click
from .models import Location

class ClickSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Click
        fields = ('uuid','count')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('uuid','city','state','country')        