import cv2

face_cascade = cv2.CascadeClassifier('Index/haarcascade_frontalface_default.xml')

class VideoCamera(object):

    def __init__(self,camID):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.\
        self.camID= camID
        self.video = cv2.VideoCapture(camID)


        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    def __del__(self):
        self.video.release()

    

    def get_frame(self):
        success, image = self.video.read()
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        
        
        
      

        for (x,y,w,h) in faces:
             cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
             roi_gray = gray[y:y+h, x:x+w]
             roi_color = image[y:y+h, x:x+w]
            


            
    
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()