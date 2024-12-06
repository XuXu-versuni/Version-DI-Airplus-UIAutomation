
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

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-140
   下列21到49行对应 测试用例：https://nutriu.atlassian.net/browse/CH-140
"""

# 打开 Air+ App
poco(text="Air+").click()
sleep(10)
#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)
#向上滑动
swipe(Template(r"tpl1733388667601.png", record_pos=(0.018, 0.412), resolution=(1440, 3088)), vector=[-0.0289, -0.3608])
sleep(2)
#进入Device Health 页面
poco("com.philips.ph.homecare:id/purifier_control_health").click()
sleep(1)
#验证是否进入 device health 页面
assert_equal(str(poco(text="Device Health").attr("enabled")), "True", "App成功Device health 页面")
sleep(3)
#验证App 是否显示清洁滤网寿命
assert_equal(str(poco("com.philips.ph.homecare:id/filter_item_clean_bar_id").attr("enabled")),"True", "成功显示滤网寿命")
sleep(2)

#验证App 是否显示滤网寿命
assert_equal(str(poco("com.philips.ph.homecare:id/filter_item_clean_bar_id").attr("enabled")),"True", "成功显示滤网寿命")
sleep(2)
# 返回App 到主页
poco("Navigate up").click()
sleep(1)
swipe(Template(r"tpl1733389501590.png", record_pos=(0.004, -0.564), resolution=(1440, 3088)), vector=[-0.0377, 0.3614])
sleep(1)
poco("Navigate up").click()
sleep(2)

