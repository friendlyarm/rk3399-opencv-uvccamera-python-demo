## **opencv-uvccamera-cpp-demo**

Run
------------
```
su pi
git clone https://github.com/friendlyarm/rk3399-opencv-ucvcamera-python-demo
cd rk3399-opencv-ucvcamera-python-demo
./run_camera_py.sh
```

Reading mjpeg stream
------------
open the camera using the following code:
```
cap = cv.VideoCapture(get_camerasrc_mjpeg(), cv.CAP_GSTREAMER)
```

Reading NV12 stream
------------
open the camera using the following code:
```
cap = cv.VideoCapture(get_camerasrc_nv12(), cv.CAP_GSTREAMER)
```

Supported camera
------------
```
Logitech C922
KS2A242
```

How can i find out the supported camera resolutions
------------
```
v4l2-ctl --list-formats-ext -d /dev/video10
```

More examples
------------
https://github.com/friendlyarm/opencv-uvccamera-cpp-demo  
https://github.com/friendlyarm/install-opencv-on-friendlycore  

