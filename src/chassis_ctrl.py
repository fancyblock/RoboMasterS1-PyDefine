
def set_pwm_value(pwm_port_enum, output_percent):
    """
    设置 PWM 输出百分比，数值越大，在某一周期内高电平的持续时间越长。该 PWM 基础频率为50Hz
    output_percent(int): [0, 100]
    """
    pass


def enable_stick_overlay():
    """
    开启底盘速度杆量叠加
    """
    pass


def disable_stick_overlay():
    """
    关闭底盘速度杆量叠加
    """
    pass


def set_follow_gimbal_offset(degree):
    """
    在“底盘跟随云台模式”下，当云台左右旋转时，底盘始终与云台保持指定夹角
    degree(int): [-180, 180]°
    """
    pass


def set_trans_speed(speed):
    """
    设置底盘平移速率，默认平移速率是 0.5 米/秒。数值越大，移动越快。
    speed(float): [0, 3.5] m/s
    """
    pass


def set_rotate_speed(speed):
    """
    设置底盘旋转速率，默认旋转速率是 30 度/秒。数值越大，旋转越快。
    speed(int): [0, 600] °/s
    """
    pass


def set_wheel_speed(lf_speed, rf_speed, lr_speed, rr_speed):
    """
    独立控制四个麦轮的转速，符合麦轮转动方向和速度的有效组合才会生效。
    lf_speed(int): [-1000, 1000] rpm
    rf_speed(int): [-1000, 1000] rpm
    lr_speed(int): [-1000, 1000] rpm
    rr_speed(int): [-1000, 1000] rpm
    """
    pass


def move(degree):
    """
    控制底盘向指定方向平移
    degree (int): [-180, 180] °
    """
    pass


def move_with_time(degree, time):
    """
    控制底盘向指定方向平移指定时长
    degree(int): [-180, 180] °
    time(float): [0, 20] s
    """
    pass


def move_with_distance(degree, distance):
    """
    控制底盘向指定方向平移指定距离
    degree(int): [-180, 180] °
    distance(float): [0, 5] m
    """
    pass


def move_degree_with_speed(speed, degree):
    """
    控制底盘以指定的平移速率向指定方向平移
    speed(float): [0, 3.5] m/s
    degree(int): [-180, 180] °
    """
    pass


def rotate(direction_enum):
    """
    控制底盘向指定方向旋转
    """
    pass


def rotate_with_time(direction_enum, time):
    """
    控制底盘向指定方向旋转指定时长
    time(float): [0, 20] s
    """
    pass


def rotate_with_degree(direction_enum, degree):
    """
    控制底盘向指定方向旋转指定角度
    degree(int): [0, 1800] °
    """
    pass


def move_and_rotate(degree, direction):
    """
    控制底盘向指定方向平移的同时做旋转运动
    degree(int): [-180, 180] °
    """
    pass


def move_with_speed(speed_x, speed_y, speed_rotation):
    """
    控制底盘以指定速度在指定方向运动
    speed_x(float): [0, 3.5] m/s
    speed_y(float): [0, 3.5] m/s
    speed_rotation(int): [-600, 600] °/s
    """
    pass


def stop():
    """
    停止底盘的所有运动
    """
    pass


def get_attitude(attitude_enum):
    """
    以上电时刻底盘位置为基准，获取底盘当前在航向轴、俯仰轴或翻滚轴上的姿态角值
    Return value:
     degree(float)
    """
    pass


def get_position_based_power_on(action_enum):
    """
    获取底盘当前位置的坐标和朝向数据
    Return value:
     position(float)
    """
    pass


def is_impact():
    """
    在行驶过程中，检测到底盘撞击到人、桌腿等障碍物时会返回“真”，否则返回“假”
    """
    pass


"""
在行驶过程中，当底盘撞击到人、桌腿等障碍物时，运行本模块内程序
def chassis_impact_detection(msg)
"""
