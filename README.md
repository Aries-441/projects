<!--
 * @FileName: 
 * @Description: 
 * @Autor: Liujunjie/Aries-441
 * @StudentNumber: 521021911059
 * @Date: 2022-11-13 22:12:15
 * @E-mail: sjtu.liu.jj@gmail.com/sjtu.1518228705@sjtu.edu.cn
 * @LastEditTime: 2022-11-18 13:12:05
-->
# 使用说明
需要四个终端  

终端1：ros2 launch tribot view_tribot_world.launch.py
将小车生成在一个空的世界中。
目前小车的运动学信息可以加载入gazebo，但是模型加载失败，无法可视化

终端2：ros2 run tribot  kinematic
小车的运动学模型节点，根据控制输入和运动学模型，输出在gazebo中的位置。
注意是run，而非launch

终端3：ros2 run tribot tribot_teleop
键盘控制运动节点。
注意是run，而非launch

终端4：rviz或者其他可视化节点

# 更新信息
更新日期作为提交信息

# 环境配置
工作区名称：projects

功能包名字：tribot

urdf文件夹里的路径需要根据个人环境配置改成自己的路径
