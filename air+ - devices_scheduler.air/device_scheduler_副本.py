#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   device_scheduler.py    
@Version:  python3.7 
@Software: PyCharm 
@Contact :   xfdzl5256@126.com
@Author  :   xfdzl
@Modify Time            @Version    @Desciption
------------            --------    -----------
2024/12/6 下午1:40         1.0         None
"""

# -*- encoding=utf8 -*-
__author__ = "xuxu"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# 初始化设备和 Poco 对象
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)


def check_and_turn_on_device():
    # 定义电源按钮路径（假设使用Template对象）
    power_btn = Template("com.philips.ph.homecare:id/dashboard_control_power_btn")

    if exists(power_btn):
        is_checked = power_btn.get_attribute('checked')
        if is_checked in ['false', False]:
            touch(power_btn)
            print("设备已开机")
        else:
            print("设备已经是开机状态")
    else:
        print("未找到电源按钮")


def configure_wake_up_schedule():
    # 找到并点击 Controls 功能项
    poco("com.philips.ph.homecare:id/purifier_control_schedule").click()

    # 触发 wake-up
    schedule_item = \
    poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring(
        "com.philips.ph.homecare:id/fragment_container_id").offspring(
        "com.philips.ph.homecare:id/schedule_list_recycler_id").child(
        "com.philips.ph.homecare:id/schedule_item_layout_id")[0]
    schedule_item.click()

    # 不做改动直接完成
    poco("com.philips.ph.homecare:id/smart_scenario_edit_done").click()


def verify_wake_up_display():
    # 验证 wake-up 在 app 中展示正确
    expected_time = "07:30 - 08:00"
    actual_time = poco("com.philips.ph.homecare:id/schedule_scenario_item_subtitle").get_text()
    assert actual_time == expected_time, f"时间展示不正确，预期: {expected_time}, 实际: {actual_time}"


def modify_wake_up_schedule():
    # 修改 wake-up 时间和光照设置
    schedule_item = \
    poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring(
        "com.philips.ph.homecare:id/fragment_container_id").offspring(
        "com.philips.ph.homecare:id/schedule_list_recycler_id").child(
        "com.philips.ph.homecare:id/schedule_item_layout_id")[0]
    schedule_item.click()

    # 修改时间
    poco("com.philips.ph.homecare:id/smart_scenario_edit_time").click()
    poco("com.philips.ph.homecare:id/time_pick_sheet_hour").swipe([-0.0072, -0.0562])
    poco("com.philips.ph.homecare:id/time_pick_sheet_apply").click()

    # 验证修改的时间是否正确
    expected_time = "10:00"
    actual_time = poco("com.philips.ph.homecare:id/smart_scenario_edit_time").get_text()
    assert actual_time == expected_time, f"时间修改不正确，预期: {expected_time}, 实际: {actual_time}"

    # 修改光照设置
    poco("com.philips.ph.homecare:id/smart_scenario_edit_light").click()
    poco("com.philips.ph.homecare:id/smart_scenario_edit_done").click()

    # 验证光照设置是否生效
    light_is_checked = str(poco(name="com.philips.ph.homecare:id/smart_scenario_edit_light").attr("checked")) == "True"
    assert light_is_checked, "光照设置未生效"


def verify_page_text():
    # 验证页面文本是否有变动
    expected_text = "30min before your set wake-up time, the purifier will slowly start ramping up power, to give you a fresh morning."
    actual_text = poco("com.philips.ph.homecare:id/smart_scenario_edit_desc").get_text()
    assert actual_text == expected_text, "页面文本发生了变化"


def cleanup():
    # 测试完毕后清理数据
    poco("com.philips.ph.homecare:id/smart_scenario_edit_disable").click()
    poco("com.philips.ph.homecare:id/smart_scenario_edit_desc").click()
    poco("com.philips.ph.homecare:id/smart_scenario_edit_disable").click()
    poco("com.philips.ph.homecare:id/smart_scenario_edit_time").click()

    # 清除 timer task
    poco("com.philips.ph.homecare:id/schedule_remove_btn").click()
    poco("android:id/button1").click()

    # 清除 power off 的任务
    power_off_task = poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring(
        "android:id/content").offspring("com.philips.ph.homecare:id/fragment_container_id").offspring(
        "android.widget.LinearLayout").child("com.philips.ph.homecare:id/schedule_item_layout_id")
    power_off_task.click()
    poco("com.philips.ph.homecare:id/schedule_remove_btn").click()
    poco("android:id/button1").click()

    # 返回设置详情页面
    poco("Navigate up").click()


if __name__ == "__main__":
    check_and_turn_on_device()
    configure_wake_up_schedule()
    verify_wake_up_display()
    modify_wake_up_schedule()
    verify_page_text()
    cleanup()