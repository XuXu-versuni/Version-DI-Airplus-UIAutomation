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

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-53
   下列20到53行对应 测试用例：https://nutriu.atlassian.net/browse/CH-53
"""
# 打开 Air+ App
poco(text="Air+").click()
sleep(10)

#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)

#点击工作模式选项
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
sleep(2)

#检查 Auto，Sleep，Medium，High 工作模式名称是否显示正确
assert_exists(Template(r"tpl1733298170194.png", record_pos=(0.013, 0.283), resolution=(1440, 3088)), "显示正确")
sleep(1)

#点击Cancel 按钮返回到App 控制页面
poco("com.philips.ph.homecare:id/dialog_control_sheet_cancel").click()
sleep()

#返回App 主页
poco("Navigate up").click()
sleep(1)

#点击工作模式选项
poco("com.philips.ph.homecare:id/dashboard_control_auto_btn").click()
sleep(2)

#检查 Auto，Sleep，Medium，High 工作模式名称是否显示正确
assert_exists(Template(r"tpl1733298170194.png", record_pos=(0.013, 0.283), resolution=(1440, 3088)), "显示正确")
sleep(1)

#点击Cancel 按钮返回到App主页面
poco("com.philips.ph.homecare:id/dialog_control_sheet_cancel").click()
sleep(2)


