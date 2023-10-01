#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray


joystick_data = None

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
            
    
            a1 = 1
            b1 = 1
            c1 = -1
            d1 = -1

            a2 = 1
            b2 = -1
            c2 = 1
            d2 = -1
                

            LFM = a1*y + a2*x + r
            RFM = b1*y + b2*x + r
            LBM = c1*y + c2*x + r
            RBM = d1*y + d2*x + r
            thrust = Float64MultiArray()

            thrust.data = [LFM,RFM,LBM,RBM]



            pub.publish(thrust)
            rate.sleep()


if __name__ == '__main__':
    try:
        thrust_value_publisher()
    except rospy.ROSInterruptException:
        pass
