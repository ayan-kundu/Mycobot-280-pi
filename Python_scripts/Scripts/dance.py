from pymycobot.mycobot import MyCobot
import time


mc = MyCobot('/dev/ttyAMA0',1000000)
mc.power_on()

print('Joint angles... %s'%(mc.get_angles()))
print('Rotational coordinates... %s'%(mc.get_coords()))
mc.send_angles([(0),64.33,(-157.67),110.97,0,0],50)
print('starting Joint angles... %s'%(mc.get_angles()))
print('starting Joint radians... %s'%(mc.get_radians()))
time.sleep (1)

repeat='inf'

while repeat=='inf':

#for count in range(3):
  mc.set_color(0,0,255)
  
# bust down
  mc.send_angles([0,122,(-157.93),29,0,0],80)
  mc.set_color(0,255,0)
  mc.send_angles([0,122,(-157.6),29,(-55),0],80)
  mc.set_color(0,0,255)
  mc.send_angles([0,122,(-157.6),29,0,0],80)
  time.sleep(.5)
 
# bust down up 
  for count in range (3):
	mc.send_angles([(0),21.5,(-157.9),113.99,55,0],80)
	time.sleep(.7)
        mc.set_color(0,0,255)
	mc.send_angles([(0),122,(-157.9),113.99,55,0],80)
	time.sleep(.7)
        mc.set_color(0,0,255)

  for count in range (2):
	mc.send_angles([(62),21.5,(-157.9),113.99,55,0],80)
	time.sleep(.7);mc.set_color(255,255,255)
	mc.send_angles([(62),122,(-157.9),113.99,-55,0],80)
	time.sleep(.7);mc.set_color(255,0,0)
  for count in range (1):
	mc.send_angles([(0),21.5,(-157.9),113.99,55,0],80)
	time.sleep(.7);mc.set_color(0,0,255)
	mc.send_angles([(0),122,(-157.9),113.99,55,0],80)
	time.sleep(.7);mc.set_color(0,255,0)
  for count in range (2):
	mc.send_angles([(-124),21.5,(-157.9),113.99,-55,0],80)
	time.sleep(.7);mc.set_color(0,255,0)
	mc.send_angles([(-124),122,(-157.9),113.99,55,0],80)
	time.sleep(.7);mc.set_color(0,255,0)


#  mc.send_angles([(0),20.5,(-157.9),113.99,55,0],50)
#  mc.send_angles([(-62),20.5,(-157.9),113.99,55,0],50)
  '''   
# little stand pose
  mc.send_angles([0,24,(-82),65.5,(-60),0],50)
  mc.set_color(255,0,0)
  mc.send_angles([0,24,(-87),55.5,(-55),0],50)
  mc.send_angles([0,24,(-87),55.5,55,0],50)
  '''   
  
# middle pose
  mc.send_angles([(0),64.33,(-157.67),110.97,0,0],50)
  mc.set_color(255,255,255)
  time.sleep(.5)

#mc.release_all_servos()