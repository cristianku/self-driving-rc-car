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

with picamera.PiCamera(camera_num=0,sensor_mode=1) as camera:
    camera.resolution = (1024, 768)
    # camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('foo.jpg')