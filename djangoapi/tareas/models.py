from django.db import models
from django.utils import timezone


class Tarea(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    fechaDesde = models.DateTimeField(default=timezone.now)
    fechaHasta = models.DateTimeField(default=timezone.now)
  
   