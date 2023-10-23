#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import String

joystick_data = None
thrust = Float64MultiArray()
#thrust = String
def joy_callback(data):
    global joystick_data
    joystick_data = data.axes

def thrust_value_publisher():
    rospy.init_node('control', anonymous=True)
    rospy.Subscriber('joy', Joy, joy_callback)
    pub = rospy.Publisher('cmd_vel', Float64MultiArray, queue_size = 10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        if joystick_data is not None:
            x = -joystick_data[0]
            y = joystick_data[1]
            r = joystick_data[3]
        
            # Multiplier to have each motor carry out the x and y values in the joystick
            # / \
            # \ /
            a = 1
            b = -1
            # x and y = left joystick, r = right joystick
            LF = a*y + a*x - r
            RF = a*y + b*x + r
            LB = b*y + a*x + r
            RB = b*y + b*x - r

            RLF = abs(LF)
            RRF = abs(RF)
            RLB = abs(LB)
            RRB = abs(RB)

            rel_arr = [RLF,RRF,RLB,RRB]

            rel = max(rel_arr)
            if LF > 1 or RF > 1 or LB > 1 or RB > 1:
                LF = LF/rel
                RF = RF/rel
                LB = LB/rel
                RB = RB/rel
            
            thrust.data = [LF,RF,LB,RB]
            #thrust = ("Hi")

            pub.publish(thrust)
            rate.sleep()

if __name__ == '__main__':
    try:
        thrust_value_publisher()
    except rospy.ROSInterruptException:
        pass
