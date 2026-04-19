# project_ros2
25	Nguyễn Văn Linh	23020749	Rotation 	Rotation	LiDAR, IMU, Encoder	Omnidirectional (mecanum, 4 bánh)

Cài đặt
Dự án này là một package ROS 2 độc lập. Bạn có thể dễ dàng thêm nó vào workspace hiện tại của mình.

1. Tạo workspace (nếu bạn chưa có sẵn):

Bash```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
2. Clone package:

Bash
git clone [URL_REPO_CỦA_BẠN]
3. Cài đặt các thư viện phụ thuộc:

Bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
4. Build package:
Vì đây là một package đơn lẻ, bạn có thể chỉ định build đúng package này để tiết kiệm thời gian (thay [tên_package_của_bạn] bằng tên thư mục package):

Bash
colcon build --packages-select [tên_package_của_bạn] --symlink-install
5. Source môi trường:

Bash
source install/setup.bash
