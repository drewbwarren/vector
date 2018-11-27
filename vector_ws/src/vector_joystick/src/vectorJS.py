#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy

class vectorJSParser:


    def __init__(self):

        self.joy = Joy()
        self.joy_sub = rospy.Subscriber('/joy', Joy, self.joy_cb)


    def joy_cb(self,joy):
        print(joy.buttons)


if __name__ == '__main__':

    rospy.init_node('vectorJoystick')

    vecJS = vectorJSParser()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Shutting down')