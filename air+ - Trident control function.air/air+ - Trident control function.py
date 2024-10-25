# -*- encoding=utf8 -*-
__author__ = "ytian1"

from airtest.core.api import *
from airtest.core.api import using
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

# 前置条件：已安装Air+ app，连接一台trident设备
# 设备当前默认工作模式为自然风，默认选择角度为OFF，默认timer关闭下运行
# 设备信息：Pixel 9 Android 14


#启动Air+ app
start_app("com.philips.ph.homecare")
sleep(10)
#在app主页点击设备卡片进入设备控制页面
touch(Template(r"tpl1729834438632.png", record_pos=(0.008, -0.127), resolution=(1080, 2424)))

#断言是否进入设备控制页面
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_controls_section").get_text(), "Controls","已进入设备控制页面")

#CH-2908 在app切换电源模式为off
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
sleep(3)
#断言当前电源是否在off状态
assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"), False, "当前电源状态为off")

#CH-2907 在app切换电源模式为on
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
sleep(3)
#断言当前电源是否在on状态
assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"),True, "当前电源状态为on")

#CH-2909 在app切换风速为1
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Speed 1").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言当前风速为1
assert_exists(Template(r"tpl1729671546825.png", record_pos=(0.005, -0.347), resolution=(1080, 2424), threshold = 0.97), "当前风速为1")

#CH-2910 在app切换风速为2
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Speed 2").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言当前风速为2
assert_exists(Template(r"tpl1729671800132.png", record_pos=(0.006, -0.343), resolution=(1080, 2424),threshold = 0.96), "当前风速为2")

#CH-2911 在app切换风速为3
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Speed 3").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言当前风速为3
assert_exists(Template(r"tpl1729671853902.png", record_pos=(0.001, -0.344), resolution=(1080, 2424),threshold = 0.95), "当前风速为3")

#CH-2912 在app切换模式为睡眠
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Sleep").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言当前模式为睡眠
assert_exists(Template(r"tpl1729755066311.png", record_pos=(0.017, -0.349), resolution=(1080, 2424),threshold = 0.8), "当前模式为睡眠")

#CH-2913 在app切换模式为自然风
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Natural Breeze").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言当前模式为自然风
assert_exists(Template(r"tpl1729755116279.png", record_pos=(-0.005, -0.347), resolution=(1080, 2424),threshold = 0.8), "当前模式为自然风")

#CH-2914 在app上旋转模式设置为on
poco("com.philips.ph.homecare:id/philips_control_oscillation_toggle_id").click()
sleep(3)
#断言当前旋转模式为on
assert_exists(Template(r"tpl1729755183832.png", record_pos=(-0.21, -0.237), resolution=(1080, 2424),threshold = 0.9), "当前旋转模式为on")


#CH-2915 在app上旋转模式设置为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_toggle_id").click()
sleep(3)
#断言当前旋转模式为off
assert_exists(Template(r"tpl1729755232487.png", record_pos=(-0.219, -0.234), resolution=(1080, 2424),threshold = 0.7), "当前旋转模式为off")


#CH-2916 在app旋转模式设为on，切换工作模式为风速1
poco("com.philips.ph.homecare:id/philips_control_oscillation_toggle_id").click()
sleep(3)
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Speed 1").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言当前模式为风速1
assert_exists(Template(r"tpl1729671546825.png", record_pos=(0.005, -0.347), resolution=(1080, 2424), threshold = 0.97), "当前风速为1")
#断言当前旋转模式为on
assert_exists(Template(r"tpl1729755183832.png", record_pos=(-0.21, -0.237), resolution=(1080, 2424), threshold = 0.9), "当前旋转模式为on")


#CH-2917 在app旋转模式设为on，切换工作模式为风速2
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Speed 2").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言当前风速为2
assert_exists(Template(r"tpl1729671800132.png", record_pos=(0.006, -0.343), resolution=(1080, 2424),threshold = 0.96), "当前风速为2")
#断言当前旋转模式为on
assert_exists(Template(r"tpl1729755183832.png", record_pos=(-0.21, -0.237), resolution=(1080, 2424),threshold = 0.9), "当前旋转模式为on")


#CH-2918 在app旋转模式设为on，切换工作模式为风速3
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Speed 3").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言当前风速为3
assert_exists(Template(r"tpl1729671853902.png", record_pos=(0.001, -0.344), resolution=(1080, 2424),threshold = 0.95), "当前风速为3")
#断言当前旋转模式为on
assert_exists(Template(r"tpl1729755183832.png", record_pos=(-0.21, -0.237), resolution=(1080, 2424),threshold = 0.9), "当前旋转模式为on")


#CH-2919 在app旋转模式设为on，切换工作模式为睡眠
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Sleep").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言当前模式为睡眠
assert_exists(Template(r"tpl1729755066311.png", record_pos=(0.017, -0.349), resolution=(1080, 2424),threshold = 0.8), "当前模式为睡眠")
#断言当前旋转模式为on
assert_exists(Template(r"tpl1729755183832.png", record_pos=(-0.21, -0.237), resolution=(1080, 2424),threshold = 0.9), "当前旋转模式为on")


#CH-2920 在app旋转模式设为on，切换工作模式为自然风
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Natural Breeze").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言当前模式为自然风
assert_exists(Template(r"tpl1729755116279.png", record_pos=(-0.005, -0.347), resolution=(1080, 2424),threshold = 0.8), "当前模式为自然风")
#断言当前旋转模式为on
assert_exists(Template(r"tpl1729755183832.png", record_pos=(-0.21, -0.237), resolution=(1080, 2424),threshold = 0.9), "当前旋转模式为on")


#将设备恢复默认模式旋转角度关闭，并且返回到app主页
poco("com.philips.ph.homecare:id/philips_control_oscillation_toggle_id").click()
sleep(3)
#断言当前旋转模式为off
assert_exists(Template(r"tpl1729755232487.png", record_pos=(-0.219, -0.234), resolution=(1080, 2424),threshold = 0.7), "当前旋转模式为off")
#返回到app主页
touch(Template(r"tpl1729835703519.png", record_pos=(-0.417, -0.985), resolution=(1080, 2424)))
sleep(3)
#断言当前页面在app主页
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(), "My Devices", "当前页面在app主页")

