# -*- encoding=utf8 -*-
__author__ = "Mengjie"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
#poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)



# 当没有水箱时，检查设备按钮状态（只有开关可以控制）
# 手动移除水箱后，检查设备按钮状态（前置条件：设备是开启状态，把所有控制功能现写死，再去移除水箱，检查设备按钮状态）
#进入控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()

sleep(3.0)
# Auto模式切换成功
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Auto").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731182521.png", record_pos=(0.012, 0.547), resolution=(1080, 2412)), "Auto模式切换成功")

# 灯光模式切换为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_off").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729669337873.png", record_pos=(-0.192, 0.702), resolution=(1080, 2412)),"灯光模式切换为off成功")

sleep(3.0)
#目标湿度控制-30%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.5, 0.5])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732810609.png", threshold = 0.98, record_pos=(0.209, 0.706), resolution=(1080, 2412)), "目标湿度30%切换成功")

# Timer切换为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.5, 0.5])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729670233002.png", threshold = 0.98, record_pos=(0.221, 0.773), resolution=(1080, 2412)),"timer切换为off成功")
 
# 手动移除水箱后，检查设备按钮状态（只有开关可以控制），当前设备是在开机状态下

swipe(Template(r"tpl1729671834778.png", record_pos=(0.305, 0.29), resolution=(1080, 2412)), vector=[-0.0292, -0.1463])

assert_exists(Template(r"tpl1729671885543.png", threshold = 0.99, record_pos=(0.014, 0.182), resolution=(1080, 2412)),"手动移除水箱后，检查设备按钮状态（只有开关可以控制）")

assert_equal(poco("com.philips.ph.homecare:id/appliance_warn_content_id").get_text(), "Please place your water reservoir in the device.", "error报警")


