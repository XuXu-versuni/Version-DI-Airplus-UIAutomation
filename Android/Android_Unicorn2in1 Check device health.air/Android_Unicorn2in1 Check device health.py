# -*- encoding=utf8 -*-
__author__ = "Mengjie"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
#poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

# 本shell对应的测试用例：
# https://nutriu.atlassian.net/browse/CH-139 (Filter Life Time-Pre-filter)
# https://nutriu.atlassian.net/browse/CH-1630（Fliter - Reset filter (App)）
# https://nutriu.atlassian.net/browse/CH-140（Filter Life Time-Wick Filter）
# https://nutriu.atlassian.net/browse/CH-146（Filter Life Time- Clean and Replacement Guide）

#启动Air+ app
start_app("com.philips.ph.homecare")
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")
# 进入设备控制页面
poco(desc="https://air-matters.com/app/philips/dark_mode/AC3420_10.png").click()
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([-0.0213, -0.6634])

# https://nutriu.atlassian.net/browse/CH-139
# 设备控制页面Device Health部分的检查
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_health").get_text(),"Device Health","Device Health文案显示")
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_health_text").get_text(),"Pollutants in, clean air out. Your device is working great.","建议文案显示")
assert_equal(poco("com.philips.ph.homecare:id/filter_item_name_id").get_text(),"Filter","Filter显示")
assert_equal(poco("com.philips.ph.homecare:id/filter_item_clean_action_id").get_text(),"Clean","Clean文案检查")
assert_exists(Template(r"tpl1736405024721.png", threshold=0.98, record_pos=(0.141, 0.231), resolution=(1080, 2412)), "Replace文案检查")
# Device Health页面的清洁和替换滤网检查
poco(text="Device Health").click()
assert_equal(poco("android.widget.TextView").get_text(),"Device Health","Device Health页面打开成功")
assert_equal(poco("com.philips.ph.homecare:id/filter_item_name_id").get_text(),"Filter","Filter文案显示")
assert_equal(poco("com.philips.ph.homecare:id/filter_item_desc_id").get_text(),"Our integrated cylindrical filter combines 3-layers: HEPA NanoProtect, Active Carbon and Pre-filter, to make sure you are fully protected from viruses, bacteria, pollen, dust, PM2.5, pet dander and gases.","Filter解释文案显示")

# https://nutriu.atlassian.net/browse/CH-1630
# 重置清洁滤网
poco("com.philips.ph.homecare:id/filter_item_clean_reset_id").click()
poco(text="Yes, I’m sure").click()
poco(text="Reset").click()
assert_equal(poco("com.philips.ph.homecare:id/filter_item_clean_value_id").get_text(),"100%","清洁滤网重置到100%")
# 重置替换滤网
poco("com.philips.ph.homecare:id/filter_item_replace_reset_id").click()
poco(text="Yes, I’m sure").click()
poco(text="Reset").click()
assert_equal(poco("com.philips.ph.homecare:id/filter_item_replace_value_id").get_text(),"100%","替换滤网重置到100%")

# https://nutriu.atlassian.net/browse/CH-146
# 检查清洁滤网和滤网重置Guide
poco(text="How-to clean and reset the filter").click()
# assert_equal(poco("android.widget.TextView").get_text(),"Cleaning the surface of the filter","检查Guide页面文案显示")
assert_exists(Template(r"tpl1736491516926.png", threshold=0.98, record_pos=(-0.008, -0.675), resolution=(1080, 2412)), "检查Guide页面文案显示")

# assert_equal(poco("android.widget.TextView").get_text(),"Warning: If you have allergies, please take protective measures or seek assistance when cleaning the filter.","滤网警告文案")
assert_exists(Template(r"tpl1736491387117.png", threshold=0.98, record_pos=(-0.011, -0.379), resolution=(1080, 2412)), "滤网警告文案")

assert_exists(Template(r"tpl1736488624721.png", threshold=0.98, record_pos=(-0.004, 0.125), resolution=(1080, 2412)), "检查滤网清洁图片指导")
# 返回上一级页面
poco(desc="关闭标签页").click()
# 检查替换滤网和滤网重置Guide
poco(text="How-to replace and reset the filter").click()
# assert_equal(poco("android.widget.TextView").get_text(),"Replacing the filter","检查Guide页面文案显示")
assert_exists(Template(r"tpl1736491549828.png", threshold=0.98, record_pos=(-0.128, -0.72), resolution=(1080, 2412)), "检查Guide页面文案显示")

# assert_equal(poco("android.widget.TextView").get_text(),"Warning: If you have allergies, please take protective measures or seek assistance when cleaning the filter.","滤网警告文案")
assert_exists(Template(r"tpl1736491422698.png", threshold=0.98, record_pos=(-0.009, -0.455), resolution=(1080, 2412)), "滤网警告文案")

assert_exists(Template(r"tpl1736488920008.png", threshold=0.98, record_pos=(0.003, 0.035), resolution=(1080, 2412)), "检查滤网替换图片指导")
# 返回上一级页面
poco(desc="关闭标签页").click()

# https://nutriu.atlassian.net/browse/CH-140
poco("com.philips.ph.homecare:id/filter_item_container_id").swipe([-0.2119, -0.7575])
# Wick滤网检查
assert_equal(poco("com.philips.ph.homecare:id/filter_wick_name_id").get_text(),"Wick","Wick文案检查")
assert_equal(poco("com.philips.ph.homecare:id/filter_wick_desc_id").get_text(),"Our humidification filters are equipped with NanoCloud technology, to humidify the air hygienically. NanoCloud emits only pure water molecules into the air and avoids white dust and wet floors around the device.","Wick滤网解释文案显示")
assert_equal(poco("com.philips.ph.homecare:id/filter_wick_action_id").get_text(),"Replace","Wick的Replace文案检查")

# https://nutriu.atlassian.net/browse/CH-1630
# Wick滤网重置
poco("com.philips.ph.homecare:id/filter_wick_reset_id").click()
poco(text="Yes, I’m sure").click()
poco(text="Reset").click()
assert_equal(poco("com.philips.ph.homecare:id/filter_wick_value_id").get_text(),"100%","Wick滤网重置到100%")

# https://nutriu.atlassian.net/browse/CH-146
# Wick滤网清洁Guide
poco(text="How to clean the humidification filter").click()
assert_equal(poco("android.widget.TextView").get_text(),"How-to clean the humidification filter","检查Guide页面的Wick滤网清洁文案显示")
assert_exists(Template(r"tpl1736489882474.png", threshold=0.98, record_pos=(0.007, -0.176), resolution=(1080, 2412)), "检查Wick滤网清洁页面的指导图片")
# 返回上一级页面
poco(desc="关闭标签页").click()
# Wick滤网替换Guide
poco(text="How to replace the humidification filter").click()
assert_equal(poco("android.widget.TextView").get_text(),"Replacing the filter","检查Guide页面的Wick滤网替换文案显示")
assert_exists(Template(r"tpl1736490197593.png", threshold=0.98, record_pos=(0.007, -0.264), resolution=(1080, 2412)), "检查Wick滤网替换页面的指导图片")
# 返回上一级页面
poco(desc="关闭标签页").click()
poco("com.philips.ph.homecare:id/filter_wick_container_id").swipe([-0.0952, -0.7314])
# 检查Sensor显示
assert_equal(poco("com.philips.ph.homecare:id/filter_item_name_id").get_text(),"Sensor"," 检查Sensor文案显示")
assert_equal(poco("com.philips.ph.homecare:id/filter_item_desc_id").get_text(),"Clean the sensor every 2 months so it can continue to provide accurate measures of the air quality. Sensors of devices in a dusty room should be cleaned more frequently.","Sensor解释文案显示")
# 检查Sensor清洁Guide
poco(text="How to clean the sensor").click()
assert_equal(poco("android.widget.TextView").get_text(),"Cleaning the air quality sensor","检查Sensor清洁指导页面的文案显示")
assert_exists(Template(r"tpl1736490648448.png", threshold=0.98, record_pos=(0.006, -0.182), resolution=(1080, 2412)), "检查Sensor清洁页面的指导图片")
# 返回上一级页面
poco(desc="关闭标签页").click()
# 返回到app主页
poco(desc="Navigate up").click()
poco(desc="返回").click()





