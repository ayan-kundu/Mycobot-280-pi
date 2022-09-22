from pymycobot.mycobot import MyCobot
import time


mc = MyCobot('/dev/ttyAMA0',1000000)
mc.power_on()

# get init pose
init_pose=mc.get_angles()
rest_pose=[122.6, -2.63, -2.02, -1.23, -1.93, -125.5]

# rest pose
mc.send_angles(rest_pose,50)
time.sleep(2)
mc.set_color(255,0,0)

print('fan starting ...')
num = 0;num_loop=0;
while num <= 3:
  num_loop=0
  while num_loop<3:
    # up-down fanning
    mc.set_color(0,0,255)
    mc.send_angles([122.6, -31.64, 45.35, -15.9, 6.32, -125.5],65) # up
    time.sleep(.55)
    mc.send_angles([122.6, -82.0, 144.93, -75.58, 2.81, -125.5],65) # down
    time.sleep(.55)
    mc.set_color(255,0,0)
    num_loop+=1

  print('Zzzzz zzz')
  
  num_loop=0  
  while num_loop<3:
    # side wise fanning
    mc.send_angles( [122.6, -27.77, 50.88, -26.27, -35, -34],50)
    time.sleep(.55)
    mc.send_angles( [122.6, -27.77, 50.88, -26.27, 35, -34],50)
    time.sleep(.55)
    mc.set_color(0,255,0)
    num_loop+=1
  
  num = num + 1

mc.send_angles(init_pose,50)
time.sleep(0.5)

#mc.release_all_servos()