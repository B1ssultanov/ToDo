from rest_framework import serializers

from .models import *

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ('title', 'description', 'user_id', 'date')