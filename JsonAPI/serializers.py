from django.contrib.auth.models import User
from JsonAPI import models
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'email', 'is_staff', 'is_active', 'is_superuser')
        
class EventPeriodTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EventPeriodType 
        fields = ('id', 'name')
        
class CalendarEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CalendarEvent 
        fields = ('id', 'name', 'description', 'event_period_type', 'user', 'start_time', 'end_time', 'date')        
                