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

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-2930
   下列20到90行对应 测试用例：https://nutriu.atlassian.net/browse/CH-2930
"""
# 打开 Air+ App
poco(text="Air+").click()
sleep(10)

#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)
#向上滑动
swipe(Template(r"tpl1733380744877.png", record_pos=(0.047, 0.686), resolution=(1440, 3088)), vector=[-0.0498, -0.5295])
sleep(1)
#点击Devices settings
poco("com.philips.ph.homecare:id/purifier_control_settings").click()
sleep(1)

#验证是否进入Settings page
assert_equal(str(poco(text="Settings").attr("enabled")), "True", "当前页面在Settings 页面")
sleep(2)
#点击Help & support 按钮
poco("com.philips.ph.homecare:id/philipsSetting_support_id").click()
sleep(1)
#验证是否进入Help & support页面
assert_equal(str(poco(text="FAQ").attr("enabled")), "True", "当前页面在FAQ 页面")
sleep(2)
#点击Still can't solve the problem？
poco(text="Still can't solve the problem?").click()
sleep(2)
#检查是否成功进入Email diagnostis 页面
assert_equal(str(poco(text="Email diagnostics").attr("enabled")), "True", "当前页面在Email diagnostics 页面")
sleep(2)
#输入反馈的问题描述
text("123")
sleep(1)
#点击 send 按钮
poco("com.philips.ph.homecare:id/menu_text_id").click()
sleep(1)
#选择你所选的邮箱展示方式
poco("com.philips.ph.homecare:id/share_sheet_item_image_id").click()
sleep(1)
#检查诊断邮件标题是否显示
assert_exists(Template(r"tpl1733383306649.png", record_pos=(-0.222, -0.394), resolution=(1440, 3088)), "成功显示内容")
sleep(1)
#App回到主页面重新打开App
poco("com.android.systemui:id/home").click()
sleep(1)
swipe(Template(r"tpl1733383591807.png", record_pos=(0.125, -0.01), resolution=(1440, 3088)), vector=[-0.0274, -0.2344])
sleep(1)
poco(text="Air+").click()
sleep(1)
#点击Try sending again
poco("android:id/button2").click()
sleep(1)
#返回App to home page
poco("Navigate up").click()
sleep(1)
poco("Navigate up").click()
sleep(1)
swipe(Template(r"tpl1733383514880.png", record_pos=(0.038, -0.577), resolution=(1440, 3088)), vector=[0.0216, 0.4393])
sleep(1)
poco("Navigate up").click()
swipe(Template(r"tpl1733383531147.png", record_pos=(-0.019, -0.692), resolution=(1440, 3088)), vector=[0.0356, 0.5163])
sleep(1)
poco("Navigate up").click()
sleep(1)









