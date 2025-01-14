# -*- encoding=utf8 -*-
__author__ = "Mengjie"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
#poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

# 本shell对应的测试用例：
# https://nutriu.atlassian.net/browse/CH-2801 (Lamp light control - Set light show Ambient light mode)
# https://nutriu.atlassian.net/browse/CH-2802（Lamp light control - Set light show AQI colour mode）
# https://nutriu.atlassian.net/browse/CH-2803（Lamp light control - Set light show off mode）

#启动Air+ app
start_app("com.philips.ph.homecare")
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")
# 进入设备控制页面
poco(desc="https://air-matters.com/app/philips/dark_mode/AC3420_10.png").click()
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([-0.0213, -0.6634])

# https://nutriu.atlassian.net/browse/CH-2801
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco(text="Ambient").click()
poco(text="Apply").click()
assert_exists(Template(r"tpl1736234052490.png", threshold=0.98, record_pos=(-0.186, 0.105), resolution=(1080, 2412)), "灯光模式显示Ambient")

# https://nutriu.atlassian.net/browse/CH-2802
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco(text="Air Quality").click()
poco(text="Apply").click()
assert_exists(Template(r"tpl1736234247234.png", threshold=0.98, record_pos=(-0.201, 0.102), resolution=(1080, 2412)), "灯光模式显示Air Quality")

# https://nutriu.atlassian.net/browse/CH-2803
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco(text="Off").click()
poco(text="Apply").click()
assert_exists(Template(r"tpl1736234350681.png", threshold=0.98, record_pos=(-0.194, 0.105), resolution=(1080, 2412)), "灯光模式显示Off")
# 返回app主页
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([0.0213, 0.6634])
poco(desc="Navigate up").click()








 