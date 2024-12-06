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

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-406
   下列20到200行对应 测试用例：https://nutriu.atlassian.net/browse/CH-406
"""
# 打开 Air+ App
poco(text="Air+").click()
sleep(10)

#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)

#打开timer 功能设置为1 h
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1733366236117.png", record_pos=(0.15, 0.406), resolution=(1440, 3088)), vector=[0.0081, -0.0416])
sleep(2)

#点击确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)

#检查timer 是否设置为1 h
assert_exists(Template(r"tpl1733366432133.png", record_pos=(0.215, 0.598), resolution=(1440, 3088)), "当前timer 设置时间为1h")

#打开timer 功能设置为2 h
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1733366236117.png", record_pos=(0.15, 0.406), resolution=(1440, 3088)), vector=[0.0081, -0.0416])
sleep(2)

#点击确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)

#检查timer 是否设置为2 h
assert_exists(Template(r"tpl1733366516069.png", record_pos=(0.219, 0.594), resolution=(1440, 3088)), "当前timer 设置时间为2h")
sleep(2)

#打开timer 功能设置为3 h
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1733366236117.png", record_pos=(0.15, 0.406), resolution=(1440, 3088)), vector=[0.0081, -0.0416])
sleep(2)

#点击确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)

#检查timer 是否设置为3h
assert_exists(Template(r"tpl1733366570559.png", record_pos=(0.222, 0.599), resolution=(1440, 3088)), "当前timer 设置时间为3h")
sleep(2)

#打开timer 功能设置为4 h
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1733366236117.png", record_pos=(0.15, 0.406), resolution=(1440, 3088)), vector=[0.0081, -0.0416])
sleep(2)

#点击确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)

#检查timer 是否设置为4h
assert_exists(Template(r"tpl1733374953919.png", record_pos=(0.215, 0.594), resolution=(1440, 3088)), "当前timer 设置时间为3h")
sleep(2)

#打开timer 功能设置为5 h
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1733366236117.png", record_pos=(0.15, 0.406), resolution=(1440, 3088)), vector=[0.0081, -0.0416])
sleep(2)

#点击确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)

#检查timer 是否设置为5h
assert_exists(Template(r"tpl1733375013311.png", record_pos=(0.218, 0.592), resolution=(1440, 3088)), "当前timer 设置时间为5h")
sleep(2)

#打开timer 功能设置为6 h
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1733366236117.png", record_pos=(0.15, 0.406), resolution=(1440, 3088)), vector=[0.0081, -0.0416])
sleep(2)

#点击确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)

#检查timer 是否设置为6h
assert_exists(Template(r"tpl1733375064091.png", record_pos=(0.217, 0.597), resolution=(1440, 3088)), "当前timer 设置时间为6h")
sleep(2)

#打开timer 功能设置为7 h
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1733366236117.png", record_pos=(0.15, 0.406), resolution=(1440, 3088)), vector=[0.0081, -0.0416])
sleep(2)

#点击确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)

#检查timer 是否设置为7h
assert_exists(Template(r"tpl1733375120877.png", record_pos=(0.222, 0.594), resolution=(1440, 3088)), "当前timer 设置时间为7h")
sleep(2)

#打开timer 功能设置为8 h
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1733366236117.png", record_pos=(0.15, 0.406), resolution=(1440, 3088)), vector=[0.0081, -0.0416])
sleep(2)

#点击确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)

#检查timer 是否设置为8h
assert_exists(Template(r"tpl1733375164083.png", record_pos=(0.218, 0.606), resolution=(1440, 3088)), "当前timer 设置时间为8h")
sleep(2)

#打开timer 功能设置为9 h
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1733366236117.png", record_pos=(0.15, 0.406), resolution=(1440, 3088)), vector=[0.0081, -0.0416])
sleep(2)

#点击确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)

#检查timer 是否设置为9h
assert_exists(Template(r"tpl1733375200433.png", record_pos=(0.227, 0.597), resolution=(1440, 3088)), "当前timer 设置时间为9h")
sleep(2)

#打开timer 功能设置为10 h
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1733366236117.png", record_pos=(0.15, 0.406), resolution=(1440, 3088)), vector=[0.0081, -0.0416])
sleep(2)

#点击确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)

#检查timer 是否设置为10h
assert_exists(Template(r"tpl1733375252522.png", record_pos=(0.218, 0.603), resolution=(1440, 3088)), "当前timer 设置时间为10 h")
sleep(2)

#打开timer 功能设置为11 h
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1733366236117.png", record_pos=(0.15, 0.406), resolution=(1440, 3088)), vector=[0.0081, -0.0416])
sleep(2)

#点击确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)

#检查timer 是否设置为11h
assert_exists(Template(r"tpl1733375303053.png", record_pos=(0.217, 0.595), resolution=(1440, 3088)), "当前timer 设置时间为11 h")
sleep(2)

#打开timer 功能设置为12 h
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1733366236117.png", record_pos=(0.15, 0.406), resolution=(1440, 3088)), vector=[0.0081, -0.0416])
sleep(2)

#点击确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)

#检查timer 是否设置为12h
assert_exists(Template(r"tpl1733375332792.png", record_pos=(0.203, 0.593), resolution=(1440, 3088)), "当前timer 设置时间为12 h")
sleep(2)

#设备关机
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
sleep(2)
#验证设备是否在关机机状态
assert_equal(str(poco(text="Power").attr("checked")), "False", "设备当前处于关机状态")
sleep(2)
#设备开机
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
#验证设备是否在开机状态
assert_equal(str(poco(text="Power").attr("checked")), "True", "设备当前处于开机状态")
sleep(2)

#检查设备timer 是否为off 状态
assert_exists(Template(r"tpl1733375542514.png", record_pos=(0.219, 0.597), resolution=(1440, 3088)), "设备timer 为off")

sleep(2)
#返回App 到主页面
poco("Navigate up").click()
sleep(2)












