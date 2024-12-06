# -*- encoding=utf8 -*-
__author__ = "xuxu"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device

poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)



#本自动化脚本是基于nala这个设备进行



#确认设备在staging 环境已经配置完毕
#确认设备已经在线，历史数据清零
#默认设备开机


# # 定义元素的路径
# power_btn = Template("com.philips.ph.homecare:id/dashboard_control_power_btn")
# # 检查元素是否存在
# if exists(power_btn):
#     # 获取元素的checked属性
#     is_checked = power_btn.get_attribute('checked')
    
#     # 判断checked属性是否为False（关机状态）
#     if is_checked == 'false' or is_checked is False:
#         # 如果是关机状态，则点击按钮开机
#         touch(power_btn)
#         print("设备已开机")
#     else:
#         print("设备已经是开机状态")
# else:
#     print("未找到电源按钮")
    
    
#找到Controls功能项
poco("com.philips.ph.homecare:id/purifier_control_schedule").click()
#触发wake-up
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/fragment_container_id").offspring("com.philips.ph.homecare:id/schedule_list_recycler_id").child("com.philips.ph.homecare:id/schedule_item_layout_id")[0].click()
#不做改动直接done
poco("com.philips.ph.homecare:id/smart_scenario_edit_done").click()
#wake-up在app展示正确，判断功能有效
assert_equal(poco("com.philips.ph.homecare:id/schedule_scenario_item_subtitle").get_text(), "07:30 - 08:00", "时间展示正确，断言有效，功能开启")

#wake-up进行功能修改
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/fragment_container_id").offspring("com.philips.ph.homecare:id/schedule_list_recycler_id").child("com.philips.ph.homecare:id/schedule_item_layout_id")[0].click()
#修改时间
poco("com.philips.ph.homecare:id/smart_scenario_edit_time").click()
poco("com.philips.ph.homecare:id/time_pick_sheet_hour").swipe([-0.0072, -0.0562])
poco("com.philips.ph.homecare:id/time_pick_sheet_apply").click()

#判断修改时间正确与否
assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_time").get_text(), "10:00", "时间修改正确，断言有效，功能开启")

#修改wake-up的light
poco("com.philips.ph.homecare:id/smart_scenario_edit_light").click()
poco("com.philips.ph.homecare:id/smart_scenario_edit_done").click()
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/fragment_container_id").offspring("com.philips.ph.homecare:id/schedule_list_recycler_id").child("com.philips.ph.homecare:id/schedule_item_layout_id")[0].click()
#用attr获取属性判断修改light是否生效
assert_equal(str(poco(name="com.philips.ph.homecare:id/smart_scenario_edit_light").attr("checked")), "True", "控件的属性值为True")

#用EQUAL判断页面的文字有没有变动
a  = "30min before your set wake-up time, the purifier will slowly start ramping up power, to give you a fresh morning."
b = "30min before your set wake-up time, the purifier will slowly start ramping up power, to give you a fresh morning."
assert_equal(a,b,msg ="assert a==b")
#也可以用获取属性text值来判断是否有变化

assert_equal(poco("com.philips.ph.homecare:id/smart_scenario_edit_desc").get_text(),"30min before your set wake-up time, the purifier will slowly start ramping up power, to give you a fresh morning.","这个页面的属性文字没哟变化！！测试通过！")

poco("com.philips.ph.homecare:id/smart_scenario_edit_done").click()
poco("com.philips.ph.homecare:id/coordinator").click()

#测试完毕，所有数据清零！！！
poco("com.philips.ph.homecare:id/smart_scenario_edit_disable").click()
poco("com.philips.ph.homecare:id/smart_scenario_edit_desc").click()
poco("com.philips.ph.homecare:id/smart_scenario_edit_disable").click()
poco("com.philips.ph.homecare:id/smart_scenario_edit_time").click()
# 清除timer task
poco("com.philips.ph.homecare:id/schedule_remove_btn").click()
poco("android:id/button1").click()

#清除power off的task
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/fragment_container_id").offspring("android.widget.LinearLayout").child("com.philips.ph.homecare:id/schedule_item_layout_id").click()
poco("com.philips.ph.homecare:id/schedule_remove_btn").click()
poco("android:id/button1").click()
#页面检测完成，返回setting详情页面
poco("Navigate up").click()
























