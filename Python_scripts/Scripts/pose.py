from pymycobot.mycobot import MyCobot
import time


mc = MyCobot('/dev/ttyAMA0',1000000)
mc.power_on()

print(mc.get_angles())
print(mc.get_coords())

if __name__=='__main__':

    for count in range(1):
        # stand by co-ords
        mc.send_coords([112.9,69.9,300,91,7.68,82.89],50,0)
        time.sleep(4)
        # same shape
        mc.send_angles([180,(-85),97,4.83,(-83.23),104.58],0)
        time.sleep(4)
        # 9 pose
        mc.send_angles([94,1.23,90,84,(-99),52],0)
        time.sleep(4)
        # L pose
        mc.send_angles([90,(-142),97,13,(-86.74),108],0)
        time.sleep(4)
        # lucky pose
        mc.send_angles([86,(-89),90,92,(-109),53],0)
        time.sleep(4)