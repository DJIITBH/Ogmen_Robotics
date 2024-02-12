import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node



def generate_launch_description():


    
    rviz= Node(name = 'rviz',package='rviz2', executable='rviz2',output='screen')

     

    


    # Launch them all!
    return LaunchDescription([
       rviz,
    ])