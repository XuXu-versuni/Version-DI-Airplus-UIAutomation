# -*- encoding=utf8 -*-
__author__ = "Mengjie"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
#poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

# 本次shell对应的测试用例：
# https://nutriu.atlassian.net/browse/CH-2994（这条case涵盖了CH-1258,CH-1185,CH-1186,CH-1177)
# https://nutriu.atlassian.net/browse/CH-1258 (30-31)
# https://nutriu.atlassian.net/browse/CH-1185 (33-34)
# https://nutriu.atlassian.net/browse/CH-1186 （36-37）
# https://nutriu.atlassian.net/browse/CH-1177 （39-40）  
# https://nutriu.atlassian.net/browse/CH-1257 （42-44）
# https://nutriu.atlassian.net/browse/CH-1583 (48-54)
# https://nutriu.atlassian.net/browse/CH-1584 (57-62)
# https://nutriu.atlassian.net/browse/CH-3499 (65-70)
# https://nutriu.atlassian.net/browse/CH-1586 (73-78)
# https://nutriu.atlassian.net/browse/CH-1587 （87-106）
# https://nutriu.atlassian.net/browse/CH-2995 (125-131)
# https://nutriu.atlassian.net/browse/CH-2998 （134-140）
# https://nutriu.atlassian.net/browse/CH-2996 (143-148)
# https://nutriu.atlassian.net/browse/CH-2997 (151-173)
# https://nutriu.atlassian.net/browse/CH-3502 （168-182）
# https://nutriu.atlassian.net/browse/CH-3500 (186-222)
    
#启动Air+ app
start_app("com.philips.ph.homecare")
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")
#检查Unicorn2in1设备按钮的默认显示（在检查之前先恢复厂测模式）
# 检查设备默认状态显示：https://nutriu.atlassian.net/browse/CH-2994
# 开关按钮：打开状态；童锁按钮：关闭；模式按钮：Auto；湿度按钮：50%；Lamp modes：Air Quality；风速按钮：Auto；灯光亮度按钮：Automatic；Timer按钮：off
poco(desc="https://air-matters.com/app/philips/dark_mode/AC3420_10.png").click()
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(),"Air Quality","进入设备控制页面成功")
swipe([744,1427],[744,500])
assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"),True,"设备默认是开机状态")

# https://nutriu.atlassian.net/browse/CH-1258
assert_equal(poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").attr("checked"),False,"童锁默认是关闭状态")

# https://nutriu.atlassian.net/browse/CH-1185
assert_exists(Template(r"tpl1733209837798.png", threshold=0.98, record_pos=(-0.194, -0.106), resolution=(1080, 2412)), "默认模式显示Auto")

# https://nutriu.atlassian.net/browse/CH-1186
assert_exists(Template(r"tpl1733210221495.png", threshold=0.98, record_pos=(-0.199, 0.269), resolution=(1080, 2412)), "Lamp mode默认显示Air Auality，灯光亮度默认显示Automatic")

# https://nutriu.atlassian.net/browse/CH-1177 
assert_exists(Template(r"tpl1733210597381.png", threshold=0.98, record_pos=(0.218, 0.194), resolution=(1080, 2412)), "风速默认显示Auto")
assert_exists(Template(r"tpl1733213423333.png", threshold=0.98, record_pos=(0.219, 0.305), resolution=(1080, 2412)), "Timer的默认显示为off")

# https://nutriu.atlassian.net/browse/CH-1257
swipe([744,500],[744,1427])
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_pr_name").get_text(),"PM2.5","设备和app上的首选指数默认显示PM2.5")

# https://nutriu.atlassian.net/browse/CH-1583
swipe([744,1427],[744,500])
# 设置模式为Auto模式
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Auto").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733209837798.png", threshold=0.98, record_pos=(-0.194, -0.106), resolution=(1080, 2412)), "模式设置Auto成功")

# https://nutriu.atlassian.net/browse/CH-1584
# 设置模式为Sleep模式
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Sleep").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733214013995.png", threshold=0.98, record_pos=(-0.178, 0.009), resolution=(1080, 2412)), "模式设置Sleep成功")

# https://nutriu.atlassian.net/browse/CH-3499
# 设置模式为Medium模式
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Medium").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733214131660.png", threshold=0.98, record_pos=(-0.203, 0.004), resolution=(1080, 2412)), "模式设置Medium成功")

# https://nutriu.atlassian.net/browse/CH-1586
# 设置模式为Turbo模式
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Turbo").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733214203501.png", threshold=0.98, record_pos=(-0.203, 0.002), resolution=(1080, 2412)), "模式设置Turbo成功")

# 恢复Auto模式
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Auto").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733209837798.png", threshold=0.98, record_pos=(-0.194, -0.106), resolution=(1080, 2412)), "模式设置Auto成功")

# https://nutriu.atlassian.net/browse/CH-1587
# 先进入AI页面，打开此功能
swipe([744,1427],[744,-500])
poco(text="Device Settings").click()
assert_equal(poco("android.widget.TextView").get_text(),"Settings","Settings页面进入成功")
swipe([744,1427],[744,500])
poco(text="Auto+ mode (Beta)").click()
# 检查AI功能默认是关闭状态
assert_equal(poco("com.philips.ph.homecare:id/autoplus_switch_id").attr("checked"),False,"AI功能默认是关闭状态")
# 打开AI功能
poco(text="Enable Auto to Auto+").click()
sleep(3.0)
assert_equal(poco("com.philips.ph.homecare:id/autoplus_switch_id").attr("checked"),True,"AI功能打开成功")
# 返回上一级页面
poco(desc="Navigate up").click()
swipe([744,500],[744,1427])
# 返回到设备控制页面
poco(desc="Navigate up").click()
swipe([744,500],[744,1427])
# 检查Auto模式变为Auto+模式
assert_exists(Template(r"tpl1733367489577.png", threshold=0.98, record_pos=(-0.197, -0.074), resolution=(1080, 2412)), "Auto+模式显示正确")
# AI功能关闭
swipe([744,1427],[744,-500])
poco(text="Device Settings").click()
assert_equal(poco("android.widget.TextView").get_text(),"Settings","Settings页面进入成功")
swipe([744,1427],[744,500])
poco(text="Auto+ mode (Beta)").click()
poco(text="Enable Auto to Auto+").click()
assert_equal(poco("com.philips.ph.homecare:id/autoplus_switch_id").attr("checked"),False,"AI关闭成功")
poco(desc="Navigate up").click()
swipe([744,500],[744,1427])
poco(desc="Navigate up").click()
swipe([744,500],[744,1427])
# AI功能关闭成功，并且Auto+模式变为Auto模式
assert_exists(Template(r"tpl1733209837798.png", threshold=0.98, record_pos=(-0.194, -0.106), resolution=(1080, 2412)), "Auto+模式切为Auto模式成功")

# https://nutriu.atlassian.net/browse/CH-2995
# 设置工作模式为Sleep模式
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Sleep").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733214013995.png", threshold=0.98, record_pos=(-0.178, 0.009), resolution=(1080, 2412)), "模式设置Sleep成功")
assert_exists(Template(r"tpl1733210221495.png", threshold=0.98, record_pos=(-0.199, 0.269), resolution=(1080, 2412)), "Lamp mode默认显示Air Auality，灯光亮度默认显示Automatic")

# https://nutriu.atlassian.net/browse/CH-2998
# 风速设置为1，模式按钮显示为manual
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco(text="1").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733385471560.png", threshold=0.98, record_pos=(0.205, 0.473), resolution=(1080, 2412)), "风速1设置成功")
assert_exists(Template(r"tpl1733385524764.png", threshold=0.98, record_pos=(-0.209, 0.315), resolution=(1080, 2412)), "工作模式变为manual")

# https://nutriu.atlassian.net/browse/CH-2996
# 灯光设置为off，工作模式不变
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Off").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733385524764.png", threshold=0.98, record_pos=(-0.209, 0.315), resolution=(1080, 2412)), "工作模式变为manual")

# https://nutriu.atlassian.net/browse/CH-2997
# 灯光亮度设置为Automatic，检查Lamp modes显示Air Quality
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Automatic").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733386686679.png", threshold=0.98, record_pos=(-0.194, 0.538), resolution=(1080, 2412)), "灯光亮度设置为Automatic，Lamp modes显示Air Quality")
# 灯光亮度设置为Bright，检查Lamp modes显示Air Quality
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Bright").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733386801580.png", threshold=0.98, record_pos=(-0.195, 0.545), resolution=(1080, 2412)), "灯光亮度设置为Bright，Lamp modes显示Air Quality")
# 灯光亮度设置为Low，检查Lamp modes显示Air Quality
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Low").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733386907879.png", threshold=0.98, record_pos=(-0.205, 0.544), resolution=(1080, 2412)), "灯光亮度设置为Low，检查Lamp modes显示Air Quality")
# 灯光亮度恢复到Automatic
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Automatic").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733471694408.png", threshold=0.98, record_pos=(-0.205, 0.283), resolution=(1080, 2412)), "灯光亮度显示Automatic")

# https://nutriu.atlassian.net/browse/CH-3502
# Lamp modes设置为Ambient，工作模式设置为Sleep，检查灯光亮度显示状态和灯光模式显示状态
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco(text="Ambient").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Sleep").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733468069608.png", threshold=0.98, record_pos=(-0.203, 0.144), resolution=(1080, 2412)), "灯光亮度显示状态和灯光模式显示状态都不变，保持用户设置")
# Lamp modes设置为Air Quality，工作模式设置为Sleep，检查灯光亮度显示状态和灯光模式显示状态
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco(text="Air Quality").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733468249005.png", threshold=0.98, record_pos=(-0.197, 0.135), resolution=(1080, 2412)), "App灯光亮度显示状态和灯光模式显示状态显示不变，保持用户设置；设备上灯3s后灭掉")


# https://nutriu.atlassian.net/browse/CH-3500
# 设置风速1
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco(text="1").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733470421528.png", threshold=0.98, record_pos=(0.216, 0.321), resolution=(1080, 2412)), "风速键显示1")
assert_exists(Template(r"tpl1733470430614.png", threshold=0.98, record_pos=(-0.205, 0.16), resolution=(1080, 2412)), "工作模式键显示manual")
# 设置风速2
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco(text="2").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733470550643.png", record_pos=(0.23, 0.316), resolution=(1080, 2412)), "风速键显示2")
assert_exists(Template(r"tpl1733470430614.png", threshold=0.98, record_pos=(-0.205, 0.16), resolution=(1080, 2412)), "工作模式键显示manual")
# 设置风速3
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco(text="3").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733470615186.png", record_pos=(0.222, 0.316), resolution=(1080, 2412)), "风速键显示3")
assert_exists(Template(r"tpl1733470430614.png", threshold=0.98, record_pos=(-0.205, 0.16), resolution=(1080, 2412)), "工作模式键显示manual")
# 设置风速4
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco(text="4").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733470697238.png", record_pos=(0.222, 0.311), resolution=(1080, 2412)), "风速键显示4")
assert_exists(Template(r"tpl1733470430614.png", threshold=0.98, record_pos=(-0.205, 0.16), resolution=(1080, 2412)), "工作模式键显示manual")
# 设置风速5
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco(text="5").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733470754566.png", record_pos=(0.22, 0.321), resolution=(1080, 2412)), "风速键显示5")
assert_exists(Template(r"tpl1733470430614.png", threshold=0.98, record_pos=(-0.205, 0.16), resolution=(1080, 2412)), "工作模式键显示manual")
# 设置工作模式为Auto
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Auto").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1733209837798.png", threshold=0.98, record_pos=(-0.194, -0.106), resolution=(1080, 2412)), "模式设置Auto成功")
assert_exists(Template(r"tpl1733470822364.png", record_pos=(0.223, 0.322), resolution=(1080, 2412)), "风速键显示Auto")























