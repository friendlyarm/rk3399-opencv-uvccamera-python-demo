import numpy as np
import cv2 as cv
import time
import os

# MJPEG
def get_camerasrc_mjpeg():
    # cam_width=1920
    # cam_height=1080
    cam_width=800
    cam_height=600
    cam_frames=30
    return 'v4l2src device=/dev/video10 io-mode=4 ! image/jpeg,width='+str(cam_width)+',height='+str(cam_height)+',framerate='+str(cam_frames)+'/1 ! jpegdec ! videoconvert ! video/x-raw,format=BGR ! appsink'

# NV12
def get_camerasrc_nv12():
    cam_width=640
    cam_height=480
    cam_frames=30
    return 'v4l2src device=/dev/video10 io-mode=4 ! videoconvert ! video/x-raw,format=NV12,width='+str(cam_width)+',height='+str(cam_height)+',framerate='+str(cam_frames)+'/1 ! videoconvert ! video/x-raw,format=BGR ! appsink'

cap = cv.VideoCapture(get_camerasrc_mjpeg(), cv.CAP_GSTREAMER)

cv.namedWindow("left")
cv.moveWindow("left", 40, 80)

if not cap.isOpened():
    print("Cannot capture from camera. Exiting.")
    os._exit(1)
last_time = time.time()

while(True):

    ret, frame = cap.read()
    cv.imshow('left', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
