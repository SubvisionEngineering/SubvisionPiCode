#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class thruster:
    def thrusting(self):
        rospy.init_node('test_code_1')

    def vel(self, twist_data):
        linear_x = twist_data.linear.x

        thrust_speed = linear_x * 2
        
        rospy.loginfo(thrust_speed)
        rate.sleep()

    def run(self):
        rospy.Subscriber('cmd_vel', Twist, self.vel)
        rospy.spin()

if __name__ == '__main__':
    try:
        check = thruster()
        check.run()
    except rospy.ROSInterruptException:
        pass
