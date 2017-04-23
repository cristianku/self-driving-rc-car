import time
import picamera

# sensor modes
#	Resolution	Aspect Ratio	Framerates	Video	Image	FoV	Binning
# 1	1920x1080	16:9	1-30fps	    x	 	        Partial	None
# 2	2592x1944	4:3	    1-15fps	    x	    x	    Full	None
# 3	2592x1944	4:3	    0.1666-1fps	x	    x	    Full	None
# 4	1296x972	4:3	    1-42fps	    x	 	        Full	2x2
# 5	1296x730	16:9	1-49fps	    x	 	        Full	2x2
# 6	640x480	    4:3	    42.1-60fps	x	 	        Full	4x4
# 7	640x480	    4:3	    60.1-90fps	x	 	        Full	4x4

class camera():

    def __init__(self):
        self.camera = picamera.PiCamera(camera_num=0,sensor_mode=4)
        # Camera warm-up time
        time.sleep(2)

    def take_picture(self):
        self.camera.brightness = 50
        self.camera.sharpness = 0
        self.camera.contrast = 0
        self.camera.saturation = 0
        self.camera.ISO = 400
        self.camera.video_stabilization = False
        self.camera.exposure_compensation = 0
        self.camera.exposure_mode = 'auto'
        #
        # 'off'
        # 'auto'
        # 'night'
        # 'nightpreview'
        # 'backlight'
        # 'spotlight'
        # 'sports'
        # 'snow'
        # 'beach'
        # 'verylong'
        # 'fixedfps'
        # 'antishake'
        # 'fireworks'

        # self.camera.meter_mode = 'average'
        self.camera.sharpness = 0
        self.camera.awb_mode = 'auto'
        self.camera.image_effect = 'none'
        self.camera.color_effects = None
        self.camera.rotation = 0
        self.camera.hflip = False
        self.camera.vflip = False
        self.camera.crop = (0.0, 0.0, 1.0, 1.0)
        self.camera.start_preview()
        self.camera.capture('photo.jpg',format='jpeg')
        self.camera.stop_preview()