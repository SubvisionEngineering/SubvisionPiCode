#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray

def callback(data):
    # Extract the array data from the received message
    Thrust_data = data.data

    # Check if the array has at least three elements
    if len(Thrust_data) >= 4:
        # Split the values into separate variables
        LFM = Thrust_data[0]
        RFM = Thrust_data[1]
        LBM = Thrust_data[2]
        RBM = Thrust_data[3]
        # Process and use the separate variables as needed
        rospy.loginfo("Received values: LFM=%f, RFM=%f, LBM=%f, RBM=%f", LFM, RFM, LBM, RBM)
    else:
        rospy.logwarn("Received array does not have enough elements.")

def array_subscriber():
    rospy.init_node('array_subscriber', anonymous=True)

    # Create a subscriber to the "my_array" topic with Float32MultiArray type
    rospy.Subscriber("cmd_vel", Float64MultiArray, callback)

    # Spin to keep the node alive
    rospy.spin()

if __name__ == '__main__':
    array_subscriber()
