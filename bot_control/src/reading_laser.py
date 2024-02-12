#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LaserFilterNode(Node):

    def __init__(self):
        super().__init__('laser_filter_node')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',  # Replace with the actual laser scan topic
            self.laser_scan_callback,
            10  # Adjust the queue size as needed
        )
        self.publisher_ = self.create_publisher(LaserScan, '/filtered_scan', 10)

    def laser_scan_callback(self, msg):
        # Extract the ranges from the LaserScan message
        ranges = msg.ranges
        for i in range(len(ranges)):
            if i >=0 and i <=60:
                continue
            elif i<=360 and i>=300:
                continue
            ranges[i] = 0.0
        
        filtered_data=ranges
        # print(filtered_data)
        
        # exit(0)
        # Create a new LaserScan message for the filtered data
        filtered_scan_msg = LaserScan()
        filtered_scan_msg.header = msg.header
        filtered_scan_msg.angle_min = 0.0
        filtered_scan_msg.angle_max = 120.0 * (3.14159265359 / 180.0)
        filtered_scan_msg.angle_increment = msg.angle_increment
        filtered_scan_msg.time_increment = msg.time_increment
        filtered_scan_msg.scan_time = msg.scan_time
        filtered_scan_msg.range_min = msg.range_min
        filtered_scan_msg.range_max = msg.range_max
        filtered_scan_msg.ranges = filtered_data
        filtered_scan_msg.intensities=msg.intensities
        

        # Publish the filtered scan data to /filtered_scan topic
        self.publisher_.publish(filtered_scan_msg)

def main(args=None):
    rclpy.init(args=args)
    laser_filter_node = LaserFilterNode()
    rclpy.spin(laser_filter_node)
    laser_filter_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

