#!/usr/bin/env python2.7
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from math import pi
from tf import transformations
from sensor_msgs.msg import Image, JointState
from std_msgs.msg import Float64

joint_position = [0,0,0,0]
gripper_states = [0, 0]

home_position = [-2.8329373416013937e-06, -1.570700117881287, 1.3700000448507081, 0.22579997205473656]

def joint_states_callback(msg):

    global joint_position
    global gripper_states

    for i in range(2, len(msg.position)):
        joint_position[i - 2] = msg.position[i]

    gripper_states[0] = msg.position[0]
    gripper_states[1] = msg.position[1]


def gripper_callback(msg):

    global gripper_states

    gripper_states[0] = msg.position[0]
    gripper_states[1] = msg.position[1]
    

def turn(angle, direction, velocity_publisher, speed = 0.5):

    vel_msg = Twist()

    if direction == 'left':
        vel_msg.angular.z = speed
    else:
        vel_msg.angular.z = -speed

    while not rospy.is_shutdown():

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(abs(current_distance - angle) > 0.005):

            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance = speed*(t1-t0)

        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        break

def move(distance, velocity_publisher, speed = 1.0):

    vel_msg = Twist()

    vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance < distance):
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance= speed*(t1-t0)
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)

        break

def move_back(distance, velocity_publisher, speed = 1.0):

    vel_msg = Twist()

    vel_msg.linear.x = -speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance < distance):
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance= speed*(t1-t0)
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)

        break

def move_arm(joint_goals):

    global joint_position

    joint_pubs = []
    joint_pubs.append(rospy.Publisher('/om_with_tb3/joint1_position/command', \
        Float64, queue_size=5))
    joint_pubs.append(rospy.Publisher('/om_with_tb3/joint2_position/command', \
        Float64, queue_size=5))
    joint_pubs.append(rospy.Publisher('/om_with_tb3/joint3_position/command', \
        Float64, queue_size=5))
    joint_pubs.append(rospy.Publisher('/om_with_tb3/joint4_position/command', \
        Float64, queue_size=5))

    for i in range(len(joint_goals)):
        joint_pub = joint_pubs[i]
        val = Float64()
        val.data = joint_goals[i]
        print(joint_position[i], val.data)
        while not rospy.is_shutdown() and abs(joint_position[i] - joint_goals[i]) \
             > 0.05:
            joint_pub.publish(val)


def open_gripper():

    global gripper_states

    gripper_pub_left = rospy.Publisher('/om_with_tb3/gripper_position/command', \
         Float64, queue_size=5)
    gripper_pub_right = rospy.Publisher('/om_with_tb3/gripper_sub_position/command', \
        Float64, queue_size=5)

    val = Float64()
    val.data = 0.019

    while not rospy.is_shutdown() and abs(gripper_states[0] - 0.019) > 0.005:
        gripper_pub_left.publish(val)
    while not rospy.is_shutdown() and abs(gripper_states[1] - 0.019) > 0.005:
        gripper_pub_right.publish(val)


def close_gripper():

    global gripper_states

    gripper_pub_left = rospy.Publisher('/om_with_tb3/gripper_position/command', \
        Float64, queue_size=5)
    gripper_pub_right = rospy.Publisher('/om_with_tb3/gripper_sub_position/command', \
        Float64, queue_size=5)

    val = Float64()
    val.data = 0.0005
    
    while not rospy.is_shutdown() and abs(gripper_states[0] - val.data) > 0.005:
        gripper_pub_left.publish(val)
    while not rospy.is_shutdown() and abs(gripper_states[1] - val.data) > 0.005:
        gripper_pub_right.publish(val)



def move_arm_to_object(item, pick_up = True, speed = 0.5):

    if pick_up:
        open_gripper()

    if item == 1:

        move_arm([0,-1.57,0.3,0])
        rospy.sleep(0.5)
        move_arm([0,0.55,0.3,0])
        rospy.sleep(0.5)

    if pick_up:
        close_gripper()
    else:
        open_gripper


def retrieve(item, velocity_publisher, speed = 0.5):

    move_arm(home_position)

    if item == 1:
        move(0.95, velocity_publisher)

    rospy.sleep(0.4)

    move_arm_to_object(item)
    move_arm(home_position)

    rospy.sleep(0.5)

    if item == 1:
        move_back(0.7, velocity_publisher)

    move_arm_to_object(1, pick_up=False)

    move_arm(home_position)


def main():

    global home_position

    rospy.init_node('robot', anonymous=True)

    joint_states_sub = rospy.Subscriber('om_with_tb3/joint_states', \
        JointState, joint_states_callback)

    velocity_publisher = rospy.Publisher('/om_with_tb3/cmd_vel', Twist, queue_size=10)

    retrieving = True

    while retrieving: 

        print('enter a number (0: done, 1: coke can)')
        item = int(input())
        # print(item)
        if item == 0:
            break
        elif item in range(2):
            retrieve(item, velocity_publisher)
        else:
            print('enter a valid object')


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass