#!/usr/bin/env python

PACKAGE = 'transforms'
import roslib;roslib.load_manifest(PACKAGE)
import rospy

from dynamic_reconfigure.server import Server
from transforms.cfg import TransformConfig
import tf
import tfx

class Broadcaster:
    
    def __init__(self, br):
        self.config = None
        self.srv = Server(TransformConfig, self.callback)
        self.br = br

    def callback(self, config, level):
        self.config = config
        return config

    def broadcast(self):
        if not self.config:
            return
        config = self.config
        self.br.sendTransform((config.x, config.y, config.z),
                         tfx.tb_angles(config.yaw, config.pitch, config.roll).quaternion,
                         rospy.Time.now(),
                         '/left_optical_frame',
                         '/world')

if __name__ == "__main__":
    rospy.init_node("transform_server")
    br = tf.TransformBroadcaster()

    bc = Broadcaster(br)
    r = rospy.Rate(100)
    while not rospy.is_shutdown():
        bc.broadcast()
        r.sleep()
