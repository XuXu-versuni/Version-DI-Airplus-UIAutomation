auto_setup(__file__)
# -*- encoding=utf8 -*-
__author__ = "xjinp"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
poco = AndroidUiautomationPoco()
auto_setup(__file__)


"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-57
例子：下列XXX到YYY行对应 测试用例：https://nutriu.atlassian.net/browse/CH-50
"""

# 打开 Air+ App
poco(text="Air+").click()
sleep(10)

#检查 设备主页面的产品图片是否显示正确
assert_exists(Template(r"tpl1730440020221.png", record_pos=(0.342, -0.644), resolution=(1440, 3088)), "显示正确")
sleep(1)

#进入设备控制页面

poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(1)

#向上滑动屏幕
swipe(Template(r"tpl1730440101211.png", record_pos=(0.017, 0.584), resolution=(1440, 3088)), vector=[-0.0156, -0.5184])
sleep(1)

#点击device settings   进入设备设置页面
poco("com.philips.ph.homecare:id/purifier_control_settings").click()
sleep(1)

#检查 设备主页面的产品图片是否显示正确
assert_exists(Template(r"tpl1730440020221.png", record_pos=(0.342, -0.644), resolution=(1440, 3088)), "显示正确")
sleep(1)

#返回App控制页面
poco("Navigate up").click()
sleep(1)

#向上滑动屏幕
swipe(Template(r"tpl1730441267259.png", record_pos=(0.001, -0.897), resolution=(1440, 3088)), vector=[-0.0173, 0.6627])
sleep(1)

#返回到App主页面
poco("Navigate up").click()
sleep(2)



