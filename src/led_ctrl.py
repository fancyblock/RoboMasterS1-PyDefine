
def set_flash(armor_enum, frequency):
    """
    设置指定位置LED灯闪烁频率
    frequency(int): [1, 10]
    """
    pass


def set_bottom_led(armor_enum, r, g, b, led_effect_enum):
    """
    控制底盘指定位置LED灯的颜色和灯效
    r(int): [0, 255]
    g(int): [0, 255]
    b(int): [0, 255]
    """
    pass


def set_top_led(armor_enum, r, g, b, led_effect_enum):
    """
    设置云台指定位置 LED 灯的颜色和灯效
    """
    pass


def set_signle_led(armor_enum, led_index, led_effect_enum):
    """
    设置云台指定序号 LED 灯的亮灭，序号 1～8 分别对应云台两侧可独立控制的 8 颗 LED 灯
    index(int/list): [1, 8]
    """
    pass


def turn_off(armor_enum):
    """
    关闭指定位置的LED灯
    """


def gun_on():
    """
    开启发射器弹道灯
    """
    pass


def gun_off():
    """
    关闭gun_off
    """
    pass
