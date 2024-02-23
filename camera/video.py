#TEST to try taking video and saving them
#ref: https://raspberrytips.com/picamera2-raspberry-pi/

import time

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder

picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

encoder = H264Encoder(10000000)

# creating 10s video
picam2.start_recording(encoder, 'test_video.h264')
time.sleep(10)
picam2.stop_recording()