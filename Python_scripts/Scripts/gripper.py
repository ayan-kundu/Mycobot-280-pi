#!/usr/bin/env python3

from pymycobot.mycobot import MyCobot
import time
# from its orihinal version file
import random, subprocess
from pymycobot.genre import Angle, Coord

mc = MyCobot('/dev/ttyAMA0',1000000)
print('power on' if mc.is_power_on() ==1 else 'power off')

print('init angles:: %s'%mc.get_angles())
print('init coords:: %s'%mc.get_coords())
print('is ATOM connected ==> %s'%mc.is_controller_connected())



def init_move(mc):
  mc.set_gripper_ini() #mc.init_electric_gripper(0)
  #pick init pose
  #mc.send_angles([88.68,0,44.91,46.75,84.37,42],50) 
  mc.send_angles([(-73.65),(-36.65),(-40.86),(-10.54),3.25,(-104.23)],50)
  time.sleep(.5)
  
  # pick pose
  #mc.send_angles([88.68,64,44.91,46.75,84.37,42],50) 
  mc.send_angles([(-73.65),(-80.33),(-40.34),24.16,(-2.02),(-114.69)],50)
  print('object picked !')
  time.sleep(1)

def gripper_test(mc):

  # gripper movement test ######################
  print('...is gripper moving ==>')
  gripper_flag=mc.is_gripper_moving()
  if gripper_flag==0:
    print('no',gripper_flag)
  elif gripper_flag==1:
    print('yes')
  else:
    print('error',gripper_flag) 
  time.sleep(1)

  # quickly closes the gripper
  mc.set_gripper_state(1,70)
  print('gripper set  state 1 | gripper closed')
  time.sleep(1)  

  # gripper closes
  #mc.set_gripper_value(2048,70)
  mc.set_gripper_state(0,70)
  print('gripper set  state 0  | gripper opened')
  time.sleep(1)
  mc.set_gripper_value(200,70) 
  #mc.set_gripper_value(255,70)
  print('gripper set value 100 | gripper closing')
  time.sleep(1)
  
  # gripper opens and closes via set_gripper_value()
  mc.set_gripper_value(50,70)
  print('gripper set value 50   | gripper opening')
  time.sleep(1)
  mc.set_gripper_value(10,70);  print('gripper set value 0 | gripper 0pening')
  print('gripper value==>',mc.get_gripper_value())


def inter_move(mc):
  # mid pose
  #mc.send_angles([(-76.28),0.79,(-1.58),(-1.14),81.03,35.5],50)
  mc.send_angles([(-73.65),(-5.36),(-55.54),(-5.53),(-3.25),-122],50)
  time.sleep(1)
  # mid place pose
  #mc.send_angles([(-82.96),35.33,104.85,20.12,90.17,35.5],50)
  mc.send_angles([105,(-37.96),(-55.54),(-9.93),1.66,-122],50)
  time.sleep(1.4)
  # place pose
  #mc.send_angles([(-88.5),66.7,45.35,46.31,84.11,42],50)
  mc.send_angles([105,(-80),(-41),24,0.96,(-122)],50)

  print('object placed !')

def return_pose(mc):
  # mid place pose
  mc.send_angles([105,(-37.96),(-55.54),(-9.93),1.66,-122],50)
  time.sleep(1)
  #pick init pose
  mc.send_angles([(-73.65),(-36.65),(-40.86),(-10.54),3.25,(-104.23)],50)

if __name__ == "__main__":

  res=raw_input('do you wanna grip from current pose (y/n) ')

  if res == 'y':
    gripper_test(mc)
  else:
    # init move including picking
    init_move(mc)
    # gripper test
    gripper_test(mc)
    # intermidiate move
    inter_move(mc)

    # gripper opens
    mc.set_gripper_value(0,70)
    print('gripper set value 0 | gripper opening')
    time.sleep(1.4)

    #return pose
    return_pose(mc)

