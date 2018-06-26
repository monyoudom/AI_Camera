from __future__ import unicode_literals

from django.db import models


class Location(models.Model):
	place = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	created_at = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.place


	def __str__(self):
		return self.place

class Camera(models.Model):
	ip = models.CharField(max_length=500)
	name = models.CharField(max_length=500)
	location = models.ForeignKey(Location,null=True)
	option = models.CharField(max_length=20)
	auth_uname = models.CharField(max_length=200)
	auth_pwd = models.CharField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	created_at = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name