# -*- coding: utf-8 -*-  
""" 
@time :    2024/10/30  14:02 
@File:     Pegasus clrculation function under switch fun and oscillation_python.py 
@Software: PyCharm 
@Author :  xfdzl 
@Version:  python3.7 
"""  
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import logging

# 初始化日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

# 定义常量
POWER_BUTTON_ID = "com.philips.ph.homecare:id/philips_control_power_btn_id"
CHILD_LOCK_BUTTON_ID = "com.philips.ph.homecare:id/philips_control_childlock_btn_id"
LIGHT_MODE_BUTTON_ID = "com.philips.ph.homecare:id/philips_control_light_mode_btn_id"
HUMIDITY_BUTTON_ID = "com.philips.ph.homecare:id/philips_control_humidity_btn_id"
APPLY_BUTTON_ID = "com.philips.ph.homecare:id/dialog_control_sheet_apply"
AUTO_BUTTON_ID = "com.philips.ph.homecare:id/philips_control_auto_btn_id"
SHEET_PICKER_ID = "com.philips.ph.homecare:id/philips_control_sheet_picker"

# 设备标识
DEVICE_TEXT = "mengjie"
DEVICE_DESC = "https://air-matters.com/app/philips/dark_mode/AMF870_15.png"

# 进入控制页面
def enter_control_page():
    logger.info("Entering control page...")
    # 选择特定设备
    device_node = poco(desc=DEVICE_DESC, text=DEVICE_TEXT)
    if not device_node.exists():
        logger.error(f"Device with desc '{DEVICE_DESC}' and text '{DEVICE_TEXT}' not found.")
        raise Exception(f"Device with desc '{DEVICE_DESC}' and text '{DEVICE_TEXT}' not found.")
    device_node.click()

# 模式切换
def switch_mode(mode_name, template_path):
    logger.info(f"Switching to {mode_name} mode...")
    poco(AUTO_BUTTON_ID).click()
    poco(text=mode_name).click()
    sleep(3.0)
    poco(APPLY_BUTTON_ID).click()
    assert_exists(Template(template_path, record_pos=(0.012, 0.547), resolution=(1080, 2412)), f"{mode_name}模式切换成功")
    sleep(3.0)

# 灯光模式切换
def switch_light_mode(mode_name, template_path):
    logger.info(f"Switching to {mode_name} light mode...")
    poco(LIGHT_MODE_BUTTON_ID).click()
    poco(f"com.philips.ph.homecare:id/dialog_control_sheet_lamp_{mode_name.lower()}").click()
    poco(APPLY_BUTTON_ID).click()
    assert_exists(Template(template_path, threshold=0.98, record_pos=(-0.208, 0.695), resolution=(1080, 2412)), f"{mode_name}切换成功")
    sleep(3.0)

# 灯光亮度切换
def switch_light_brightness(brightness, template_path):
    logger.info(f"Switching to {brightness} brightness...")
    poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
    poco(text=brightness).click()
    poco(APPLY_BUTTON_ID).click()
    assert_exists(Template(template_path, threshold=0.98, record_pos=(-0.211, 0.781), resolution=(1080, 2412)), f"灯光切换为{brightness}成功")
    sleep(3.0)

# 目标湿度控制
def set_target_humidity(humidity, template_path):
    logger.info(f"Setting target humidity to {humidity}%...")
    poco(HUMIDITY_BUTTON_ID).click()
    if humidity == 30:
        poco(SHEET_PICKER_ID).swipe([0.5, 0.5])
    elif humidity == 35:
        poco(SHEET_PICKER_ID).swipe([-0.008, -0.0287])
    # 可以继续添加更多的湿度设置逻辑
    poco(APPLY_BUTTON_ID).click()
    assert_exists(Template(template_path, threshold=0.98, record_pos=(0.209, 0.706), resolution=(1080, 2412)), f"目标湿度{humidity}%切换成功")
    sleep(3.0)

# 主函数
def main():
    try:
        enter_control_page()

        # 上下滑动屏幕
        poco("com.philips.ph.homecare:id/philips_control_layout_id").swipe([-0.0539, -0.5587])
        poco("com.philips.ph.homecare:id/philips_control_layout_id").swipe([-0.0488, 0.8438])
        poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([-0.1412, -0.2345])
        sleep(3.0)

        # 设备关机控制
        poco(POWER_BUTTON_ID).click()
        assert_equal(poco(POWER_BUTTON_ID).attr("checked"), False, msg="设备关机.")
        sleep(3.0)

        # 设备开机控制
        poco(POWER_BUTTON_ID).click()
        assert_equal(poco(POWER_BUTTON_ID).attr("checked"), True, msg="设备开机.")

        # 童锁打开控制
        poco(CHILD_LOCK_BUTTON_ID).click()
        assert_equal(poco(CHILD_LOCK_BUTTON_ID).attr("checked"), True, msg="童锁打开.")
        sleep(3.0)

        # 童锁关闭控制
        poco(CHILD_LOCK_BUTTON_ID).click()
        assert_equal(poco(CHILD_LOCK_BUTTON_ID).attr("checked"), False, msg="童锁关闭.")

        # 模式切换
        switch_mode("Auto", r"tpl1726731182521.png")
        switch_mode("Sleep", r"tpl1726731452159.png")
        switch_mode("Medium", r"tpl1726731497712.png")
        switch_mode("High", r"tpl1726731551102.png")

        # 灯光模式切换
        switch_light_mode("Humidity", r"tpl1726731828009.png")
        switch_light_mode("Warm", r"tpl1726731935717.png")
        switch_light_mode("Dawn", r"tpl1726731985254.png")
        switch_light_mode("Calm", r"tpl1726732012578.png")
        switch_light_mode("Breath", r"tpl1726732052079.png")
        switch_light_mode("Off", r"tpl1726732109040.png")

        # 灯光亮度切换
        switch_light_brightness("Bright", r"tpl1726732266066.png")
        switch_light_brightness("Low", r"tpl1726732335858.png")
        switch_light_brightness("Off", r"tpl1726732379261.png")

        # 目标湿度控制
        set_target_humidity(30, r"tpl1726732810609.png")
        set_target_humidity(35, r"tpl1729663414303.png")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()