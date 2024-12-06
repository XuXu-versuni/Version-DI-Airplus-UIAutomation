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
# https://nutriu.atlassian.net/browse/CH-2971 (27-48)
# https://nutriu.atlassian.net/browse/CH-2972 (52-78)
# https://nutriu.atlassian.net/browse/CH-2992 (82-84)
# https://nutriu.atlassian.net/browse/CH-2990 (87-93)
# https://nutriu.atlassian.net/browse/CH-2973 (97-117)
# https://nutriu.atlassian.net/browse/CH-2975 (121-123)
# https://nutriu.atlassian.net/browse/CH-2976 (125-130)

#启动Air+ app
start_app("com.philips.ph.homecare")
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")

# 本Shell对应的测试用例：https://nutriu.atlassian.net/browse/CH-2971
# 前置条件：第一次配网设备或者本地添加设备，才会有新功能卡片提示
# 进入设备控制页面
poco(desc="https://air-matters.com/app/philips/dark_mode/AC3420_10.png").click()
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(),"Air Quality","进入设备控制页面成功")
# 检查Al Enable卡片显示
assert_equal(poco("com.philips.ph.homecare:id/control_new_feature_btn").get_text(),"Enable now","Al Enable卡片显示正常")
# 检查Al卡片文案显示
assert_equal(poco("com.philips.ph.homecare:id/control_new_feature_msg").get_text(),"Enable Auto+ mode for the best performance at the lowest energy.","Al卡片文案展示正常")
# 关闭Al卡片
poco("com.philips.ph.homecare:id/control_new_feature_close").click()
# assert_not_exists(Template(r"tpl1730963666599.png", record_pos=(0.017, -0.159), resolution=(1080, 2412)), "关闭Al卡片成功")
assert_equal(poco("com.philips.ph.homecare:id/control_new_feature_btn").get_text(),"Learn more","smart scenario卡片显示正常")
# 检查smart scenario卡片文案显示
assert_exists(Template(r"tpl1730966798888.png", record_pos=(-0.042, -0.215), resolution=(1080, 2412)), "smart scenario卡片文案显示正常")
# 点击Learn more按钮，进入schedule页面
poco("com.philips.ph.homecare:id/control_new_feature_btn").click()
sleep(6.0)
assert_equal(poco("android.widget.TextView").get_text(),"Scheduler","Schedule页面进入成功")
# 返回上一级页面
poco("Navigate up").click()
# 关闭smart scenario卡片
poco("com.philips.ph.homecare:id/control_new_feature_close").click()
assert_not_exists(Template(r"tpl1730963787945.png", record_pos=(-0.017, -0.188), resolution=(1080, 2412)), "关闭smart scenario卡片成功")

# 本Shell对应的测试用例：https://nutriu.atlassian.net/browse/CH-2972    
sleep(3.0)
swipe([874,1257],[874,29])
# 进入schedule页面，检查smart schedule卡片显示
poco("com.philips.ph.homecare:id/purifier_control_schedule").click()
assert_equal(poco("android.widget.TextView").get_text(),"Scheduler","Schedule页面进入成功")
assert_equal(poco("com.philips.ph.homecare:id/schedule_scenario_item_title").get_text(),"Fresh wake-up","Fresh wake-up卡片展示正常")
assert_exists(Template(r"tpl1731034084365.png", record_pos=(-0.151, -0.093), resolution=(1080, 2412)), "Fresh bedtime卡片展示正常")
# 检查Fresh wake-up任务默认显示
poco(text="Fresh wake-up").click()
sleep(3.0)
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_title").get_text(),"Fresh wake-up","任务卡片展示正常，且文案显示正常")
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_subtitle").get_text(),"Wake up to a fresh & clean bedroom","任务卡片展示正常，且文案显示正常")
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_desc").get_text(),"30min before your set wake-up time, the purifier will slowly start ramping up power, to give you a fresh morning.","任务卡片展示正常，且文案显示正常")
sleep(6.0)
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_time").get_text(),"08:00","默认结束时间显示为08：00")
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_time_desc").get_text(),"Starts at 07:30","默认开始时间显示为07：30")
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_light").attr("checked"),True,"默认灯光是打开状态")
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_light_desc").get_text(),"Light turns on gradually, to mimic sunrise","wake-up灯光文案显示正确")
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_repeat_section").get_text(),"Repeat every...","每天重复运行时间文案显示正确")
# 每天循环运行时间是默认全选的状态
assert_equal(poco("com.philips.ph.homecare:id/schedule_monday_btn").attr("checked"),True,"1每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/schedule_tuesday_btn").attr("checked"),True,"2每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/schedule_wednesday_btn").attr("checked"),True,"3每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/schedule_thursday_btn").attr("checked"),True,"4每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/schedule_friday_btn").attr("checked"),True,"5每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/schedule_saturday_btn").attr("checked"),True,"6每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/schedule_sunday_btn").attr("checked"),True,"7每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_done").get_text(),"Done","Done按钮显示正常")

# 本shell对应的测试用例：https://nutriu.atlassian.net/browse/CH-2992
# 设置一条Fresh wake-up任务
poco("com.philips.ph.homecare:id/smart_scenario_edit_done").click()
assert_equal(poco("com.philips.ph.homecare:id/schedule_scenario_item_status").get_text(),"ON","打开状态显示正确")
assert_equal(poco("com.philips.ph.homecare:id/schedule_scenario_item_subtitle").get_text(),"07:30 - 08:00","设置成功后的时间显示正确")

# 本shell对应的测试用例：https://nutriu.atlassian.net/browse/CH-2990
# 再次进入Fresh wake-up页面，可以disable schedule
poco(text="Fresh wake-up").click()
sleep(6.0)
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_disable").get_text(),"Disable scheduler","disable schedule按钮显示正常")
poco("com.philips.ph.homecare:id/smart_scenario_edit_disable").click()
# Fresh wake-up恢复默认状态(紧用任务成功)
assert_equal(poco("com.philips.ph.homecare:id/schedule_scenario_item_status").get_text(),"OFF","Fresh wake-up恢复默认状态")


# 本shell对应的测试用例：https://nutriu.atlassian.net/browse/CH-2973
sleep(3.0)
# 检查Fresh bedtime任务默认显示
poco(text="Fresh bedtime").click()
sleep(3.0)
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_title").get_text(),"Fresh bedtime","任务卡片展示正常，且文案显示正常")
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_subtitle").get_text(),"Fall asleep in a fresh & clean bedroom","任务卡片展示正常，且文案显示正常")
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_desc").get_text(),"1hr before your set bedtime, the device goes into Turbo mode for 15min. The next 45min it switches to quiet Sleep mode.","任务卡片展示正常，且文案显示正常")
sleep(3.0)
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_time").get_text(),"11:00","默认结束时间显示为11：00")
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_time_desc").get_text(),"Starts at 10:00","默认开始时间显示为10:00")
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_light").attr("checked"),True,"默认灯光是打开状态")
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_light_desc").get_text(),"Dim light that switches off at your set bedtime","bedtime灯光文案显示正确")
# 每天循环运行时间是默认全选的状态
assert_equal(poco("com.philips.ph.homecare:id/schedule_monday_btn").attr("checked"),True,"1每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/schedule_tuesday_btn").attr("checked"),True,"2每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/schedule_wednesday_btn").attr("checked"),True,"3每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/schedule_thursday_btn").attr("checked"),True,"4每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/schedule_friday_btn").attr("checked"),True,"5每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/schedule_saturday_btn").attr("checked"),True,"6每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/schedule_sunday_btn").attr("checked"),True,"7每天重复时间都是默认选中的")
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_done").get_text(),"Done","Done按钮显示正常")

# 本shell对应的测试用例：https://nutriu.atlassian.net/browse/CH-2975
# 设置一条Fresh bedtime任务
poco("com.philips.ph.homecare:id/smart_scenario_edit_done").click()
assert_exists(Template(r"tpl1732865927388.png", threshold=0.98, record_pos=(0.015, -0.039), resolution=(1080, 2412)), "bedtime设置成功后的显示状态正确")

# 本shell对应的测试用例:https://nutriu.atlassian.net/browse/CH-2976
sleep(3.0)
poco(text="Fresh bedtime").click()
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_disable").get_text(),"Disable scheduler","disable schedule按钮显示正常")
poco("com.philips.ph.homecare:id/smart_scenario_edit_disable").click()
# Fresh bedtime恢复默认状态(禁用任务成功)
assert_exists(Template(r"tpl1732866419069.png", record_pos=(0.022, -0.046), resolution=(1080, 2412)), "Fresh bedtime恢复默认状态")











