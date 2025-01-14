# -*- encoding=utf8 -*-
__author__ = "ytian1"

from airtest.core.api import *
from airtest.core.api import using
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
# element = UIObjectProxy(poco = poco,name = "com.philips.ph.homecare:id/display_theme_auto")
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

#前置条件：已安装Air+ app，已连接Pegasus 3in1设备
#设备信息：Samsung S22 Android 14

#CH-2831 Sensor monitoring in standby - Power off/on

#启动Air+ app
start_app("com.philips.ph.homecare")
#断言当前是否在app主页
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(), "My Devices", "当前在App主页")

#点击app主页Pegasus卡片
poco("com.philips.ph.homecare:id/dashboard_device_name").click()
#断言已进入设备控制页面
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(), "Air Quality", "已进入设备控制页面")

#点击右上角设备设置按钮
poco("com.philips.ph.homecare:id/menu_setting_id").click()
sleep(2)
#断言进入设备设置页面
assert_equal(poco("android.widget.TextView").get_text(), "Settings", "已进入设备设置页面")
#断言sensor monitoring默认状态为关
assert_equal(poco("com.philips.ph.homecare:id/philipsSetting_monitoring_id").attr("checked"),False, "Sensor monitoring状态为关")

#打开sensor monitoring开关
poco("com.philips.ph.homecare:id/philipsSetting_monitoring_id").click()
sleep(3)
#断言sensor monitoring默认状态为开
assert_equal(poco("com.philips.ph.homecare:id/philipsSetting_monitoring_id").attr("checked"),True, "Sensor monitoring状态为开")

#关闭sensor monitoring开关
poco("com.philips.ph.homecare:id/philipsSetting_monitoring_id").click()
sleep(3)
#断言sensor monitoring默认状态为关
assert_equal(poco("com.philips.ph.homecare:id/philipsSetting_monitoring_id").attr("checked"),False, "Sensor monitoring状态为关")

#恢复默认返回app主页
#点击返回按钮，返回到设备控制页面
poco("Navigate up").click()
sleep(3)
#断言已进入设备控制页面
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(), "Air Quality", "已进入设备控制页面")

#点击返回按钮，返回到app主页
poco("Navigate up").click()
#断言当前是否在app主页
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(), "My Devices", "当前在App主页")
