#include <ros/ros.h>

#include <dynamic_reconfigure/server.h>
#include <transforms/TransformConfig.h>

void callback(transforms::TransformConfig &config, uint32_t level) {
    ROS_INFO("x: %f", config.x);
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "transforms");

  dynamic_reconfigure::Server<transforms::TransformConfig> server;
  dynamic_reconfigure::Server<transforms::TransformConfig>::CallbackType f;

  f = boost::bind(&callback, _1, _2);
  server.setCallback(f);

  ROS_INFO("Spinning node");
  ros::spin();
  return 0;
}
