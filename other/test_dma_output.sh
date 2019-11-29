#!/bin/bash

gst-launch-1.0 v4l2src io-mode=4 device=/dev/video10 ! "image/jpeg,width=1920,height=1080,framerate=30/1" ! mppvideodec ! kmssink
