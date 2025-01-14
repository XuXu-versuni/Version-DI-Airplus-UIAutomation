# -*- encoding=utf8 -*-
__author__ = "xjinp"

# from airtest.core.api import *

# auto_setup(__file__)


from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
poco = AndroidUiautomationPoco()
auto_setup(__file__)

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-61
   下列20到90行对应 测试用例：https://nutriu.atlassian.net/browse/CH-61
"""
# 打开 Air+ App
start_app("com.philips.ph.homecare")
sleep(10)

#进入设备控制页面
#poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
#sleep(3)
#点击 主页设备工作模式按钮
poco("com.philips.ph.homecare:id/dashboard_control_auto_btn").click()
#切换工作模式为Medium mode
poco(text="Medium").click()
sleep(1)
#点击确认切换Medium mode 按钮
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
#检查当前工作模式是否为Medium mode
assert_exists(Template(r"tpl1733377502207.png", record_pos=(-0.117, 0.297), resolution=(1440, 3088)), "当前模式 图标为medium，确认当前模式为medium mode")
sleep(1)
#切换工作模式为Auto mode
poco("com.philips.ph.homecare:id/dashboard_control_auto_btn").click()
sleep(1)
poco(text="Auto").click()
sleep(1)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#检查当前工作模式是否为Auto mode
assert_exists(Template(r"tpl1733377636879.png", record_pos=(-0.11, 0.292), resolution=(1440, 3088)), "当前模式 图标为Auto，确认当前模式为Auto mode")
sleep(1)
#切换工作模式为Sleep mode
poco("com.philips.ph.homecare:id/dashboard_control_auto_btn").click()
sleep(1)
poco(text="Sleep").click()
sleep(1)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
#检查当前工作模式是否为Sleep mode
assert_exists(Template(r"tpl1733377865697.png", record_pos=(-0.117, 0.291), resolution=(1440, 3088)), "当前模式 图标为Sleep，确认当前模式为sleep mode")
sleep(1)
#切换工作模式为High mode
poco("com.philips.ph.homecare:id/dashboard_control_auto_btn").click()
poco(text="High").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#检查当前工作模式是否为High mode
assert_exists(Template(r"tpl1733377975660.png", record_pos=(-0.106, 0.298), resolution=(1440, 3088)), "当前模式 图标为High，确认当前模式为High mode")
sleep(1)
#点击主页设备灯光按钮
poco("com.philips.ph.homecare:id/dashboard_control_light_mode_btn").click()
sleep(1)
#检查灯光选项
assert_exists(Template(r"tpl1733378178846.png", record_pos=(0.024, 0.339), resolution=(1440, 3088)), "灯光选项模式名称显示正确")
sleep(1)
#取消灯光选项
poco("com.philips.ph.homecare:id/dialog_control_sheet_cancel").click()
sleep(1)
#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)
#检查设备环境灯光按钮图标
assert_exists(Template(r"tpl1733378345035.png", record_pos=(-0.267, 0.594), resolution=(1440, 3088)), "显示正确")
sleep(1)
#检查设备灯光按钮图标
assert_exists(Template(r"tpl1733378392742.png", record_pos=(-0.29, 0.464), resolution=(1440, 3088)), "显示正确")
sleep(1)
#检查设备湿度按钮图标
assert_exists(Template(r"tpl1733378415242.png", record_pos=(0.169, 0.467), resolution=(1440, 3088)), "显示正确")
sleep(1)
#检查设备timer 按钮图标
assert_exists(Template(r"tpl1733378467538.png", record_pos=(0.176, 0.594), resolution=(1440, 3088)), "显示正确")
sleep(1)
#返回App 到主页面
poco("Navigate up").click()
sleep(2)


