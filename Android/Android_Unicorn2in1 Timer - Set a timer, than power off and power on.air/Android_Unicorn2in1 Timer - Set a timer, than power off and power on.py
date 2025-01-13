# -*- encoding=utf8 -*-
__author__ = "Mengjie"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
#poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

# https://nutriu.atlassian.net/browse/CH-1596（Timer - Set a timer, than power off and power on）

#启动Air+ app
start_app("com.philips.ph.homecare")
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")
# 进入设备控制页面
poco(desc="https://air-matters.com/app/philips/dark_mode/AC3420_10.png").click()
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([-0.0213, -0.6634])

# https://nutriu.atlassian.net/browse/CH-1596
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.0396, -0.0354])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1735873358792.png", threshold = 0.98, record_pos=(0.209, 0.481), resolution=(1080, 2412)), "timer设置时间为1h")
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.0091, 0.0286])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1735873476333.png", threshold = 0.98, record_pos=(0.218, 0.48), resolution=(1080, 2412)), "timer设置为off")
# 返回app主页
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([0.0213, 0.6634])
poco(desc="Navigate up").click()

