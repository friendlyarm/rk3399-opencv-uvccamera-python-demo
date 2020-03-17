import numpy as np
import cv2 as cv
import os
import v4l2capture
import select

if __name__ == '__main__':
    #cap = cv.VideoCapture(0)
    #cap.set(cv.cv.CV_CAP_PROP_FRAME_WIDTH, 1920)      # <-- this doesn't work. OpenCV tries to set VIDIO_S_CROP instead of the frame format
    #cap.set(cv.cv.CV_CAP_PROP_FRAME_HEIGHT, 1080)
    
    # The following is from: https://github.com/gebart/python-v4l2capture
    
    # Open the video device.
    video = v4l2capture.Video_device("/dev/video10")
    
    # Suggest an image size to the device. The device may choose and
    # return another size if it doesn't support the suggested one.
    size_x, size_y = video.set_format(1920, 1080, fourcc='MJPG')
    
    print("device chose {0}x{1} res".format(size_x, size_y))
    
    # Create a buffer to store image data in. This must be done before
    # calling 'start' if v4l2capture is compiled with libv4l2. Otherwise
    # raises IOError.
    video.create_buffers(30)
    
    # Send the buffer to the device. Some devices require this to be done
    # before calling 'start'.
    video.queue_all_buffers()
    
    # Start the device. This lights the LED if it's a camera that has one.
    print("start capture")
    video.start()

    while(True):
        #We used to do the following, but it doesn't work :(
        #ret, frame = cap.read()
        
        #Instead...
        
        # Wait for the device to fill the buffer.
        select.select((video,), (), ())

        # The rest is easy :-)
        image_data = video.read_and_queue()
        frame = cv.imdecode(np.frombuffer(image_data, dtype=np.uint8), cv.IMREAD_COLOR)
    
        cv.imshow('frame', frame)
        key = cv.waitKey(1)
        if key & 0xFF == ord('q'):
            break

    #cap.release()
    video.close()
    
    cv.destroyAllWindows()
