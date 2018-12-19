# Copied from uos / ceres_robot / ceres_navigation om 19/12/2018

import rospy
import smach
import time

from geometry_msgs.msg import PoseStamped


class WaitForGoal(smach.State):
    def __init__(self):
        smach.State.__init__(
            self,
            outcomes=['succeeded', 'preempted'],
            output_keys=['target_pose'])
        self._global_target_pose = PoseStamped()
        self._subscriber = None
        self._flag_goal_received = False

    def execute(self, userdata):
        self._flag_goal_received = False
        self._subscriber = rospy.Subscriber('/move_base_simple/goal', PoseStamped, self.goal_callback)

        rate = 0.3
        while not self._flag_goal_received and not rospy.is_shutdown():
            time.sleep(rate)

        userdata.target_pose = self._global_target_pose
        print "Target Pose:", self._global_target_pose.pose.position.x, self._global_target_pose.pose.position.y,\
              self._global_target_pose.pose.position.z
        if rospy.is_shutdown():
          return 'preempted'

        return 'succeeded'

    def goal_callback(self, msg):
        print "Received goal:"
        self._global_target_pose = msg
        self._subscriber.unregister()
        self._flag_goal_received = True