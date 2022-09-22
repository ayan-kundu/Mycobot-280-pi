from pymycobot.mycobot import MyCobot
import time, random
rand=random.randint(0,255)

mc = MyCobot('/dev/ttyAMA0',1000000)
mc.power_on()

current_angles=mc.get_angles()
current_angles[0]=-90


flag='inf'

# init pose
mc.set_color(rand,rand,rand)
mc.send_angles(current_angles,75)
print("Let's Dance... Dance Dance !!!" )
while flag =='inf':
    rand=random.randint(0,255)
    # loop start ...

    mc.set_color(rand,0,0)
    mc.send_angles([-90, -40, 40, -12, 84.95, -45],50)
    time.sleep(1)
    mc.set_color(0,rand,0)
    
    mc.send_angles([-90, 26, -48, 14, 85.95,45],50)
    time.sleep(1)