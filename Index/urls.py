from django.conf.urls import url
from . import views

urlpatterns = [

	url (r'^index/', views.basic, name='index'),
 	
	url (r'^home/', views.index, name='home'),
	url(r'^addlocation/',views.addlocation , name = 'addlocation'),
 	url(r'^addcamera/',views.addcamera, name='addcamera'),
 	url(r'^video_streamer/(?P<camID>\d+)',views.video_streamer, name='video_streamer'),
 	url(r'^camera_by_location/(?P<locationid>\d+)', views.camera_by_location, name='camera_by_location'),
 	url(r'^cameras/',views.cameras_list, name='cameras_list')
   
]