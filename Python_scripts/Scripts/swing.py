from pymycobot.mycobot import MyCobot
import time

num = None


mc = MyCobot('/dev/ttyAMA0',1000000)
mc.power_on()


mc.send_angles([0,0,0,0,0,0],50)
mc.set_color(255,0,0)
mc.send_angle(5,-90,50)

num = 0
while num < 10:
  mc.set_color(0,0,255)
  mc.send_angle(2,45,50)
  time.sleep(.7)
  mc.set_color(255,0,0)
  mc.send_angle(2,0,50)
  time.sleep(.4)
  mc.set_color(0,255,0)
  time.sleep(0.3)
  mc.send_angle(2,(-45),50)
  time.sleep(.7)
  num = num + 1

mc.send_angles([88.68,(-138.51),155.65,(-128.05),(-9.93),(-15.29)],50)
time.sleep(0.5)

mc.send_angles([0,0,0,0,0,0],50)
#mc.release_all_servos()