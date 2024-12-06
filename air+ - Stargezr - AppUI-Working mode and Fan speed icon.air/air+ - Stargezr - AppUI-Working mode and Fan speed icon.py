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

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-60
   下列20到200行对应 测试用例：https://nutriu.atlassian.net/browse/CH-60
"""
# 打开 Air+ App
poco(text="Air+").click()
sleep(10)

poco(text="Air+").click()
sleep(10)
poco(text="Air+").click()
sleep(10)


####


#点击设备主页工作模式选项按钮
poco("com.philips.ph.homecare:id/dashboard_control_auto_btn").click()
sleep(1)
#检查Auto 模式和icon
assert_exists(Template(r"tpl1733376253949.png", record_pos=(0.02, 0.065), resolution=(1440, 3088)), "Auto 模式名称和icon 显示正确")
sleep(1)
#检查sleep 模式和icon
assert_exists(Template(r"tpl1733376314895.png", record_pos=(0.017, 0.209), resolution=(1440, 3088)), "Sleep 模式名称和icon 显示正确")
sleep(1)
#检查Medium 模式和icon
assert_exists(Template(r"tpl1733376362570.png", record_pos=(0.005, 0.343), resolution=(1440, 3088)), "Medium 模式名称和icon 显示正确")
sleep(1)
#检查High 模式和icon
assert_exists(Template(r"tpl1733376407995.png", record_pos=(0.02, 0.474), resolution=(1440, 3088)), "High模式名称和icon 显示正确")
sleep(1)

#取消当前页面，App返回到主页
poco("com.philips.ph.homecare:id/dialog_control_sheet_cancel").click()
sleep(2)

#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)
#点击设备主页工作模式选项按钮
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
sleep(1)
#检查Auto 模式和icon
assert_exists(Template(r"tpl1733376253949.png", record_pos=(0.02, 0.065), resolution=(1440, 3088)), "Auto 模式名称和icon 显示正确")
sleep(1)
#检查sleep 模式和icon
assert_exists(Template(r"tpl1733376314895.png", record_pos=(0.017, 0.209), resolution=(1440, 3088)), "Sleep 模式名称和icon 显示正确")
sleep(1)
#检查Medium 模式和icon
assert_exists(Template(r"tpl1733376362570.png", record_pos=(0.005, 0.343), resolution=(1440, 3088)), "Medium 模式名称和icon 显示正确")
sleep(1)
#检查High 模式和icon
assert_exists(Template(r"tpl1733376407995.png", record_pos=(0.02, 0.474), resolution=(1440, 3088)), "High模式名称和icon 显示正确")
sleep(1)

#取消当前页面，App返回到主页
poco("com.philips.ph.homecare:id/dialog_control_sheet_cancel").click()
sleep(2)
poco("Navigate up").click()
sleep(2)


