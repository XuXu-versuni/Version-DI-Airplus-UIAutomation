
# -*- encoding=utf8 -*-

""" 
@time :    2024/11/08  14:52 
@File:     Prometheus device power on&off and mode control_python.py 
@Software: PyCharm 
@Author :  xfdzl 
@Version:  python3.7 
"""  



def start_app(app_id):
    print(f"启动应用: {app_id}")

def assert_equal(expected, actual, message):
    if expected == actual:
        print(f"断言成功: {message}")
    else:
        print(f"断言失败: {message}, 预期值为 {expected}, 实际值为 {actual}")

def click_element(element_id):
    print(f"点击元素: {element_id}")

def swipe(start_x, start_y, end_x, end_y):
    print(f"滑动操作: 从 ({start_x}, {start_y}) 到 ({end_x}, {end_y})")

def assert_exists(template_path, threshold, message):
    print(f"验证图像存在: {template_path}, 阈值为 {threshold}, {message}")

# 启动Air+ app
start_app("com.philips.ph.homecare")

# 模拟点击操作
click_element("com.philips.ph.homecare:id/dashboard_section_title")

# 模拟滑动操作
swipe(806, 1814, 809, 449)

# 模拟模式设置
click_element("com.philips.ph.homecare:id/philips_control_power_btn_id")
assert_equal("预期值", "实际值", "打开成功")

# 模拟设置Auto mode
click_element("com.philips.ph.homecare:id/philips_control_auto_btn_id")
click_element("Auto")
click_element("com.philips.ph.homecare:id/dialog_control_sheet_apply")
assert_exists("tpl1730874755774.png", 0.95, "Auto mode设置成功")

# 请注意，以上代码仅为示例，实际的自动化操作需要依赖于第三方库。# 导入必要的库
import time
from airtest.core.api import start_app, assert_equal, exists, sleep, device
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# poco初始化
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# 自动设置环境
auto_setup(__file__)

# 启动Air + app
start_app("com.philips.ph.homecare")
try:
    assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(), "My Devices", "app打开成功")
    # 进入设备控制页面
    poco(desc="https://air - matters.com/app/philips/dark_mode/CX3120_01.png").click()
    device().swipe([806, 1814], [809, 449])
    assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(), "Temperature around device", "控制页面进入成功")

    # Prometheus设备的打开和关闭功能
    # 关闭功能
    poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
    time.sleep(2.0)
    assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"), False, "关闭成功")

    # 打开功能
    poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
    assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"), True, "打开成功")

    # 设置Auto mode
    poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
    poco(text="Auto").click()
    poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
    # 阈值根据机型适配，注意修改你本地的阈值
    assert exists(Template(r"tpl1730874755774.png", threshold=0.95, record_pos=(-0.206, 0.354), resolution=(1080, 2412))), "Auto mode设置成功"

    # 设置High mode
    poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
    poco(text="High").click()
    poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
    # 阈值根据机型适配
    assert exists(Template(r"tpl1730875036187.png", threshold=0.95, record_pos=(-0.191, 0.278), resolution=(1080, 2412))), "High mode设置成功"

    # 设置Low mode
    poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
    poco(text="Low").click()
    poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
    # 阈值根据机型适配
    assert exists(Template(r"tpl1730875222501.png", threshold=0.98, record_pos=(-0.194, 0.289), resolution=(1080, 2412))), "Low mode设置成功"

    # 设置Medium mode
    poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
    poco(text="Medium").click()
    poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
    # 阈值根据机型适配
    assert exists(Template(r"tpl1730875392422.png", threshold=0.98, record_pos=(-0.194, 0.283), resolution=(1080, 2412))), "Medium mode设置成功"

    # 设置Ventilation mode
    poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
    poco(text="Ventilation").click()
    poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
    # 阈值根据机型适配
    assert exists(Template(r"tpl1730880379003.png", threshold=0.98, record_pos=(-0.206, 0.623), resolution=(1080, 2412))), "Ventilation mode设置成功"
except Exception as e:
    print("测试过程中出现错误:", e)