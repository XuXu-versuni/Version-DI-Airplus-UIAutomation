# -*- encoding=utf8 -*-
__author__ = "xuxu"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

import time

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/09181FDD4000E1?ori_method=ADBORI&touch_method=MAXTOUCH&",])


# script content
print("start...")

import time
import uiautomator2 as u2


def main():
    # 连接安卓设备，这里假设设备已通过USB连接并且开启了USB调试模式
    device = u2.connect()

    # 启动Air+ app
    device.app_start("com.philips.ph.homecare")
    time.sleep(5)  # 适当等待应用启动完成，可根据实际情况调整等待时间

    # 验证app是否成功打开
    dashboard_title_text = device(resourceId="com.philips.ph.homecare:id/dashboard_section_title").get_text()
    if dashboard_title_text == "My Devices":
        print("app打开成功")
    else:
        print("app打开失败")

    # 进入设备控制页面相关操作（对应原脚本部分功能逻辑）
    device(description="https://air-matters.com/app/philips/dark_mode/AC3420_10.png").click()
    time.sleep(5)
    purifier_control_title_text = device(resourceId="com.philips.ph.homecare:id/purifier_control_readings_title").get_text()
    if purifier_control_title_text == "Air Quality":
        print("进入设备控制页面成功")
    else:
        print("进入设备控制页面失败")

    # 检查Al Enable卡片显示相关验证
    control_new_feature_btn_text = device(resourceId="com.philips.ph.homecare:id/control_new_feature_btn").get_text()
    if control_new_feature_btn_text == "Enable now":
        print("Al Enable卡片显示正常")
    else:
        print("Al Enable卡片显示异常")

    # 检查Al卡片文案显示验证
    control_new_feature_msg_text = device(resourceId="com.philips.ph.homecare:id/control_new_feature_msg").get_text()
    if control_new_feature_msg_text == "Enable Auto+ mode for the best performance at the lowest energy.":
        print("Al卡片文案展示正常")
    else:
        print("Al卡片文案展示异常")

    # 关闭Al卡片操作及后续验证
    device(resourceId="com.philips.ph.homecare:id/control_new_feature_close").click()
    time.sleep(3)
    control_new_feature_btn_text_after_close = device(resourceId="com.philips.ph.homecare:id/control_new_feature_btn").get_text()
    if control_new_feature_btn_text_after_close == "Learn more":
        print("smart scenario卡片显示正常")
    else:
        print("smart scenario卡片显示异常")

    # 检查smart scenario卡片文案显示（这里简单示例验证元素是否存在，可根据实际更细致判断文案内容等）
    if device.exists(resourceId="com.philips.ph.homecare:id/schedule_scenario_item_title", text="Fresh wake-up"):
        print("smart scenario卡片文案显示正常")
    else:
        print("smart scenario卡片文案显示异常")

    # 点击Learn more按钮进入schedule页面及验证
    device(resourceId="com.philips.ph.homecare:id/control_new_feature_btn").click()
    time.sleep(6)
    scheduler_text = device(resourceId="android.widget.TextView").get_text()
    if scheduler_text == "Scheduler":
        print("Schedule页面进入成功")
    else:
        print("Schedule页面进入失败")

    # 返回上一级页面
    device.press("back")
    time.sleep(3)

    # 关闭smart scenario卡片及验证
    device(resourceId="com.philips.ph.homecare:id/control_new_feature_close").click()
    time.sleep(3)
    if not device.exists(resourceId="com.philips.ph.homecare:id/schedule_scenario_item_title", text="Fresh wake-up"):
        print("关闭smart scenario卡片成功")
    else:
        print("关闭smart scenario卡片失败")

    # 以下是后续原脚本中其他部分逻辑对应的代码转换（大致类似的处理方式）

    # 模拟滑动操作（对应原脚本中的滑动功能）
    time.sleep(3)
    device.swipe([874, 1257], [874, 29])
    time.sleep(3)

    # 进入schedule页面，检查smart schedule卡片显示相关验证
    device(resourceId="com.philips.ph.homecare:id/purifier_control_schedule").click()
    time.sleep(5)
    scheduler_text_again = device(resourceId="android.widget.TextView").get_text()
    if scheduler_text_again == "Scheduler":
        print("Schedule页面再次进入成功")
    else:
        print("Schedule页面再次进入失败")

    fresh_wakeup_title_text = device(resourceId="com.philips.ph.homecare:id/schedule_scenario_item_title").get_text()
    if fresh_wakeup_title_text == "Fresh wake-up":
        print("Fresh wake-up卡片展示正常")
    else:
        print("Fresh wake-up卡片展示异常")

    if device.exists(resourceId="com.philips.ph.homecare:id/schedule_scenario_item_title", text="Fresh bedtime"):
        print("Fresh bedtime卡片展示正常")
    else:
        print("Fresh bedtime卡片展示异常")

    # 检查Fresh wake-up任务默认显示相关验证
    device(text="Fresh wake-up").click()
    time.sleep(3)

    smart_scenario_edit_title_text = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_title").get_text()
    if smart_scenario_edit_title_text == "Fresh wake-up":
        print("Fresh wake-up任务卡片展示正常，且文案显示正常")
    else:
        print("Fresh wake-up任务卡片展示或文案显示异常")

    smart_scenario_edit_subtitle_text = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_subtitle").get_text()
    if smart_scenario_edit_subtitle_text == "Wake up to a fresh & clean bedroom":
        print("Fresh wake-up任务卡片副标题文案显示正常")
    else:
        print("Fresh wake-up任务卡片副标题文案显示异常")

    smart_scenario_edit_desc_text = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_desc").get_text()
    if smart_scenario_edit_desc_text == "30min before your set wake-up time, the purifier will slowly start ramping up power, to give you a fresh morning.":
        print("Fresh wake-up任务卡片描述文案显示正常")
    else:
        print("Fresh wake-up任务卡片描述文案显示异常")

    time.sleep(6)

    smart_scenario_edit_time_text = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_time").get_text()
    if smart_scenario_edit_time_text == "08:00":
        print("Fresh wake-up默认结束时间显示正常")
    else:
        print("Fresh wake-up默认结束时间显示异常")

    smart_scenario_edit_time_desc_text = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_time_desc").get_text()
    if smart_scenario_edit_time_desc_text == "Starts at 07:30":
        print("Fresh wake-up默认开始时间显示正常")
    else:
        print("Fresh wake-up默认开始时间显示异常")

    smart_scenario_edit_light_checked = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_light").info.get('checked', False)
    if smart_scenario_edit_light_checked:
        print("Fresh wake-up默认灯光是打开状态")
    else:
        print("Fresh wake-up默认灯光不是打开状态")

    smart_scenario_edit_light_desc_text = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_light_desc").get_text()
    if smart_scenario_edit_light_desc_text == "Light turns on gradually, to mimic sunrise":
        print("Fresh wake-up灯光文案显示正确")
    else:
        print("Fresh wake-up灯光文案显示错误")

    smart_scenario_edit_repeat_section_text = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_repeat_section").get_text()
    if smart_scenario_edit_repeat_section_text == "Repeat every...":
        print("Fresh wake-up每天重复运行时间文案显示正确")
    else:
        print("Fresh wake-up每天重复运行时间文案显示错误")

    # 验证每天循环运行时间默认全选状态（针对各个星期的按钮进行判断）
    schedule_monday_btn_checked = device(resourceId="com.philips.ph.homecare:id/schedule_monday_btn").info.get('checked', False)
    if schedule_monday_btn_checked:
        print("Fresh wake-up中星期一重复时间默认选中")
    else:
        print("Fresh wake-up中星期一重复时间未默认选中")

    schedule_tuesday_btn_checked = device(resourceId="com.philips.ph.homecare:id/schedule_tuesday_btn").info.get('checked', False)
    if schedule_tuesday_btn_checked:
        print("Fresh wake-up中星期二重复时间默认选中")
    else:
        print("Fresh wake-up中星期二重复时间未默认选中")

    schedule_wednesday_btn_checked = device(resourceId="com.philips.ph.homecare:id/schedule_wednesday_btn").info.get('checked', False)
    if schedule_wednesday_btn_checked:
        print("Fresh wake-up中星期三重复时间默认选中")
    else:
        print("Fresh wake-up中星期三重复时间未默认选中")

    schedule_thursday_btn_checked = device(resourceId="com.philips.ph.homecare:id/schedule_thursday_btn").info.get('checked', False)
    if schedule_thursday_btn_checked:
        print("Fresh wake-up中星期四重复时间默认选中")
    else:
        print("Fresh wake-up中星期四重复时间未默认选中")

    schedule_friday_btn_checked = device(resourceId="com.philips.ph.homecare:id/schedule_friday_btn").info.get('checked', False)
    if schedule_friday_btn_checked:
        print("Fresh wake-up中星期五重复时间默认选中")
    else:
        print("Fresh wake-up中星期五重复时间未默认选中")

    schedule_saturday_btn_checked = device(resourceId="com.philips.ph.homecare:id/schedule_saturday_btn").info.get('checked', False)
    if schedule_saturday_btn_checked:
        print("Fresh wake-up中星期六重复时间默认选中")
    else:
        print("Fresh wake-up中星期六重复时间未默认选中")

    schedule_sunday_btn_checked = device(resourceId="com.philips.ph.homecare:id/schedule_sunday_btn").info.get('checked', False)
    if schedule_sunday_btn_checked:
        print("Fresh wake-up中星期日重复时间默认选中")
    else:
        print("Fresh wake-up中星期日重复时间未默认选中")

    smart_scenario_edit_done_text = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_done").get_text()
    if smart_scenario_edit_done_text == "Done":
        print("Fresh wake-up的Done按钮显示正常")
    else:
        print("Fresh wake-up的Done按钮显示异常")

    # 以下继续后续原脚本功能逻辑对应的代码转换

    # 设置一条Fresh wake-up任务及相关验证
    device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_done").click()
    time.sleep(3)

    schedule_scenario_item_status_text = device(resourceId="com.philips.ph.homecare:id/schedule_scenario_item_status").get_text()
    if schedule_scenario_item_status_text == "ON":
        print("Fresh wake-up打开状态显示正确")
    else:
        print("Fresh wake-up打开状态显示错误")

    schedule_scenario_item_subtitle_text = device(resourceId="com.philips.ph.homecare:id/schedule_scenario_item_subtitle").get_text()
    if schedule_scenario_item_subtitle_text == "07:30 - 08:00":
        print("Fresh wake-up设置成功后的时间显示正确")
    else:
        print("Fresh wake-up设置成功后的时间显示错误")

    # 再次进入Fresh wake-up页面，验证disable schedule相关操作及显示
    device(text="Fresh wake-up").click()
    time.sleep(6)

    smart_scenario_edit_disable_text = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_disable").get_text()
    if smart_scenario_edit_disable_text == "Disable scheduler":
        print("Fresh wake-up中disable schedule按钮显示正常")
    else:
        print("Fresh wake-up中disable schedule按钮显示异常")

    device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_disable").click()
    time.sleep(3)

    schedule_scenario_item_status_text_after_disable = device(resourceId="com.philips.ph.homecare:id/schedule_scenario_item_status").get_text()
    if schedule_scenario_item_status_text_after_disable == "OFF":
        print("Fresh wake-up恢复默认状态（禁用任务成功）")
    else:
        print("Fresh wake-up恢复默认状态（禁用任务失败）")

    # 检查Fresh bedtime任务默认显示相关操作及验证
    time.sleep(3)
    device(text="Fresh bedtime").click()
    time.sleep(3)

    smart_scenario_edit_title_text_for_bedtime = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_title").get_text()
    if smart_scenario_edit_title_text_for_bedtime == "Fresh bedtime":
        print("Fresh bedtime任务卡片展示正常，且文案显示正常")
    else:
        print("Fresh bedtime任务卡片展示或文案显示异常")

    smart_scenario_edit_subtitle_text_for_bedtime = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_subtitle").get_text()
    if smart_scenario_edit_subtitle_text_for_bedtime == "Fall asleep in a fresh & clean bedroom":
        print("Fresh bedtime任务卡片副标题文案显示正常")
    else:
        print("Fresh bedtime任务卡片副标题文案显示异常")

    smart_scenario_edit_desc_text_for_bedtime = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_desc").get_text()
    if smart_scenario_edit_desc_text_for_bedtime == "1hr before your set bedtime, the device goes into Turbo mode for 15min. The next 45min it switches to quiet Sleep mode.":
        print("Fresh bedtime任务卡片描述文案显示正常")
    else:
        print("Fresh bedtime任务卡片描述文案显示异常")

    time.sleep(3)

    smart_scenario_edit_time_text_for_bedtime = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_time").get_text()
    if smart_scenario_edit_time_text_for_bedtime == "11:00":
        print("Fresh bedtime默认结束时间显示正常")
    else:
        print("Fresh bedtime默认结束时间显示异常")

    smart_scenario_edit_time_desc_text_for_bedtime = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_time_desc").get_text()
    if smart_scenario_edit_time_desc_text_for_bedtime == "Starts at 10:00":
        print("Fresh bedtime默认开始时间显示正常")
    else:
        print("Fresh bedtime默认开始时间显示异常")

    smart_scenario_edit_light_checked_for_bedtime = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_light").info.get('checked', False)
    if smart_scenario_edit_light_checked_for_bedtime:
        print("Fresh bedtime默认灯光是打开状态")
    else:
        print("Fresh bedtime默认灯光不是打开状态")

    smart_scenario_edit_light_desc_text_for_bedtime = device(resourceId="com.philips.ph.homecare:id/smart_scenario_edit_light_desc").get_text()
    if smart_scenario_edit_light_desc_text_for_bedtime == "Dim light that switches off at your set bedtime":
        print("Fresh bedtime灯光文案显示正确")
    else:
        print("Fresh bedtime灯光文案显示错误")

    # 验证Fresh bedtime每天循环运行时间默认全选状态（类似Fresh wake-up的验证方式）
    schedule_monday_btn_checked_for_bedtime = device(resourceId="com.philips.ph.homecare:id/schedule_monday_btn").info.get('checked', False)
    if schedule_monday_btn_checked_for_bedtime:
        print("Fresh bedtime中星期一重复时间默认选中")
    else:
        print("Fresh bedtime中星期一重复时间未默认选中")

    schedule_tuesday_btn_checked_for_bedtime = device(resourceId="com.philips.ph.homecare:id/schedule_tuesday_btn").info.get('checked', False)
    if schedule_tuesday_btn_checked_for_bedtime:
        print("Fresh bedtime中星期二重复时间默认选中")
    else:
        print("Fresh bedtime中星期二重复时间未默认选中")

    schedule_wednesday_btn_checked_for_bedtime = device(resourceId="com.philips.ph.homecare:id/schedule_wednesday_btn").info.get('checked', False)
    if schedule_wednesday_btn_checked_for_bedtime:
        print("Fresh bedtime中星期三重复时间默认选中")
    else:
        print("Fresh bedtime中星期三重复时间未默认选中")

    schedule_thursday_btn_checked_for_bedtime = device(resourceId="com.philips.ph.homecare:id/schedule_thursday_btn").info.get('checked', False)
    if schedule_thursday_btn_checked_for_bedtime:
        print("Fresh bedtime中星期四重复时间默认选中")
    else:
        print("Fresh bedtime中星期四重复时间未默认选中