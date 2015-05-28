from django.db import models
from django.contrib.auth.models import User

class EventPeriodType(models.Model):
    name = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = True
        db_table = 'event_period_type'

class CalendarEvent(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500, blank=True)
    event_period_type = models.ForeignKey('EventPeriodType')
    user = models.ForeignKey(User)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    date = models.DateTimeField()
    
    class Meta:
        managed = True
        db_table = 'calendar_event'        