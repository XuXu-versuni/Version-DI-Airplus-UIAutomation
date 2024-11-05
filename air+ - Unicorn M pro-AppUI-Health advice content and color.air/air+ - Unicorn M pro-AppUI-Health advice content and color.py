# -*- encoding=utf8 -*-
__author__ = "xjinp"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
poco = AndroidUiautomationPoco()
auto_setup(__file__)


"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-54
例子：下列XXX到YYY行对应 测试用例：https://nutriu.atlassian.net/browse/CH-50
"""
# 打开 Air+ App
poco(text="Air+").click()
sleep(10)

#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)

#向上滑动
swipe(Template(r"tpl1730359614605.png", record_pos=(-0.136, 0.542), resolution=(1440, 3088)), vector=[0.0395, -0.4907])
sleep(2)

#点击进入Device Health 页面
poco("com.philips.ph.homecare:id/purifier_control_health").click()
sleep(1)

#检查页面显示和文字显示
assert_exists(Template(r"tpl1730364620138.png", record_pos=(-0.008, -0.434), resolution=(1440, 3088)), "图片文字显示正确")

#向下滑动
swipe(Template(r"tpl1730365360081.png", record_pos=(0.057, 0.734), resolution=(1440, 3088)), vector=[-0.1384, -0.7235])
sleep(2)

#检查sensor 文字解释
assert_exists(Template(r"tpl1730365402463.png", record_pos=(0.0, 0.518), resolution=(1440, 3088)), "文字显示正确")
sleep(2)

#点击 how to clean the filter
poco(text="How to clean the filter").click()
sleep(2)

# 检查 如何清洁过滤器 页面显示
assert_exists(Template(r"tpl1730365560557.png", record_pos=(0.003, -0.407), resolution=(1440, 3088)), "文字步骤显示正确")
sleep(2)

# 返回 App device Health 页面
poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
sleep(1)

#点击 how to replace the filter
poco(text="How to replace the filter").click()
sleep(1)

# 检查 如何清洁过滤器 页面显示
assert_exists(Template(r"tpl1730365671239.png", record_pos=(0.01, -0.258), resolution=(1440, 3088)), "文字步骤显示正确")
sleep(1)

# 返回 App device Health 页面
poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
sleep(1)

#返回App- 设备控制页面
poco("Navigate up").click()
sleep(1)

#向上滑动页面
swipe(Template(r"tpl1730365772053.png", record_pos=(-0.028, -0.832), resolution=(1440, 3088)), vector=[-0.0436, 0.6663])
sleep(1)

#返回app主页面
poco("Navigate up").click()
sleep(2)







