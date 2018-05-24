import serial
import time

device_name = '/dev/ttyACM0'

ser = serial.Serial(device_name, 9600)

ultra_sound_dist = 300
motor_speed = [0, 0]

while 1:
  raw_input = ser.readline()
  if (raw_input):
    ultra_sound_dist = int(raw_input)
    print(ultra_sound_dist)
  motor_speed[0] = (motor_speed[0] + 1) % 255
  motor_speed[0] = (motor_speed[0] + 1) % 255
  ser.write(''.join([str(speed).zfill(4) for speed in motor_speed]))
  print('Sent: ' + ''.join([str(speed).zfill(4) for speed in motor_speed]))
  # time.sleep(1)
