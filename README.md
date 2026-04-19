# project_ros2
25	Nguyễn Văn Linh	23020749	Rotation 	Rotation	LiDAR, IMU, Encoder	Omnidirectional (mecanum, 4 bánh)

Cài đặt
1. Tạo workspace:

```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```
2. Clone package:
```
git clone https://github.com/linhnghu/project_ros
mv ~/ros2_ws/src/project_ros/my_robot_urdf ~/ros2_ws/src/
rm -rf project_ros
```
3. Build package:

```
cd ~/ros2_ws
colcon build --packages-select my_robot_urdf --symlink-install
```
4. Source môi trường:

```
source install/setup.bash
```
5. Chạy file launch

```
ros2 launch my_robot_urdf launch.py
```
