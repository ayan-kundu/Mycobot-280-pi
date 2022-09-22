from pymycobot.mycobot import MyCobot
import time

num = None


mc = MyCobot('/dev/ttyAMA0',1000000)
mc.power_on()
j=input('enter joint no to release or all ')
time.sleep(2)
current_angles=mc.get_angles()
print('current angles %s'%current_angles)
#mc.release_all_servos()
print(j)

if j >0 and j <7:
    mc.release_servo(int(j))
else:
    mc.release_all_servos()
# mc.release_servo(3);#mc.focus_servo(1)