#TEST to try taking pictures and saving them
#ref: https://raspberrytips.com/picamera2-raspberry-pi/

import time
from picamera2 import Picamera2, Preview

picam = Picamera2()

# Setting up the size of image for pictures and video instead of using default
config = picam.create_preview_configuration(main={"size": (1600, 1200)})
picam.configure(config)

picam.start_preview(Preview.QTGL)

picam.start()


for i in range(1, 5):
    picam.capture_file(f"coffeeMug-{i}.jpg")  # takes picture and saves it
    print(F"Captured image {i}")
    time.sleep(5)  # lapse between takes

picam.stop()