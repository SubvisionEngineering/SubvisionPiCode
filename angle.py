#!/usr/bin/env python3

import rospy
import pigpio
import time
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import String

pwm_pin1 = 25   # pin 22    left front thruster
pwm_pin2 = 18   # pin 12    right front thruster
pwm_pin3 = 23   # pin 16    left back thruster
pwm_pin4 = 24   #pin 18     right back thruster
pwm_pin5 = 27   #pin 13     right up thruster
pwm_pin6 = 22   #pin 15     left up thruster
pwm_pin7 = 7    # pin 26    clamp servo

pi = pigpio.pi()
# Set the pulse width range for the servo (in microseconds)
pulse_width_min = 500  # Minimum pulse width for 0 degrees
pulse_width_max = 2500  # Maximum pulse width for 180 degrees

def move_servo(degrees):
    pulse_width = int((float(degrees) / 180.0) * (pulse_width_max - pulse_width_min) + pulse_width_min)
    pi.set_servo_pulsewidth(servo_pin, pulse_width) 
    time.sleep(0.5)  # Adjust delay as needed


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
        RM = 150 * Thrust_data[4] + 1500 
        LM = 150 * Thrust_data[4] + 1500 

        LFM_PWM = int(LFM)
        RFM_PWM = int(RFM)
        LBM_PWM = int(LBM)
        RBM_PWM = int(RBM)
        RM_PWM = int(RM)
        LM_PWM = int(LM)
    
        pi.set_servo_pulsewidth(pwm_pin1, LFM_PWM)
        pi.set_servo_pulsewidth(pwm_pin2, RFM_PWM)
        pi.set_servo_pulsewidth(pwm_pin3, LBM_PWM)
        pi.set_servo_pulsewidth(pwm_pin4, RBM_PWM)
        pi.set_servo_pulsewidth(pwm_pin5, RM_PWM)
        pi.set_servo_pulsewidth(pwm_pin6, LM_PWM)

        # Process and use the separate variables as needed
        rospy.loginfo("Received values: LFM=%f, RFM=%f, LBM=%f, RBM=%f, LM=%f, RM=%f", LFM_PWM, RFM_PWM, LBM_PWM, RBM_PWM, RM, LM)
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

