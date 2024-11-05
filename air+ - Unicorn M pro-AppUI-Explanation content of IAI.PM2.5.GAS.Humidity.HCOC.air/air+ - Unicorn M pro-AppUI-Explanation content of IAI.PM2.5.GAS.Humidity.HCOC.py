# -*- encoding=utf8 -*-
__author__ = "xjinp"

from airtest.core.api import *

auto_setup(__file__)
# -*- encoding=utf8 -*-
__author__ = "xjinp"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
poco = AndroidUiautomationPoco()
auto_setup(__file__)


"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-56
例子：下列XXX到YYY行对应 测试用例：https://nutriu.atlassian.net/browse/CH-56
"""


# 打开 Air+ App
poco(text="Air+").click()
sleep(10)

#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)

#点击 打开Air quality explained 选项
poco("com.philips.ph.homecare:id/purifier_control_readings_title").click()
sleep(2)

#检查PM2.5 解释内容
poco(text="PM2.5 are fine, inhalable particles with a diameter of 2.5 micrometers or smaller. In comparison: a human hair is about 70 micrometers in diameter. PM2.5 is a common air pollutant and due to its size, can be inhaled and impact your health. Outdoor, it’s emitted from vehicles, industries, fires and construction sites while stoves, fireplaces, pet dander and mould can be a source of PM2.5 indoors. Thanks to your device’s multi-layer filtration system, 99.97% of these particles are captured from the air.").click()
assert_exists(Template(r"tpl1730367224329.png", record_pos=(-0.005, 0.162), resolution=(1440, 3088)), "显示正确")
sleep(2)

#点击Gas 按钮
poco("reading_gas").click()
sleep(1)

#检查Gas 解释内容
assert_exists(Template(r"tpl1730368263091.png", record_pos=(0.018, 0.133), resolution=(1440, 3088)), "显示正确")
sleep(1)

#点击IAI 按钮
poco("reading_iai").click()
sleep(1)

#检查IAI 解释内容
assert_exists(Template(r"tpl1730368758033.png", record_pos=(0.014, 0.304), resolution=(1440, 3088)), "显示正确")
sleep(1)

#点击Humidity 按钮
poco("reading_humidity").click()
sleep(1)

#检查Humidity 解释内容
assert_exists(Template(r"tpl1730369223458.png", record_pos=(-0.006, 0.187), resolution=(1440, 3088)), "显示正确")
sleep(2)

#点击Back 回到设备控制页面
poco("com.philips.ph.homecare:id/web_back_btn_id").click()
sleep(1)

#返回App 主页面
poco("Navigate up").click()
sleep(2)






