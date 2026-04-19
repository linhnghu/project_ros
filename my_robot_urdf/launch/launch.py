import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Khai báo các đường dẫn
    package_name = 'my_robot_urdf'
    pkg_share = get_package_share_directory(package_name)
    urdf_file = os.path.join(pkg_share, 'urdf', 'rv2.urdf')
    rviz_config_file = os.path.join(pkg_share, 'my_robot_urdf', 'urdf.rviz')
    
    # 2. Đọc nội dung file URDF
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    # --- SỬA LỖI ĐƯỜNG DẪN CRASH GAZEBO ---
    robot_desc = robot_desc.replace('$(find my_robot_urdf)', pkg_share)
    # -----------------------------------------------------

    # 3. Fix GAZEBO_MODEL_PATH
    pkg_parent = os.path.abspath(os.path.join(pkg_share, ".."))
    set_gazebo_model_path = SetEnvironmentVariable(
        name='GAZEBO_MODEL_PATH',
        value=pkg_parent
    )

    # 4. Robot State Publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
    )

    # 5. Gazebo
    gazebo_launch_file = os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch_file),
    )

    # 6. Spawn Robot
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'robot_rv2', '-topic', 'robot_description'],
        output='screen'
    )

    # 7. Khởi chạy các Controller từ ros2_control
    load_joint_state_broadcaster = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
        output="screen",
    )

    load_arm_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["arm_controller"],
        output="screen",
    )

    # 8. Chạy RViz2
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        parameters=[{'use_sim_time': True}],
        arguments=['-d', rviz_config_file]
    )

    # 9. Khởi chạy Node điều khiển tay máy (Cửa sổ Terminal 1)
    arm_commander_node = Node(
        package='my_robot_urdf',
        executable='arm_commander.py', 
        name='arm_commander',
        output='screen',
        parameters=[{'use_sim_time': True}],
        prefix=['gnome-terminal -- '] 
    )

    # 10. Khởi chạy Node điều khiển di chuyển Teleop (Cửa sổ Terminal 2)
    teleop_node = Node(
        package='my_robot_urdf',
        executable='teleop.py',  # Nhớ đổi tên này nếu bạn lưu file tên khác nhé!
        name='teleop',
        output='screen',
        parameters=[{'use_sim_time': True}],
        prefix=['gnome-terminal -- '] 
    )

    return LaunchDescription([
        set_gazebo_model_path,
        robot_state_publisher,
        gazebo,
        spawn_robot,
        load_joint_state_broadcaster, 
        load_arm_controller,          
        rviz_node,
        arm_commander_node,
        teleop_node  # <--- Đã thêm Node Teleop vào Launch
    ])
