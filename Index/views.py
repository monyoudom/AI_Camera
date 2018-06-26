from django.shortcuts import render ,HttpResponse,redirect
from django.http import StreamingHttpResponse

from camera import VideoCamera
from .models  import Location, Camera
from .form   import LocationForm, CameraForm
def basic(request):
	locations = Location.objects.all()

	context = { 

	'locations':locations

	}
	return render(request, "Index/basic.html"  , context)

def index(request):
	locations = Location.objects.all()

	
	
	context = {


	'locations':locations

	}
	return render(request, "Index/home.html"  , context)
	#return HttpResponse ("hello")	
def addlocation(request):
	locations = Location.objects.all()

	
	if request.method == "POST":
		form  = LocationForm(request.POST)
		if form.is_valid():
			post = form.save(commit=True)
			
			return redirect('/addcamera')
	else:
		form = LocationForm()
 	
 	return render(request,'Index/Addlocation.html', {'form':form,'locations':locations})


def addcamera(request):
	locations = Location.objects.all()

	
	context = {}

	if request.method == "POST":
		ip = request.POST['ip']
		name = request.POST['name']
		loc = request.POST['location']
		auth_uname = request.POST['auth_uname']
		auth_pwd   = request.POST['auth_pwd']
		option = request.POST.getlist('option[]')
		optionStr = ','.join(str(x) for x in option)
		location = Location.objects.get(pk=loc)
		camObj = Camera.objects.create(
									ip=ip,
									name=name,
									location=location,
									option = optionStr,
									auth_uname = auth_uname,
									auth_pwd = auth_pwd
								)

		camObj.save()
		Camname = Camera.objects.all()

		CameraLists = Camera.objects.filter(location__pk = request.POST.get('location'))
		context.update({'CameraLists' : CameraLists,'Camname':Camname,'locations' : locations})

		return render (request,"Index/cameralocation.html",context)

	locations = Location.objects.all()

	context.update({'locations' : locations})

	return render (request,"Index/Camera_Add.html",context)

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_streamer(request, camID ):
	camObj = Camera.objects.get(pk=camID)

	
	camIP = "rtsp://%s:%s@%s/" %(camObj.auth_uname, camObj.auth_pwd, camObj.ip)



	

	
		
	
	

	

	
	
	repsone = gen(VideoCamera(camIP))
	
	return  StreamingHttpResponse(repsone,content_type='multipart/x-mixed-replace; boundary=frame')

def camera_by_location(request ,locationid):
	
	context = {}

	CameraLists = Camera.objects.filter(location__id =locationid)
	locations = Location.objects.all()

	context.update({
		'CameraLists': CameraLists,
		'locations': locations
	})

	return render(request, "Index/cameralocation.html", context)

def cameras_list(request):
	context = {}
	CameraLists = Camera.objects.all()
	locations = Location.objects.all()
	context.update({'CameraLists' : CameraLists,'locations' : locations})

	return render (request,"Index/cameras.html",context)

 
