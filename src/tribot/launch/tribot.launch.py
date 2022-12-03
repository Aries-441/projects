'''
FileName: 
Description: 
Autor: Liujunjie/Aries-441
StudentNumber: 521021911059
Date: 2022-11-18 17:03:37
E-mail: sjtu.liu.jj@gmail.com/sjtu.1518228705@sjtu.edu.cn
LastEditTime: 2022-12-03 18:32:47
'''
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from scripts import GazeboRosPaths

def generate_launch_description():
 
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    urdf_file_name = 'urdf/tribot_description.urdf'

    #print("urdf_file_name : {}".format(urdf_file_name))

    urdf = os.path.join(
        get_package_share_directory('tribot'),
        urdf_file_name)
    return LaunchDescription([

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
            
        #ExecuteProcess(
           #cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
           #output='screen'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=[urdf]),

        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}]
            ),
 
        #Node(
            #package='gazebo_ros',
            #executable='spawn_entity.py',
            #name='urdf_spawner',
            #utput='screen',
            #arguments=["-topic", "/robot_description","/joint_state_publisher"
            #"-entity", "tribot", "-x", "0.0", "-y", "0.0", "-z", "0.0"],
            #arguments=["-topic", "robot_description", "-entity", "robot", "-x", "0.0", "-y", "0.0", "-z", "0.0"],
            #arguments=["-entity","irb52urdf","-b","-file", urdf,],
            
            #)
  ])