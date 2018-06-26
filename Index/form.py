from django import forms

from .models import Location,Camera

class LocationForm(forms.ModelForm):
	place = forms.CharField(max_length=128, help_text="Please enter the category name.")
	class Meta:
		model = Location
		fields = ('place',)

class CameraForm(forms.ModelForm):
	ip = forms.CharField(max_length=30, help_text= "Please enter the category name.")
	name = forms.CharField(max_length=100, help_text="Pleas enter the category name")
	# location = forms.CharField(max_length=100, help_text="Pleas enter the category name")
	# option  = forms.CharField(max_length=100 , help_text="Pleas Enter the value")

	class Meta:
		model = Camera

		fields = ('ip', 'name',)
		
			
	