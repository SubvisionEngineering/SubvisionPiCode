#!/usr/bin/env python3

import rospy
import pigpio
import time
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import String

pwm_pin1 = 25   # pin 22    left front thruster
pwm_pin2 = 18   # pin 12    right front thruster
pwm_pin3 = 23   # pin 16    left back thruster
#pwm_pin4 = 24

pwm_pin5 = 7    # pin 26    clamp servo


def callback(data):
    # Extract the array data from the received message
    global Thrust_data
    Thrust_data = data.data
    
    #do:
        #pi.set_servo_pulsewidth(11, 1500)
        #time.sleep(7)
        #i = 1
    #while i < 1
    
    # Check if the array has at least three elements
    if len(Thrust_data) >= 4:
    # Split the values into separate variables
    # For 10V, keep range between 1250-1750 for 4.5A draw
        LFM = 150 * Thrust_data[0] + 1500
        RFM = 150 * Thrust_data[1] + 1500
        LBM = 150 * Thrust_data[2] + 1500
        RBM = 150 * Thrust_data[3] + 1500
       #RM = 150 * Thrust_data[4] + 1500 
       #LM = 150 * Thrust_data[5] + 1500 

        LFM_PWM = int(LFM)
        RFM_PWM = int(RFM)
        LBM_PWM = int(LBM)
        RBM_PWM = int(RBM)
        #RM_PWM = int(RM)
        #LM_PWM = int(LM)
    
        pi.set_servo_pulsewidth(pwm_pin1, LFM_PWM)
        pi.set_servo_pulsewidth(pwm_pin2, RFM_PWM)
        pi.set_servo_pulsewidth(pwm_pin3, LBM_PWM)
        #pi.set_servo_pulsewidth(pwm_pin4, RBM_PWM)
        #pi.set_servo_pulsewidth(15, RM_PWM)
        #pi.set_servo_pulsewidth(16, LM_PWM)
	        pi.set_servo_

        # Process and use the separate variables as needed
        rospy.loginfo       
        pi.set_servo_("Received values: LFM=%f, RFM=%f, LBM=%f, RBM=%f", LFM_PWM, RFM_PWM, LBM_PWM, RBM_PWM)
    else:
        rospy.logwarn("Received array does not have enough elements.")



def array_subscriber():
    rospy.init_node('angle', anonymous=True)

    if not pi.connected:
        rospy.logerr("uh oh")
        return

    #pi.set_servo_pulsewidth(pwm_pin, 1500)
    #time.sleep(7)
    rospy.Subscriber('cmd_vel', Float64MultiArray, callback)
    
    # Spin to keep the node alive
    rospy.spin()

if __name__ == '__main__':
   # GPIO.setmode(GPIO.BCM)

  
    pi = pigpio.pi()
   # GPIO.setup(pwm_pin, GPIO.OUT)
    array_subscriber()
