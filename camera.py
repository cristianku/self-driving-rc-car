import time
import picamera
import matplotlib.image as mpimg
import numpy as np
from fractions import Fraction

# from moviepy.editor import VideoFileClip
#

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
        # self.camera.framerate = Fraction(1, 6)

        # self.camera.shutter_speed = 6000000
        self.camera.exposure_mode = 'off'
        self.camera.iso = 800

        time.sleep(2)

    def take_picture(self):
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
        self.camera.start_preview()
        self.camera.capture('photo.jpg',format='jpeg')
        self.camera.stop_preview()

    def lane_detection(self):

        image = mpimg.imread('photo.jpg')

        import cv2  # bringing in OpenCV libraries
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # grayscale conversion

        # cv2.imwrite('photo_gray_image.png', gray)

        # Define a kernel size and apply Gaussian smoothing
        kernel_size = 5
        blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

        # Define our parameters for Canny and apply
        low_threshold = 50
        high_threshold = 130
        edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
        cv2.imwrite('photo_edges.png', edges)

        # Next we'll create a masked edges image using cv2.fillPoly()
        mask = np.zeros_like(edges)
        ignore_mask_color = 255

        # This time we are defining a four sided polygon to mask
        imshape = image.shape
        vertices = np.array([[(0, imshape[0]), (250, 230), (1350, 230), (imshape[1], imshape[0])]], dtype=np.int32)
        cv2.fillPoly(mask, vertices, ignore_mask_color)
        masked_edges = cv2.bitwise_and(edges, mask)

        masked_edges2 = cv2.bitwise_and(blur_gray, mask)
        cv2.imwrite('photo_masked_edges.png', masked_edges2)


        # Define the Hough transform parameters
        # Make a blank the same size as our image to draw on
        rho = 3  # distance resolution in pixels of the Hough grid
        theta = 1  # np.pi/180 # angular resolution in radians of the Hough grid
        threshold = 5  # minimum number of votes (intersections in Hough grid cell)
        min_line_length = 2  # minimum number of pixels making up a line
        max_line_gap = 100  # maximum gap in pixels between connectable line segments
        line_image = np.copy(image) * 0  # creating a blank to draw lines on

        # Run Hough on edge detected image
        # Output "lines" is an array containing endpoints of detected line segments
        lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
                                min_line_length, max_line_gap)

        # Iterate over the output "lines" and draw lines on a blank image
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)

        # Create a "color" binary image to combine with line image
        color_edges = np.dstack((edges, edges, edges))

        # Draw the lines on the edge image
        lines_edges = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)

        cv2.imwrite('photo_lines_edges.png', lines_edges)
