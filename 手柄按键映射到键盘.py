import pygame
import time
from pynput.keyboard import Key, Controller
import datetime

# pip install pygame pynput

# 配置映射 - 手柄按键到键盘按键的映射
# 键盘按键参考:
# Key.space: 空格键
# Key.enter: 回车键
# Key.esc: ESC键
# Key.tab: Tab键
# Key.shift: Shift键
# Key.ctrl: Ctrl键
# Key.alt: Alt键
# Key.up: 上箭头
# Key.down: 下箭头
# Key.left: 左箭头
# Key.right: 右箭头
# 'a', 'b', 'c'...: 字母键
# '1', '2', '3'...: 数字键
CONFIG = {
    # 手柄按键映射到键盘按键
    # 格式: "手柄按键": 键盘按键
    # 默认为空，请根据需要自行配置
    "A": None,        # A按钮映射
    "B": None,        # B按钮映射
    "X": None,        # X按钮映射
    "Y": None,        # Y按钮映射
    "UP": None,       # 方向键上映射
    "DOWN": None,     # 方向键下映射
    "LEFT": None,     # 方向键左映射
    "RIGHT": None,    # 方向键右映射
    "START": None,    # Start按钮映射
    "SELECT": None,   # Select按钮映射
    "LB": None,       # LB按钮映射
    "RB": None        # RB按钮映射
}

# 手柄按键索引参考 (基于Xbox控制器)
# 按钮索引 (joystick.get_button(index)):
# 0: A按钮
# 1: B按钮
# 2: X按钮
# 3: Y按钮
# 4: LB按钮(左肩键)
# 5: RB按钮(右肩键)
# 6: SELECT按钮(返回/选择按钮)
# 7: START按钮(开始按钮)
# 8: Xbox/Guide按钮
# 9: 左摇杆按下
# 10: 右摇杆按下
#
# 方向键 (joystick.get_hat(0)):
# (0, 1): 上
# (0, -1): 下
# (-1, 0): 左
# (1, 0): 右
# (1, 1): 右上
# (1, -1): 右下
# (-1, -1): 左下
# (-1, 1): 左上
# (0, 0): 中间/未按下

# 初始化pygame和游戏手柄
pygame.init()
pygame.joystick.init()

# 创建键盘控制器
keyboard = Controller()

def main():
    # 检查是否有游戏手柄连接
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("未检测到游戏手柄，请连接手柄后重试。")
        return
    
    # 初始化第一个检测到的游戏手柄
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"已检测到游戏手柄: {joystick.get_name()}")
    
    # 按钮映射 - 手柄按钮索引到按钮名称的映射
    button_mapping = {
        0: "A",
        1: "B",
        2: "X",
        3: "Y",
        4: "LB",
        5: "RB",
        6: "SELECT",
        7: "START"
    }
    
    # 方向键映射 - 方向键值到方向名称的映射
    hat_mapping = {
        (0, 1): "UP",
        (0, -1): "DOWN",
        (-1, 0): "LEFT",
        (1, 0): "RIGHT"
    }
    
    # 记录按钮状态
    button_states = [False] * joystick.get_numbuttons()
    hat_state = (0, 0)
    
    print("程序已启动，按下手柄按键将检测按键信息...")
    print("请在CONFIG字典中设置按键映射以启用键盘模拟功能")
    print("按Ctrl+C退出程序")
    
    try:
        # 主循环
        while True:
            # 处理事件队列
            pygame.event.pump()
            
            # 检查按钮状态
            for i in range(joystick.get_numbuttons()):
                try:
                    button_pressed = joystick.get_button(i)
                    
                    # 如果按钮状态改变
                    if button_pressed != button_states[i]:
                        button_states[i] = button_pressed
                        
                        # 如果按钮在映射中且被按下
                        if i in button_mapping and button_pressed:
                            button_name = button_mapping[i]
                            print(f"检测到 {button_name} 按钮被按下")
                            
                            # 如果按钮有对应的键盘映射且映射不为None
                            if button_name in CONFIG and CONFIG[button_name] is not None:
                                key = CONFIG[button_name]
                                print(f"模拟键盘按键: {key} " + datetime.datetime.now().strftime("%H:%M:%S"))
                                keyboard.press(key)
                                keyboard.release(key)
                        
                except pygame.error:
                    print("读取手柄按键时出错，请确保手柄仍然连接。")
                    return
            
            # 检查方向键状态
            try:
                current_hat = joystick.get_hat(0)  # 通常只有一个方向键(hat)
                
                # 如果方向键状态改变
                if current_hat != hat_state:
                    hat_state = current_hat
                    
                    # 如果方向键在映射中且不是中间位置
                    if current_hat in hat_mapping:
                        direction = hat_mapping[current_hat]
                        print(f"检测到方向键: {direction}")
                        
                        # 如果方向有对应的键盘映射且映射不为None
                        if direction in CONFIG and CONFIG[direction] is not None:
                            key = CONFIG[direction]
                            print(f"模拟键盘按键: {key} " + datetime.datetime.now().strftime("%H:%M:%S"))
                            keyboard.press(key)
                            keyboard.release(key)
                    
            except pygame.error:
                print("读取方向键时出错，请确保手柄仍然连接。")
                return
            
            # 短暂休眠以减少CPU使用率
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        print("\n程序已退出")
    finally:
        # 清理资源
        pygame.joystick.quit()
        pygame.quit()

if __name__ == "__main__":
    main()
