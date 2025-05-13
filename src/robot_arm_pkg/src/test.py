#!/usr/bin/env python3.8

# _*_ coding: utf-8 _*_

# 导入依赖

import sys

import rospy

import moveit_commander

import moveit_msgs.msg

import geometry_msgs.msg

def move_arm_to_grasp_target():

    # 初始化moveit_commander和rospy节点

    moveit_commander.roscpp_initialize(sys.argv)

    rospy.init_node('move_arm_to_grasp', anonymous=True)

    # 初始化需要使用的对象

    group_name = "arm" # 替换为你的机械臂group名称

    group = moveit_commander.MoveGroupCommander(group_name)

    # 设置目标位置

    target_pose = geometry_msgs.msg.Pose()

    target_pose.position.x = 0.12 # 请根据实际情况设置目标位置的x坐标

    target_pose.position.y = 0.41 # 请根据实际情况设置目标位置的y坐标

    target_pose.position.z = 0.44 # 请根据实际情况设置目标位置的z坐标

    # 设置目标姿态

    # target_pose.orientation.w =

    # ... 请根据实际情况设置目标姿态

    # 设置目标姿态

    target_pose.orientation.x = 0.0 # 替换为目标姿态的x分量

    target_pose.orientation.y = 0.0 # 替换为目标姿态的y分量

    target_pose.orientation.z = 0.0 # 替换为目标姿态的z分量

    target_pose.orientation.w = 1.0 # 替换为目标姿态的w分量

    rospy.loginfo(target_pose)

    group.set_pose_target(target_pose)

    # 规划并执行路径

    plan = group.go(wait=True)

    group.stop() # 停止所有剩余的运动

    group.clear_pose_targets()

    # 关闭moveit

    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':

    try:

        move_arm_to_grasp_target()

    except rospy.ROSInterruptException: