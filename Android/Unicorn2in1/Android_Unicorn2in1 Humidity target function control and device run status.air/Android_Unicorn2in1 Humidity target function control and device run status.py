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
# https://nutriu.atlassian.net/browse/CH-3503 (Unicorn2in1 - Humidity target function control and device run status)

#启动Air+ app
start_app("com.philips.ph.homecare")
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")
# 进入设备控制页面
poco(desc="https://air-matters.com/app/philips/dark_mode/AC3420_10.png").click()
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([-0.0213, -0.6634])

# https://nutriu.atlassian.net/browse/CH-3503
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco(text="40%").click()
poco(text="Apply").click()
assert_exists(Template(r"tpl1736235067422.png", threshold=0.98, record_pos=(0.217, -0.046), resolution=(1080, 2412)), "目标湿度显示40%")
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco(text="50%").click()
poco(text="Apply").click()
assert_exists(Template(r"tpl1736235215291.png", threshold=0.98, record_pos=(0.221, -0.048), resolution=(1080, 2412)), "目标湿度显示50%")
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco(text="60%").click()
poco(text="Apply").click()
assert_exists(Template(r"tpl1736235288503.png", threshold=0.98, record_pos=(0.227, -0.042), resolution=(1080, 2412)), "目标湿度显示60%")
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco(text="70%").click()
poco(text="Apply").click()
assert_exists(Template(r"tpl1736235348670.png", threshold=0.98, record_pos=(0.228, -0.046), resolution=(1080, 2412)), "目标湿度显示70%")











