# -*- encoding=utf8 -*-
__author__ = "ytian1"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# CH-1612 Light-Brightness Percentage (Pegasus)	 (34~133)
# CH-1614 Light -Select Sleep + any brightnessagain, and power off and on	(136~167)
# CH-266 Light-On/Off-App Functionality （171~184)
# CH-270 Light-After power off and power on again	（187~198）

#前置条件：已安装Air+ app，已连接Pegasus 3in1设备，灯光默认为100%
#设备信息：Samsung S22 Android 14

#启动Air+ app
start_app("com.philips.ph.homecare")

#点击设备卡片进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_card_content").click()

#断言是否进入设备控制页面
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(), "Air Quality","已进入设备控制页面")
swipe([802,1914],[802,819])
sleep(2)

# CH-1612 Light-Brightness Percentage (Pegasus)	(34~133)
#设置灯光为OFF
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Off").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前灯光为OFF
assert_exists(Template(r"tpl1733382696861.png", record_pos=(0.285, 0.738), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为off")

#设置灯光为10%
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="10 %").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前灯光为10%
assert_exists(Template(r"tpl1733382903439.png", record_pos=(0.281, 0.745), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为10%")

#设置灯光为20%
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="20 %").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前灯光为20%
assert_exists(Template(r"tpl1733382998979.png", record_pos=(0.285, 0.742), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为20%")

#设置灯光为30%
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="30 %").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前灯光为30%
assert_exists(Template(r"tpl1733383060046.png", record_pos=(0.283, 0.744), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为30%")

#设置灯光为40%
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="40 %").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前灯光为40%
assert_exists(Template(r"tpl1733383142722.png", record_pos=(0.28, 0.742), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为40%")

#设置灯光为50%
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="50 %").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前灯光为50%
assert_exists(Template(r"tpl1733383209110.png", record_pos=(0.283, 0.746), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为50%")

#设置灯光为60%
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="60 %").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前灯光为60%
assert_exists(Template(r"tpl1733383320622.png", record_pos=(0.287, 0.753), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为60%")

#设置灯光为70%
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="70 %").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前灯光为70%
assert_exists(Template(r"tpl1733383384774.png", record_pos=(0.284, 0.747), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为70%")

#设置灯光为80%
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco("com.philips.ph.homecare:id/coordinator").swipe([-0.0047, -0.1946])
sleep(3)
poco(text="80 %").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前灯光为80%
assert_exists(Template(r"tpl1733383488719.png", record_pos=(0.281, 0.746), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为80%")

#设置灯光为90%
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="90 %").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前灯光为90%
assert_exists(Template(r"tpl1733383552081.png", record_pos=(0.287, 0.748), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为90%")

#设置灯光为100%
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="100 %").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前灯光为100%
assert_exists(Template(r"tpl1733383618940.png", record_pos=(0.282, 0.743), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为100%")

# CH-1614 Light -Select Sleep + any brightnessagain, and power off and on	(136~167)
#选择睡眠模式
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Sleep").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前模式为睡眠
assert_exists(Template(r"tpl1733383915304.png", record_pos=(-0.201, 0.449), resolution=(1080, 2340),threshold = 0.98), "当前为睡眠模式")

#灯光设置为50%
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="50 %").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()poco(text="50 %").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前灯光为50%
assert_exists(Template(r"tpl1733383209110.png", record_pos=(0.283, 0.746), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为50%")

#在app上点击关机按钮
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
sleep(5)
#断言当前设备为关机状态
assert_exists(Template(r"tpl1733384306518.png", record_pos=(-0.122, 0.331), resolution=(1080, 2340),threshold = 0.98), "当前为关机状态")
#在app上点击开机按钮
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
sleep(3)
#断言当前设备为开机状态
assert_exists(Template(r"tpl1733384125483.png", record_pos=(-0.128, 0.261), resolution=(1080, 2340),threshold = 0.98), "当前为开机状态")
#断言当前模式为睡眠模式
assert_exists(Template(r"tpl1733383915304.png", record_pos=(-0.201, 0.449), resolution=(1080, 2340),threshold = 0.98), "当前为睡眠模式")
#断言当前灯光为50%
assert_exists(Template(r"tpl1733383209110.png", record_pos=(0.283, 0.746), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为50%")

# CH-266 Light-On/Off-App Functionality （171~184)
#在app点击灯光按钮OFF
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Off").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前灯光为OFF
assert_exists(Template(r"tpl1733382696861.png", record_pos=(0.285, 0.738), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为off")
#在app上点击灯光按钮100%
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco("com.philips.ph.homecare:id/coordinator").swipe([0.0023, -0.3394])
sleep(3)
poco(text="100 %").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前灯光为100%
assert_exists(Template(r"tpl1733383618940.png", record_pos=(0.282, 0.743), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为100%")

# CH-270 Light-After power off and power on again （187~198）
#在app上点击关机按钮
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
sleep(3)
#断言当前设备为关机状态
assert_exists(Template(r"tpl1733384306518.png", record_pos=(-0.122, 0.331), resolution=(1080, 2340),threshold = 0.98), "当前为关机状态")
#在app上点击开机按钮
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
sleep(3)
#断言当前设备为开机状态
assert_exists(Template(r"tpl1733384125483.png", record_pos=(-0.128, 0.261), resolution=(1080, 2340),threshold = 0.98), "当前为开机状态")
#断言当前灯光仍然为100%
assert_exists(Template(r"tpl1733383618940.png", record_pos=(0.282, 0.743), resolution=(1080, 2340),threshold = 0.98), "当前灯光设置为100%")





