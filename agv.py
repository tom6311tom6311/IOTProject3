import serial
import time

device_name = '/dev/ttyACM0'

ser = serial.Serial(device_name, 9600)

ultra_sound_dist = 300
motor_speed = [0, 0]

while 1:
  raw_input = ser.readline().replace('\r', '').replace('\n', '')
  if (raw_input):
    ultra_sound_dist = float(raw_input)
    print(ultra_sound_dist)
  motor_speed[0] = (motor_speed[0] + 1) % 255
  motor_speed[1] = (motor_speed[1] + 1) % 255
  ser.write(''.join([str(speed).zfill(3) for speed in motor_speed]))
  print('Sent: ' + ''.join([str(speed).zfill(3) for speed in motor_speed]))
  # time.sleep(1)
