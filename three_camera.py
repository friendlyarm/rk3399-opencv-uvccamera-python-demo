import numpy as np
import cv2 as cv
import time
import os

# MJPEG
def get_camerasrc_mjpeg(n):
    # cam_width=1920
    # cam_height=1080
    cam_width=432
    cam_height=240
    cam_frames=15
    return 'v4l2src device=/dev/video'+str(n)+' io-mode=4 ! image/jpeg,width='+str(cam_width)+',height='+str(cam_height)+',framerate='+str(cam_frames)+'/1 ! jpegdec ! videoconvert ! video/x-raw,format=BGR ! appsink drop=true'

# NV12
def get_camerasrc_nv12(n):
    cam_width=640
    cam_height=480
    cam_frames=30
    return 'v4l2src device=/dev/video'+str(n)+' io-mode=4 ! videoconvert ! video/x-raw,format=NV12,width='+str(cam_width)+',height='+str(cam_height)+',framerate='+str(cam_frames)+'/1 ! videoconvert ! video/x-raw,format=BGR ! appsink drop=true'

cap1 = cv.VideoCapture(get_camerasrc_mjpeg(10), cv.CAP_GSTREAMER)
cap2 = cv.VideoCapture(get_camerasrc_mjpeg(12), cv.CAP_GSTREAMER)
cap3 = cv.VideoCapture(get_camerasrc_mjpeg(14), cv.CAP_GSTREAMER)

if not cap1.isOpened():
    print("Cannot capture from camera1. Exiting.")
    os._exit(1)

if not cap2.isOpened():
    print("Cannot capture from camera2. Exiting.")
    os._exit(1)

if not cap3.isOpened():
    print("Cannot capture from camera3. Exiting.")
    os._exit(1)

last_time = time.time()

cv.namedWindow("1")
cv.namedWindow("2")
cv.namedWindow("3")

while(True):

    ret1, frame1 = cap1.read()
    if ret1:
        cv.imshow('1', frame1)
    else:
        print("empty frame1")

    del frame1
    del ret1

    ret2, frame2 = cap2.read()
    if ret2:
        cv.imshow('2', frame2)
    else:
        print("empty frame2")

    del frame2
    del ret2

    ret3, frame3 = cap3.read()
    if ret3:
        cv.imshow('3', frame3)
    else:
        print("empty frame3")

    del frame3
    del ret3

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cap3.release()
cv.destroyAllWindows()

