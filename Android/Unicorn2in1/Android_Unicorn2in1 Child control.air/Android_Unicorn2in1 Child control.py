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
# https://nutriu.atlassian.net/browse/CH-269（Timer - check device and app icon）（16-26）
# https://nutriu.atlassian.net/browse/CH-49（Child Lock-Re-power the device）（28-32）

#启动Air+ app
start_app("com.philips.ph.homecare")
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")
# 进入设备控制页面
poco(desc="https://air-matters.com/app/philips/dark_mode/AC3420_10.png").click()
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([-0.0213, -0.6634])
# https://nutriu.atlassian.net/browse/CH-269
poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").click()
assert_equal(poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").attr("checked"),True,"童锁打开成功")
poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").click()
assert_equal(poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").attr("checked"),False,"童锁关闭成功")

# 本shell对应的测试用例：https://nutriu.atlassian.net/browse/CH-49
poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").click()
assert_equal(poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").attr("checked"),True,"童锁打开成功")
# 手动把设备断电后，再上电，检查童锁状态
assert_equal(poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").attr("checked"),False,"童锁关闭成功")
# 返回app主页
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([0.0213, 0.6634])
poco(desc="Navigate up").click()
