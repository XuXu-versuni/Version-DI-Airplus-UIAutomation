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
# https://nutriu.atlassian.net/browse/CH-1631 (Button beep control - Check button default state)
# https://nutriu.atlassian.net/browse/CH-2827(Beep sound - On/Off )

#启动Air+ app
start_app("com.philips.ph.homecare")
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")
# 进入设备控制页面
poco(desc="https://air-matters.com/app/philips/dark_mode/AC3420_10.png").click()
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([-0.0010, -0.9999])

# https://nutriu.atlassian.net/browse/CH-1631
poco(text="Device Settings").click()
assert_equal(poco("com.philips.ph.homecare:id/philipsSetting_volume_id").attr("checked"),True,"Beep sound默认是打开的状态")

# https://nutriu.atlassian.net/browse/CH-2827
poco(text="Beep sound").click()
assert_equal(poco("com.philips.ph.homecare:id/philipsSetting_volume_id").attr("checked"),False,"Beep sound关闭状态")
poco(text="Beep sound").click()
assert_equal(poco("com.philips.ph.homecare:id/philipsSetting_volume_id").attr("checked"),True,"Beep sound打开状态")
# 返回到app主页
poco(desc="Navigate up").click()
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([0.0213, 0.6634])
poco(desc="Navigate up").click()



