from django.contrib import admin

from . import models

class CameraAdmin(admin.ModelAdmin):
	list_display = ('name', 'ip', 'auth_uname', 'auth_pwd', 'location', 'option')
	empty_value_display = 'unknown'

class LocationAdmin(admin.ModelAdmin):
	list_display = ('id', 'place')
	empty_value_display = 'unknown'

admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Camera, CameraAdmin)