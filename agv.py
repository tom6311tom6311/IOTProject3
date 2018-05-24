import serial
import time
import os
import shutil
import subprocess
import atexit

device_name = '/dev/ttyACM0'
imgs_dir = 'imgs'
sub_ps = []

subp_capture_imgs = subprocess.Popen(['python', 'capture_imgs.py', device_name])
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

ultra_sound_dist = 300
motor_speed = [0, 0]

while 1:
  raw_input = ser.readline().replace('\r', '').replace('\n', '')
  if (raw_input):
    ultra_sound_dist = float(raw_input)
    print(ultra_sound_dist)
  motor_speed[0] = (motor_speed[0] + 10) % 255
  motor_speed[1] = (motor_speed[1] + 10) % 255
  ser.write(''.join([str(speed).zfill(3) for speed in motor_speed]))
  print('Sent: ' + ''.join([str(speed).zfill(3) for speed in motor_speed]))
  # time.sleep(1)
