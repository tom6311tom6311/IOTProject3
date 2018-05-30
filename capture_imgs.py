import sys
from picamera import PiCamera
from time import sleep

imgs_dir = sys.argv[1]
img_idx = 0

camera = PiCamera()

while 1:
  camera.capture(imgs_dir + '/' + str(img_idx) + '.jpg')
  sleep(5)
