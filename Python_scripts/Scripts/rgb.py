from pymycobot.mycobot import MyCobot
import time

num = None


mc = MyCobot('/dev/ttyAMA0',1000000)
mc.power_on()

current_angles=mc.get_angles()
current_angles[-2]=60
mc.send_angles(current_angles,50)
time.sleep(0.5)

num = 1
while num > 0:

  mc.send_angle(6,15,50)
  mc.set_color(255,0,0);time.sleep(.35)
  mc.set_color(255,126,63)
  time.sleep(0.5)
  mc.set_color(0,255,0)
  time.sleep(0.6)

  mc.set_color(0,0,255);time.sleep(.35)
  mc.set_color(55,255,55)
  mc.send_angle(6,(-30),50)
  time.sleep(0.6)
  mc.set_color(125,125,125)

  num = num + 1

