#!/usr/bin/python3

import rospy
from std_msgs.msg import String

def call_back(msg):
    rospy.loginfo(msg.data)

def listener():
    rospy.init_node("RAA24_s")
    rospy.Subscriber("Greetings",String,callback=call_back)
    rospy.spin()

if __name__ == "__main__" :
    listener()
    