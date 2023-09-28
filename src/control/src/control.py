#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
joystick_data = None

twist = Twist()

def joy_callback(data):
    global joystick_data
    joystick_data = data.axes

def joystick_publisher ():
    rospy.init_node('control', anonymous=True)
    rospy.Subscriber('joy', Joy, joy_callback)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        if joystick_data is not None:
            x_value = joystick_data[0]
            y_value = joystick_data[1]

            twist.linear.x = x_value
            twist.linear.y = y_value
            pub.publish(twist)


            rospy.loginfo("X values %f",x_value)
            rospy.loginfo("Y Value %f",y_value)
            rate.sleep()

if __name__ == '__main__':
    try:
        joystick_publisher()
    except rospy.ROSInterruptException:
        pass
