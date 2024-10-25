# -*- encoding=utf8 -*-
__author__ = "Wmeng1"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device

# poco脚本初始化
poco = AndroidUiautomationPoco(use_airtest_input = True,screenshot_each_action = False)
auto_setup(__file__)


# Stargazer Uitrasonic检查设备功能控制

#Stargazer Eva设备
#进入控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
#上下滑动屏幕
poco("com.philips.ph.homecare:id/philips_control_layout_id").swipe([-0.0539, -0.5587])
poco("com.philips.ph.homecare:id/philips_control_layout_id").swipe([-0.0488, 0.8438])
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([-0.1412, -0.2345])
sleep(3.0)
#设备关机控制
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
#判断设备是否关机
assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"),False,msg="设备关机.")

sleep(3.0)
#设备开机控制
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
#判断设备是否开机
assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"),True,msg="设备开机.")

sleep(3.0)
#模式切换为Auto
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Auto").click()
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731182521.png", record_pos=(0.012, 0.547), resolution=(1080, 2412)), "Auto模式切换成功")

sleep(3.0)
#模式切换为Sleep
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Sleep").click()
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731452159.png", record_pos=(0.006, 0.557), resolution=(1080, 2412)), "Sleep模式切换成功")

sleep(3.0)
#模式切换为Medium
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Medium").click()
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731497712.png", record_pos=(0.017, 0.551), resolution=(1080, 2412)), "Medium模式切换成功")

sleep(3.0)
#模式切换为High
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="High").click()
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731551102.png", record_pos=(0.002, 0.553), resolution=(1080, 2412)), "High模式切换成功")

sleep(3.0)
#湿度灯的切换
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_humidity").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731828009.png", threshold = 0.98, record_pos=(-0.208, 0.695), resolution=(1080, 2412)), "Huimidity切换成功")


sleep(3.0)
#环境灯的切换（Ambient:Warm）
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_warm").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731935717.png", threshold = 0.98, record_pos=(-0.206, 0.628), resolution=(1080, 2412)), "Ambient:Warm切换成功")


sleep(3.0)
#环境灯的切换（Ambient:Dawn）
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_dawn").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731985254.png", threshold = 0.98, record_pos=(-0.206, 0.626), resolution=(1080, 2412)), "Ambient:Dawn切换成功")

sleep(3.0)
#环境灯的切换（Ambient:Calm）
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_calm").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732012578.png", threshold = 0.98, record_pos=(-0.201, 0.623), resolution=(1080, 2412)), "Ambient:Calm切换成功")

sleep(3.0)
#环境灯的切换（Ambient:Breath）
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_breath").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732052079.png", threshold = 0.98, record_pos=(-0.199, 0.629), resolution=(1080, 2412)), "Ambient:Breath切换成功")

sleep(3.0)
#灯光关闭
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_off").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732109040.png", threshold = 0.98, record_pos=(-0.206, 0.629), resolution=(1080, 2412)), "灯光关闭成功")


#灯光亮度控制
sleep(3.0)
#灯光切换为亮
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Bright").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732266066.png", threshold = 0.98, record_pos=(-0.211, 0.781), resolution=(1080, 2412)), "灯光切换为亮成功")

sleep(3.0)
#灯光切换为暗
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Low").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732335858.png", threshold = 0.98, record_pos=(-0.208, 0.778), resolution=(1080, 2412)), "灯光切换为暗成功")


sleep(3.0)
#灯光切换为关闭
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Off").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732379261.png", threshold = 0.98, record_pos=(-0.198, 0.784), resolution=(1080, 2412)), "灯光切换为关闭成功")


sleep(3.0)
#目标湿度控制-40%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco(text="40%").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729841733055.png", threshold=0.98, record_pos=(0.22, 0.628), resolution=(1080, 2412)),"目标湿度控制-40%成功")

sleep(3.0)
#目标湿度控制-50%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco(text="50%").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729841975415.png", threshold=0.98, record_pos=(0.235, 0.622), resolution=(1080, 2412)),"目标湿度控制-50%成功")

sleep(3.0)
#目标湿度控制-60%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco(text="60%").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729842079165.png", threshold=0.98, record_pos=(0.216, 0.628), resolution=(1080, 2412)),"目标湿度控制-60%成功")

sleep(3.0)
#目标湿度控制-70%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco(text="70%").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729842167890.png", threshold=0.98, record_pos=(0.218, 0.701), resolution=(1080, 2412)),"目标湿度控制-70%成功")


