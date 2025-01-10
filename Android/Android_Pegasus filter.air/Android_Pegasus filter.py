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

#前置条件：已安装Air+ app，已连接Pegasus 3in1设备
#设备信息：Samsung S22 Android 14

# CH-1630 Fliter - Reset filter (App)  （30~82）
# CH-150 Filter Purchase-Nano Protec Filter （87~98）
# CH-149 Filter Purchase-HEPA Filter （87~98）
# CH-148 Filter Purchase-Active Carbon Filter （87~98）
# CH-146 Filter Life Time- Clean and Replacement Guide （101~142）

#启动Air+ app
start_app("com.philips.ph.homecare")
#断言当前是否在app主页
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(), "My Devices", "当前在App主页")

# CH-1630 Fliter - Reset filter (App) （30~82）
#点击app主页Pegasus卡片
poco("com.philips.ph.homecare:id/dashboard_device_name").click()
#断言已进入设备控制页面
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(), "Air Quality", "已进入设备控制页面")

#滑动页面至device health
swipe([804,1862],[804,100])
sleep(3)
swipe([804,1862],[804,100])
sleep(3)

#点击device health按钮
poco("com.philips.ph.homecare:id/purifier_control_health").click()
#断言是否进入device health页面
assert_equal(poco("android.widget.TextView").get_text(), "Device Health", "已进入device health页面")
#断言filter文案检查
assert_exists(Template(r"tpl1736478677205.png", record_pos=(-0.018, -0.006), resolution=(1080, 2340)), "Filter文案显示正确")
#断言filter图片检查
assert_exists(Template(r"tpl1736478714007.png", record_pos=(-0.003, -0.49), resolution=(1080, 2340)), "Filte滤网图片显示正确")


#点击Clean滤网reset按钮，将滤网寿命恢复100%
poco("com.philips.ph.homecare:id/filter_item_clean_reset_id").click()
poco("com.philips.ph.homecare:id/dialog_filter_reset_check").click()
poco("com.philips.ph.homecare:id/dialog_filter_reset_apply").click()
sleep(3)
#断言当前clean滤网寿命为100%
assert_equal(poco("com.philips.ph.homecare:id/filter_item_clean_value_id").get_text(), "100%", "当前clean滤网寿命为100%")

#clean滤网已经显示100%，再次点击reset按钮，重置滤网寿命
poco("com.philips.ph.homecare:id/filter_item_clean_reset_id").click()
poco("com.philips.ph.homecare:id/dialog_filter_reset_check").click()
poco("com.philips.ph.homecare:id/dialog_filter_reset_apply").click()
sleep(3)
#断言当前clean滤网寿命为100%
assert_equal(poco("com.philips.ph.homecare:id/filter_item_clean_value_id").get_text(), "100%", "当前clean滤网寿命为100%")

#点击replace滤网reset按钮，将滤网寿命恢复100%
poco("com.philips.ph.homecare:id/filter_item_replace_reset_id").click()
poco("com.philips.ph.homecare:id/dialog_filter_reset_check").click()
poco("com.philips.ph.homecare:id/dialog_filter_reset_apply").click()
sleep(3)
#断言当前replace滤网寿命为100%
assert_equal(poco("com.philips.ph.homecare:id/filter_item_replace_value_id").get_text(), "100%", "当前replace滤网寿命为100%")

#Replace滤网已经显示100%，再次点击reset按钮，重置滤网寿命
poco("com.philips.ph.homecare:id/filter_item_replace_reset_id").click()
poco("com.philips.ph.homecare:id/dialog_filter_reset_check").click()
poco("com.philips.ph.homecare:id/dialog_filter_reset_apply").click()
sleep(3)
#断言当前replace滤网寿命为100%
assert_equal(poco("com.philips.ph.homecare:id/filter_item_replace_value_id").get_text(), "100%", "当前replace滤网寿命为100%")

# CH-150 Filter Purchase-Nano Protec Filter （87~98）
# CH-149 Filter Purchase-HEPA Filter （87~98）
# CH-148 Filter Purchase-Active Carbon Filter （87~98）
#滑动页面至购买链接处
swipe([718,1776],[718,1064])
#点击购买链接按钮
poco(text="Order filter").click()
sleep(5)
#断言已进入购买链接页面
assert_exists(Template(r"tpl1736475242612.png", record_pos=(-0.29, -0.763), resolution=(1080, 2340)), "已进入购买链接页面")

#退出购买链接页面，返回到device health页面
poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
#断言当前在device health页面
assert_equal(poco("android.widget.TextView").get_text(), "Device Health", "已进入device health页面")

# CH-146 Filter Life Time- Clean and Replacement Guide （101~142）
#点击clen重置滤网按钮
poco(text="How-to clean and reset the filter").click()
#断言cleaning guide页面文案检查
assert_exists(Template(r"tpl1736477304569.png", record_pos=(-0.011, -0.466), resolution=(1080, 2340)), "pre filter 清洁提示文案")
#断言cleaning图片检查
assert_exists(Template(r"tpl1736477540124.png", record_pos=(-0.004, 0.348), resolution=(1080, 2340)), "Pre filter清洁图片")


#返回到device health页面
poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
#断言当前在device health页面
assert_equal(poco("android.widget.TextView").get_text(), "Device Health", "已进入device health页面")

#点击replace重置滤网按钮
poco(text="How-to replace and reset the filter").click()
#断言cleaning guide页面文案检查
assert_exists(Template(r"tpl1736477733132.png", record_pos=(-0.011, -0.544), resolution=(1080, 2340)), "replace提示文案")

#断言replace滤网图片检查
assert_exists(Template(r"tpl1736477808653.png", record_pos=(0.006, 0.054), resolution=(1080, 2340)), "replace清洁图片")

#返回到device health页面
poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
#断言当前在device health页面
assert_equal(poco("android.widget.TextView").get_text(), "Device Health", "已进入device health页面")

#滑动页面至清洁sensor按钮处
swipe([722,1808],[722,808])
sleep(3)

#断言sensor文案显示
assert_exists(Template(r"tpl1736478078989.png", record_pos=(-0.005, 0.465), resolution=(1080, 2340)), "sensor文案显示正确")

#点击清洁sensor按钮
poco("com.philips.ph.homecare:id/filter_item_instruction_id").click()
#检查sensor页面内容显示
assert_exists(Template(r"tpl1736478169376.png", record_pos=(-0.001, 0.005), resolution=(1080, 2340)), "sensor页面显示正确")

#返回到device health页面
poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
#断言当前在device health页面
assert_equal(poco("android.widget.TextView").get_text(), "Device Health", "已进入device health页面")

#返回到设备控制页面
poco("Navigate up").click()
#返回到app主页
poco("com.android.systemui:id/back").click()
#断言当前是否在app主页
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(), "My Devices", "当前在App主页")









