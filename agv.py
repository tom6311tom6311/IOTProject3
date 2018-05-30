import serial
import time
import os
import shutil
import subprocess
import atexit

device_name = '/dev/ttyACM0'
imgs_dir = 'imgs'
motor_delta = 0.05
sub_ps = []

subp_capture_imgs = subprocess.Popen(['python', 'capture_imgs.py', imgs_dir])
sub_ps.append(subp_capture_imgs)

def on_exit():
  print('Terminating subprocess...')
  for p in sub_ps:
    p.terminate()
  print('done')

atexit.register(on_exit)

if not os.path.exists(imgs_dir):
  os.makedirs(imgs_dir)
else:
  shutil.rmtree(imgs_dir)
  os.makedirs(imgs_dir)


ser = serial.Serial(device_name, 9600)

motor_speed = [0.0, 0.0]

while 1:
  raw_input = ser.readline().replace('\r', '').replace('\n', '')
  if (raw_input):
    [front_sonar_dist, left_sonar_dist, angle] = [float(i) for i in raw_input.split(' ')]
    print(left_sonar_dist)
    if (left_sonar_dist > 40 or left_sonar_dist == 0):
      motor_speed[0] = (motor_speed[0] + motor_delta) % 255
      motor_speed[1] = (motor_speed[1] - motor_delta) % 255
    else:
      motor_speed[0] = (motor_speed[0] - motor_delta) % 255
      motor_speed[1] = (motor_speed[1] + motor_delta) % 255

    ser.write(''.join([str(int(speed)).zfill(3) for speed in motor_speed]))
    print('Sent: ' + ''.join([str(int(speed)).zfill(3) for speed in motor_speed]))
    # time.sleep(1)
