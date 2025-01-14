# -*- encoding=utf8 -*-
__author__ = "xjinp"

from airtest.core.api import *

auto_setup(__file__)


from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
poco = AndroidUiautomationPoco()
auto_setup(__file__)

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-1594
   下列20到80行对应 测试用例：https://nutriu.atlassian.net/browse/CH-1594
"""
# 打开 Air+ App
poco(text="Air+").click()
sleep(10)

#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)

#检查timer 状态，App 应该显示 timer 状态为 Off
assert_exists(Template(r"tpl1732867779867.png", record_pos=(0.213, 0.603), resolution=(1440, 3088)), "App timer 状态 为 off")
sleep(2)



#设置 timer 为 4 小时
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
sleep(1)

swipe(Template(r"tpl1733109234380.png", record_pos=(0.215, 0.438), resolution=(1440, 3088)), vector=[-0.0042, -0.0573])

#点击 确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(5)

#检查timer时间是否为2 hour
assert_exists(Template(r"tpl1733109397939.png", record_pos=(0.218, 0.598), resolution=(1440, 3088)), "当前timer时间为 2h")
sleep(2)

#进入设置timer页面
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
sleep(1)
swipe(Template(r"tpl1733279430653.png", record_pos=(0.223, 0.434), resolution=(1440, 3088)), vector=[-0.0068, -0.051])

#点击 确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(5)

#检查timer时间是否为4小时
assert_exists(Template(r"tpl1733279496225.png", record_pos=(0.226, 0.528), resolution=(1440, 3088)), "当前timer时间为 4h")


#设置 timer 为off
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
sleep(1)
swipe(Template(r"tpl1733280756882.png", record_pos=(0.235, 0.221), resolution=(1440, 3088)), vector=[-0.0161, 0.0496])
sleep(2)
swipe(Template(r"tpl1733280823100.png", record_pos=(0.201, 0.224), resolution=(1440, 3088)), vector=[-0.0073, 0.0436])

sleep(2)

#点击 确认
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(5)


#检查timer 状态，App 应该显示 timer 状态为 Off
assert_exists(Template(r"tpl1732867779867.png", record_pos=(0.213, 0.603), resolution=(1440, 3088)), "App timer 状态 为 off")
sleep(2)

#返回App 到App 主页
poco("Navigate up").click()
sleep(2)