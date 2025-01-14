# -*- encoding=utf8 -*-
__author__ = "xjinp"

from airtest.core.api import *

auto_setup(__file__)


from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
poco = AndroidUiautomationPoco()
auto_setup(__file__)

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-56
   下列20到41行对应 测试用例：https://nutriu.atlassian.net/browse/CH-56
"""
# 打开 Air+ App
poco(text="Air+").click()
sleep(10)

#检查设备产品图片显示
assert_exists(Template(r"tpl1736318162457.png", record_pos=(-0.323, 0.015), resolution=(1440, 3088)), "显示正确")

sleep(1)


#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)

#向下滑动
swipe(Template(r"tpl1733302507976.png", record_pos=(0.068, 0.762), resolution=(1440, 3088)), vector=[-0.0285, -0.5381])

#点击Devices settings 按钮
poco("com.philips.ph.homecare:id/purifier_control_settings").click()
sleep(2)

#验证App 是否进入setting 页面
assert_equal(str(poco(text="Settings").attr("enabled")), "True", "App 已进入settings 页面")
sleep(3)

#检查设备产品图片显示
assert_exists(Template(r"tpl1736318195855.png", record_pos=(0.35, -0.635), resolution=(1440, 3088)), "产品图片显示正确")

sleep(2)

#返回App 到主页
poco("Navigate up").click()
sleep(2)

#向下滑动
swipe(Template(r"tpl1733302946450.png", record_pos=(0.276, -0.903), resolution=(1440, 3088)), vector=[-0.1435, 0.5971])
sleep(2)

#返回App to home page
poco("Navigate up").click()
sleep(2)
