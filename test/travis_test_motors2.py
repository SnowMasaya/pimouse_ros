#!/usr/bin/env python
#encoding: utf8
import unittest, rostest
import rosnode, rospy
import time
from pimouse_ros.msg import MotorFreqs
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse

class MotorTest(unittest.TestCase):
    def setUp(self):
        rospy.write_for_service('/motor_on')
        rospy.write_for_service('/motor_off')
        on = rospy.ServiceProxy('/motor_on', Trigger)
        ret = ont()
   
    def test_on_off(self):
        off = rospy.ServiceProxy('/motor_off', Trigger)
        ret = off()
        self.assertEqual(ret.success, True, 'motor off does not succeded')
        self.assertEqual(ret.message, "OFF", 'motor off wrong message')
        with open('/dev/rtmotoren0', "r") as f:
            data = f.readline()
            self.assertEqual(data, '0\n', 'wrong value in rtmotor0 at motor off')
            
        off = rospy.ServiceProxy('/motor_on', Trigger)
        ret = off()
        self.assertEqual(ret.success, True, 'motor on does not succeded')
        self.assertEqual(ret.message, "ON", 'motor on wrong message')
        with open('/dev/rtmotoren0', "r") as f:
            data = f.readline()
            self.assertEqual(data, '1\n', 'wrong value in rtmotor0 at motor on')


if __name__ == '__main__':
    rospy.init_node('travis_test_motors')
    rostest.rosrun('pimouse_ros','travis_test_motors', MotorTest)
