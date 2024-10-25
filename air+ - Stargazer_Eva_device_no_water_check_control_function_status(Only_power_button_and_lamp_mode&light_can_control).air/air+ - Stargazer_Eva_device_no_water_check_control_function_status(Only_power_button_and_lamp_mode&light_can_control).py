# -*- encoding=utf8 -*-
__author__ = "Mengjie"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
#poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

# 当水箱无水时，检查控制功能状态（只有开关键和灯光键可控制）
# 当水箱无水后，检查设备按钮状态（前置条件：准备一台无水Stargazer Eva设备，检查设备按钮状态）
#进入控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()

# sleep(3.0)
# # Auto模式切换成功
# poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
# poco(text="Auto").click()
# poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# assert_exists(Template(r"tpl1726731182521.png", record_pos=(0.012, 0.547), resolution=(1080, 2412)), "Auto模式切换成功")

# # 灯光模式切换为off
# sleep(3.0)
# poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
# poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_off").click()
# poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# assert_exists(Template(r"tpl1729669337873.png", record_pos=(-0.192, 0.702), resolution=(1080, 2412)),"灯光模式切换为off成功")

# sleep(3.0)
# #目标湿度控制-30%
# poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
# poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.5, 0.5])
# poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# assert_exists(Template(r"tpl1726732810609.png", threshold = 0.98, record_pos=(0.209, 0.706), resolution=(1080, 2412)), "目标湿度30%切换成功")

# # Timer切换为off
# sleep(3.0)
# poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
# poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.5, 0.5])
# poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# assert_exists(Template(r"tpl1729670233002.png", threshold = 0.98, record_pos=(0.221, 0.773), resolution=(1080, 2412)),"timer切换为off成功")


# 当水箱无水时，设备开机状态，检查控制功能状态（只有开关键和灯光键可控制）

swipe(Template(r"tpl1729749227194.png", record_pos=(0.329, 0.424), resolution=(1080, 2412)), vector=[-0.0693, -0.192])

assert_exists(Template(r"tpl1729749130205.png", threshold = 0.98, record_pos=(0.014, 0.154), resolution=(1080, 2412)),"当水箱无水时，只有开关键和灯光键可控制")
# 检查缺水error警告
assert_equal(poco("com.philips.ph.homecare:id/appliance_warn_content_id").get_text(),"Please refill the water reservoir to sustain the humidity level in the room.","缺水error警告文案显示正确")

# 




 