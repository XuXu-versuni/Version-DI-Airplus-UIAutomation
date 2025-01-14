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

#CH-1631 Button beep control - Check button default state （28~37）
#CH-2827 Beep sound - power off/on （40~50）


#前置条件：已安装Air+ app，App与Pegasus 3in1 设备已连接成功
#设备信息：Samsung S22 Android 14


#启动Air+ app
start_app("com.philips.ph.homecare")
#断言当前是否在app主页
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(), "My Devices", "当前在App主页")
wait(2.0)
#CH-1631 Button beep control - Check button default state（28~37）
#点击app主页Pegasus卡片
poco("com.philips.ph.homecare:id/dashboard_device_name").click()
#断言已进入设备控制页面
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(), "Air Quality", "已进入设备控制页面")
#点击右上角设备设置按钮
poco("com.philips.ph.homecare:id/menu_setting_id").click()
#断言进入设备设置页面
assert_equal(poco("android.widget.TextView").get_text(), "Settings", "已进入设备设置页面")
#检查beep sound按钮默认状态为开
assert_equal(poco("com.philips.ph.homecare:id/philipsSetting_volume_id").attr("checked"),True,"beep sound按钮状态为开")

#CH-2827 Beep sound - power off/on（40~50）
#关闭beep sound按钮
poco("com.philips.ph.homecare:id/philipsSetting_volume_id").click()
sleep(3)
#断言beep sound按钮为关
assert_equal(poco("com.philips.ph.homecare:id/philipsSetting_volume_id").attr("checked"),False,"beep sound按钮状态为关")

#打开beep sound按钮
poco("com.philips.ph.homecare:id/philipsSetting_volume_id").click()
sleep(3)
#断言beep sound按钮为开
assert_equal(poco("com.philips.ph.homecare:id/philipsSetting_volume_id").attr("checked"),True,"beep sound按钮状态为开")

#点击返回按钮，返回到设备控制页面
poco("Navigate up").click()
sleep(3)
#断言已进入设备控制页面
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(), "Air Quality", "已进入设备控制页面")

#点击返回按钮，返回到app主页
poco("Navigate up").click()
#断言当前是否在app主页
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(), "My Devices", "当前在App主页")