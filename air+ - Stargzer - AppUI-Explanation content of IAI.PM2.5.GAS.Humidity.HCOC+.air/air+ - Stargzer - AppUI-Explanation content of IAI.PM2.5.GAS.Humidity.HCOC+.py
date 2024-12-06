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

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-56
   下列20到41行对应 测试用例：https://nutriu.atlassian.net/browse/CH-56
"""
# 打开 Air+ App
poco(text="Air+").click()
sleep(10)

#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)

# Stargzer 仅支持温度和湿度显示
#1 检查目标温度显示按钮是否存在
assert_equal(str(poco(text="Humidity").attr("enabled")), "True", "App显示目标湿度功能")
sleep(3)

#2 检查目标湿度按钮是否存在
assert_equal(str(poco(text="Temperature").attr("enabled")), "True", "App显示目标温度功能")
sleep(3)
# 返回App 主页
poco("Navigate up").click()
sleep(2)