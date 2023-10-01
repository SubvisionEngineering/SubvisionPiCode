#!/usr/bin/env python

import rospy
import pigpio
from geometry_msgs.msg import Twist

class thruster:
    def thrusting(self, pi):
        rospy.init_node('thrust')
        rospy.Subscriber('cmd_vel', Twist, self.PWM_velocity)

        self.thrust_pins = [] #gpio PWM
    
        self.pi = pigpio.pi()

        self.pwm_range = #range
        self.pwm_freq = #freq
    
        # PWM duty cycle is now thrust
        self.thrust = self.pi.set_PWM_dutycycle

        # initialize PWM for each thruster
        for pin in self.thrust_pins:
            self.pi.set_mode(pin, pigpio.OUTPUT)
            self.pi.set_PWM_range(pin, self.pwm_range)
            self.pi.set_PWMfreq(pin, self.pwm_freq)
            self.pi.set_PWM_dutycycle(pin, 0)

    def PWM_velocity(self, twist_data):
        # taking linear and angular vel
        linear_x = twist_data.linear.x
        #linear_y = twist_data.lienar.y

        thrust_speed = linear_x
    
        # map thruster speed to PWM values within range of [0, self.pwm_range]
        pwm_values = [self.map_to_pwm(speed) for speed in thrust_speed]

        # setting PWM values for each thruster
        for i, pin in enumerate(self.thrust_pins):
            self.thrust(pin, pwm_values[i])

    def PWM_map(self, speed):
        # Map speed to PWM value within range [0, self.pwm_range]
        pwm = int((speed + 1) * (self.pwm_range / 2))
        return max(0, min(self.pwm_range, pwm))

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        controller = thruster()
        controller.run()
    except rospy.ROSInterruptException:
        pass
