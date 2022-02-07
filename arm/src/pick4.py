#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("ARM")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size = 20)


#group.set_planner_id("RRTConnectkConfigDefault")
#group.set_planning_time(20.0)
pose_target = geometry_msgs.msg.Pose()
#pose_target.orientation.w = 1.0
pose_target.position.x = 0.1
pose_target.position.y = 0.0
pose_target.position.z = 0.3

plan1 = group.plan()
if not plan1.joint_trajectory.points:
	rospy.loginfo("not reachable!!")
else:
	rospy.loginfo("reachable!!")
	group.set_pose_target(pose_target)

#group.set_named_target("PICK")

plan1 = group.plan()
group.go(wait=True)


rospy.sleep(5)
moveit_commander.roscpp_shutdown()
