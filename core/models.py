#coding: UTF8

from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Message(models.Model):
	id_type = models.IntegerField(default=0, blank=False, null=False, verbose_name="Tipo de Emegência")
	latitude = models.CharField(blank=False, verbose_name="Latitude", max_length=11)
	logitude = models.CharField(blank=False, verbose_name="Longitude", max_length=11)
	time_log = models.DateTimeField(verbose_name="Horário e cadastro")
	time_out = models.DateTimeField(verbose_name="Horário de recebimento")
	time_in = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "latitude: "+self.latitude + " - logitude: "+self.logitude