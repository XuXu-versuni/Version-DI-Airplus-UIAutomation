# -*- encoding=utf8 -*-
__author__ = "Wmeng1"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device

# Poco脚本初始化
poco = AndroidUiautomationPoco(Use_airtest_input = True,screenshot_each_action = False)
auto_setup(__file__)

# Stargazer Eva设备无水并且自动干燥模式打开，检查控制功能（只有控制功能和灯光模式/灯光亮度可控制）
# 进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_control_more_btn").click()
assert_exists(Template(r"tpl1729754367621.png", record_pos=(-0.263, -0.354), resolution=(1080, 2412)),"设备控制页面进入成功")
swipe([873,1488],[-865,-1574])
sleep(3.0)
# 设备是开机状态，进入AuickDry mode页面
poco("com.philips.ph.homecare:id/purifier_control_dry_mode").click()
assert_equal(poco("com.philips.ph.homecare:id/quick_dry_manual_id").get_text(),"Manual QuickDry mode","AuickDry mode页面进入成功")
# 检查Auto QuickDry mode下的文案显示（语言：English）
# assert_equal(poco("android.widget.TextView").get_text(),"Activating to automatically switch to the QuickDry mode when the water tank is not refilled when it is empty. The humidifier uses the power of the fan to accelerate filter drying after usage, promoting hygienic maintenance, and prolonging the filter’s lifespan. The process of drying can take up to 4 hours, depending on the conditions of the room.","Auto QuickDry mode下的文案显示正确")
assert_exists(Template(r"tpl1729758580126.png", record_pos=(-0.019, -0.516), resolution=(1080, 2412)),"Auto QuickDry mode下的文案显示正确")
# 检查Manual QuickDry mode下的文案（语言：English）
assert_exists(Template(r"tpl1729758646470.png", record_pos=(-0.004, -0.003), resolution=(1080, 2412)),"Manual QuickDry mode下的文案显示正确")

assert_equal(poco("com.philips.ph.homecare:id/quick_dry_manual_btn").attr("enabled"),True,"Start按钮可以点击")
# 打开Manual QuickDry mode功能
sleep(3.0)
poco("com.philips.ph.homecare:id/quick_dry_manual_btn").click()
swipe(Template(r"tpl1729755101055.png", record_pos=(0.232, -0.375), resolution=(1080, 2412)), vector=[-0.1874, 0.7782])

assert_equal(poco("com.philips.ph.homecare:id/purifier_control_dry_progress").get_text(),"QuickDry in progress","打开Manual QuickDry mode功能成功")

# Stargazer Eva设备无水并且自动干燥模式打开，检查控制功能（只有控制功能和灯光模式/灯光亮度可控制）
swipe([892,1472],[887,1178])
assert_exists(Template(r"tpl1729755839871.png", threshold=0.98, record_pos=(0.02, 0.29), resolution=(1080, 2412)),"只有控制功能和灯光模式/灯光亮度可控制，符合预期结果")










