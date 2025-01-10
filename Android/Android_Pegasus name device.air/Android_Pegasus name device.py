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

#CH-273 Name Device-Change the device name in the device settings
#CH-274 Name Device-Special characters/length restrictions

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

#点击输入名字按钮,更改为office
poco("com.philips.ph.homecare:id/philipsSetting_name_id").click()
poco("com.philips.ph.homecare:id/dialog_name_edit").click()
text("office")
poco("com.philips.ph.homecare:id/dialog_name_apply").click()
sleep(3)

#断言当前设备名字更改为office
assert_equal(poco("com.philips.ph.homecare:id/philipsSetting_name_id").get_text(), "office", "当前设备名字为office")

#点击输入名字按钮，将设备名字更改为特殊字符
poco("com.philips.ph.homecare:id/philipsSetting_name_id").click()
poco("com.philips.ph.homecare:id/dialog_name_edit").click()
text("！@#￥%……&*（）——+")
poco("com.philips.ph.homecare:id/dialog_name_apply").click()
sleep(5)

#返回到设备控制页面断言设备名字！@#￥%……&*（）——+
poco("Navigate up").click()
assert_exists(Template(r"tpl1736320633276.png", record_pos=(-0.015, -0.916), resolution=(1080, 2340)), "当前设备名字正确")

#在设备控制页面点击右上角设置按钮，再进入设备设置页面
poco("com.philips.ph.homecare:id/menu_setting_id").click()
sleep(2)
#断言进入设备设置页面
assert_equal(poco("android.widget.TextView").get_text(), "Settings", "已进入设备设置页面")

#点击输入名字按钮，将设备名字更改为9个中文字符
poco("com.philips.ph.homecare:id/philipsSetting_name_id").click()
poco("com.philips.ph.homecare:id/dialog_name_edit").click()
text("飞利浦空气净化器牛")
poco("com.philips.ph.homecare:id/dialog_name_apply").click()
sleep(10)

#返回到设备控制页面断言设备名字为"飞利浦空气净化器牛"
poco("Navigate up").click()
assert_equal(poco("android.widget.TextView").get_text(), "飞利浦空气净化器牛", "当前设备名字为飞利浦空气净化器牛")

#在设备控制页面点击右上角设置按钮，再进入设备设置页面
poco("com.philips.ph.homecare:id/menu_setting_id").click()
sleep(2)
#断言进入设备设置页面
assert_equal(poco("android.widget.TextView").get_text(), "Settings", "已进入设备设置页面")

#点击输入名字按钮，将设备名字更改为29个英文字符
poco("com.philips.ph.homecare:id/philipsSetting_name_id").click()
poco("com.philips.ph.homecare:id/dialog_name_edit").click()
text("qwertyuiopasdfghjklzxcvbnmnbv")
poco("com.philips.ph.homecare:id/dialog_name_apply").click()
sleep(5)

#返回到设备控制页面断言设备名字为"qwertyuiopasdfghjklzxcvbnmnbv"
poco("Navigate up").click()
assert_equal(poco("android.widget.TextView").get_text(), "qwertyuiopasdfghjklzxcvbnmnbv", "qwertyuiopasdfghjklzxcvbnmnbv")

#恢复默认返回app主页
#点击返回按钮，返回到app主页
poco("Navigate up").click()
#断言当前是否在app主页
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(), "My Devices", "当前在App主页")












