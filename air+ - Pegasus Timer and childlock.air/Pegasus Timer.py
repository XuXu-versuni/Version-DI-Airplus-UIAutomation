# -*- encoding=utf8 -*-
__author__ = "ytian1"

from airtest.core.api import *
from airtest.core.api import using
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
# element = UIObjectProxy(poco = poco,name = "com.philips.ph.homecare:id/display_theme_auto")
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

# CH-1596 Timer - Set a timer, than power off and power on
# CH-1595 Timer - Set timer to 0.5h-12h
# CH-49 Child Lock-Re-power the device
# CH-269 Child Lock-On&Off-Device Functionality


#启动Air+ app
start_app("com.philips.ph.homecare")

#点击设备卡片进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_card_content").click()

#断言是否进入设备控制页面
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(), "Air Quality","已进入设备控制页面")
swipe([802,1914],[802,819])
sleep(2)

# CH-1596 Timer - Set a timer, than power off and power on
#设置1h关机后timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
sleep(2)
swipe([723,1545],[723,1400])
sleep(3)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言当前timer设定为1h
assert_exists(Template(r"tpl1733213688905.png", record_pos=(-0.271, 0.768), resolution=(1080, 2340), threshold = 0.98), "当前timer设定为1h")
#在app上点击关机按钮
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
sleep(3)
#断言当前设备为关机状态
assert_exists(Template(r"tpl1733213909631.png", record_pos=(-0.122, 0.352), resolution=(1080, 2340),threshold = 0.98), "当前为关机状态")
#在app上点击开机按钮
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
sleep(3)
#断言当前设备为开机状态
assert_exists(Template(r"tpl1733377151995.png", record_pos=(-0.137, 0.033), resolution=(1080, 2340),threshold = 0.98), "当前为开机状态")
#断言当前timer状态为关闭的状态
assert_exists(Template(r"tpl1733380468659.png", record_pos=(-0.28, 0.535), resolution=(1080, 2340), threshold = 0.98), "当前timer为off")


# CH-1595 Timer - Set timer to 0.5h-12h
#设置30分钟的timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0, -0.0378])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前timer设置为30min
assert_exists(Template(r"tpl1733378526226.png", record_pos=(-0.264, 0.606), resolution=(1080, 2340),threshold = 0.98), "当前timer设置为30min")

#设置1h的timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0, -0.0378])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前timer设置为1h
assert_exists(Template(r"tpl1733378759497.png", record_pos=(-0.273, 0.614), resolution=(1080, 2340),threshold = 0.98), "当前timer设置为1h")

#设置2h的timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0, -0.0378])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前timer设置为2h
assert_exists(Template(r"tpl1733378852862.png", record_pos=(-0.271, 0.61), resolution=(1080, 2340),threshold = 0.98), "当前timer设置为2h")

#设置3h的timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0, -0.0378])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前timer设置为3h
assert_exists(Template(r"tpl1733378943650.png", record_pos=(-0.274, 0.609), resolution=(1080, 2340),threshold = 0.98), "当前timer设置为3h")

#设置4h的timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0, -0.0378])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前timer设置为4h
assert_exists(Template(r"tpl1733378989682.png", record_pos=(-0.262, 0.606), resolution=(1080, 2340),threshold = 0.98), "当前timer设置为4h")

#设置5h的timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0, -0.0378])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前timer设置为5h
assert_exists(Template(r"tpl1733379048944.png", record_pos=(-0.268, 0.606), resolution=(1080, 2340),threshold = 0.98), "当前timer设置为5h")

#设置6h的timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0, -0.0378])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前timer设置为6h
assert_exists(Template(r"tpl1733379122688.png", record_pos=(-0.272, 0.609), resolution=(1080, 2340),threshold = 0.98), "当前timer设置为6h")

#设置7h的timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0, -0.0378])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前timer设置为7h
assert_exists(Template(r"tpl1733379186106.png", record_pos=(-0.271, 0.61), resolution=(1080, 2340),threshold = 0.98), "当前timer设置为7h")

#设置8h的timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0, -0.0378])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前timer设置为8h
assert_exists(Template(r"tpl1733379254644.png", record_pos=(-0.267, 0.606), resolution=(1080, 2340),threshold = 0.98), "当前timer设置为8h")

#设置9h的timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0, -0.0378])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前timer设置为9h
assert_exists(Template(r"tpl1733379314917.png", record_pos=(-0.275, 0.605), resolution=(1080, 2340),threshold = 0.98), "当前timer设置为9h")

#设置10h的timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0, -0.0378])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前timer设置为10h
assert_exists(Template(r"tpl1733379403271.png", record_pos=(-0.267, 0.609), resolution=(1080, 2340),threshold = 0.98), "当前timer设置为10h")

#设置11h的timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0, -0.0378])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前timer设置为11h
assert_exists(Template(r"tpl1733379465134.png", record_pos=(-0.265, 0.611), resolution=(1080, 2340),threshold = 0.98), "当前timer设置为11h")

#设置12h的timer
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0, -0.0378])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前timer设置为12h
assert_exists(Template(r"tpl1733379529659.png", record_pos=(-0.275, 0.609), resolution=(1080, 2340),threshold = 0.98), "当前timer设置为12h")


# CH-49 Child Lock-Re-power the device
#在app上打开童锁
poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").click()
sleep(3)
#断言当前童锁是否打开的状态
assert_exists(Template(r"tpl1733380266776.png", record_pos=(0.128, 0.119), resolution=(1080, 2340),threshold = 0.98),  "当前童锁已打开")
#在app上点击关机按钮
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
sleep(3)
#断言当前设备为关机状态
assert_exists(Template(r"tpl1733213909631.png", record_pos=(-0.122, 0.352), resolution=(1080, 2340),threshold = 0.98), "当前为关机状态")
#在app上点击开机按钮
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
sleep(3)
#断言当前设备为开机状态
assert_exists(Template(r"tpl1733377151995.png", record_pos=(-0.137, 0.033), resolution=(1080, 2340),threshold = 0.98), "当前为开机状态")
#断言童锁功能为关闭状态
assert_exists(Template(r"tpl1733380670127.png", record_pos=(0.127, 0.122), resolution=(1080, 2340),threshold = 0.98), "当前童锁已关闭")


# CH-269 Child Lock-On&Off-Device Functionality
#打开童锁功能
poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").click()
sleep(3)
#断言当前童锁功能已打开
assert_exists(Template(r"tpl1733380266776.png", record_pos=(0.128, 0.119), resolution=(1080, 2340),threshold = 0.98),  "当前童锁已打开")
#关闭童锁功能
poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").click()
sleep(3)
#断言当前童锁功能已关闭
assert_exists(Template(r"tpl1733380670127.png", record_pos=(0.127, 0.122), resolution=(1080, 2340),threshold = 0.98), "当前童锁已关闭")


#返回app主页
poco("com.android.systemui:id/back").click()
sleep(2)
#断言当前返回到app主页
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(), "My Devices","已返回到app主页")








