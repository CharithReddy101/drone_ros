#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseArray

class Whycon_detect():

	def __init__(self):
		#Initialize a node called whycon_detection
		rospy.init_node('whycon_detection',anonymous=True)
		#Create a python dictionary called whycon_coordinates
		self.whycon_coordinates = {}
		#subscribing to the '/whycon/poses' topic
		rospy.Subscriber('/whycon/poses',PoseArray,self.callback)
		#we are getting the data from subscribed topic which actually gives us the poses of the markers.
	def callback(self,received_data):
		#x1=received_data.poses[0].position.x
		#print x1
		self.whycon=[]
		for i in range(len(received_data.poses)):
			self.whycon.append(["x:","{:.3f}".format(received_data.poses[i].position.x),"Y:", "{:.3f}".format(received_data.poses[i].position.y),"Z:", "{:.3f}".format(received_data.poses[i].position.z)])
			self.whycon_coordinates[i]=self.whycon[i]
		print (self.whycon_coordinates)

if __name__=="__main__":
	marker = Whycon_detect()
	while not rospy.is_shutdown():
		rospy.spin()
