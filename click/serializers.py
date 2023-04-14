from rest_framework import serializers
from .models import Click

class ClickSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Click
        fields = ('uuid','count')