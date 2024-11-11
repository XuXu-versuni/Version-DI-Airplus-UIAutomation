# -*- encoding=utf8 -*-
__author__ = "Mengjie"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
#poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)
'''
本Shell对应的总的测试用例：
https://nutriu.atlassian.net/browse/CH-3114
https://nutriu.atlassian.net/browse/CH-3115
https://nutriu.atlassian.net/browse/CH-3116
https://nutriu.atlassian.net/browse/CH-3117
https://nutriu.atlassian.net/browse/CH-3118
https://nutriu.atlassian.net/browse/CH-3119

'''
#启动Air+ app
start_app("com.philips.ph.homecare")
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")
# 进入设备控制页面
poco(desc="https://air-matters.com/app/philips/dark_mode/CX3120_01.png").click()
swipe([806,1814],[809,449])
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(),"Temperature around device","控制页面进入成功")
# Prometheus设备的打开和关闭功能


'''
这里需要说明一下，设备状态在执行脚本的时候尽量都是关闭状态，切本脚本执行完毕之后要恢复所有数据到一个默认状态，注意修改代码中的阈值的大小以便测试准确性
'''


# 关闭功能
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()

sleep(2.0)
assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"),False,"关闭成功")

# 打开功能
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"),True,"打开成功")


# 本Shell对应的测试用例：https://nutriu.atlassian.net/browse/CH-3115

# 设置Auto mode，这里的设备状态是在关闭AI功能的情况下
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Auto").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# 阈值根据机型适配，注意修改你本地的阈值
assert_exists(Template(r"tpl1730874755774.png", threshold=0.95, record_pos=(-0.206, 0.354), resolution=(1080, 2412)),"Auto mode设置成功")


# 本Shell对应的测试用例: https://nutriu.atlassian.net/browse/CH-3116

# 设置High mode
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="High").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# 阈值根据机型适配
assert_exists(Template(r"tpl1730875036187.png", threshold=0.95, record_pos=(-0.191, 0.278), resolution=(1080, 2412)),"High mode设置成功")


# 本Shell对应的测试用例: https://nutriu.atlassian.net/browse/CH-3117

# 设置Low mode
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Low").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# 阈值根据机型适配
assert_exists(Template(r"tpl1730875222501.png", threshold=0.98, record_pos=(-0.194, 0.289), resolution=(1080, 2412)),"Low mode设置成功")


# 本Shell对应的测试用例: https://nutriu.atlassian.net/browse/CH-3118

# 设置Medium mode
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Medium").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# 阈值根据机型适配
assert_exists(Template(r"tpl1730875392422.png", threshold=0.98, record_pos=(-0.194, 0.283), resolution=(1080, 2412)),"Medium mode设置成功")


# 本Shell对应的测试用例: https://nutriu.atlassian.net/browse/CH-3119

# 设置Ventilation mode
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Ventilation").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# 阈值根据机型适配
assert_exists(Template(r"tpl1730880379003.png", threshold=0.98, record_pos=(-0.206, 0.623), resolution=(1080, 2412)),"Ventilation mode设置成功")





#text("c8f815c9175211ef93b3d1205527f292")


