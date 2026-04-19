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
git clone gh repo clone linhnghu/project_ros
```
3. Cài đặt các thư viện phụ thuộc:

```
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
```
4. Build package:

```
colcon build --packages-select my_robot_urdf --symlink-install
```
5. Source môi trường:

```
source install/setup.bash
```
6. Chạy file launch

```
ros2 launch my_robot_urdf launch.py
```
