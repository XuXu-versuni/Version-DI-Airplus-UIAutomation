
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

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-146
   下列21到49行对应 测试用例：https://nutriu.atlassian.net/browse/CH-146
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
#点击进入 How to clean the humidification filter 功能按钮
poco(text="How to clean the humidification filter").click()
sleep(3)
#验证清洁滤网步骤是否显示正确
assert_exists(Template(r"tpl1733391426141.png", record_pos=(0.011, -0.253), resolution=(1440, 3088)), "清洁步骤显示正确")
sleep(2)
#返回 device health 页面
poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
sleep(2)
#点击进入 How to replace the humidification filter 功能按钮
poco(text="How to replace the humidification filter").click()
sleep(3)
#验证滤网更换步骤是否显示正确
assert_exists(Template(r"tpl1733391536311.png", record_pos=(0.008, -0.324), resolution=(1440, 3088)), "滤网更换步骤显示正确")
sleep(1)
#返回 device health 页面
poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
sleep(2)
#返回App 到控制页面
poco("Navigate up").click()
sleep(1)
#向下滑动屏幕
swipe(Template(r"tpl1733391664868.png", record_pos=(0.019, -0.665), resolution=(1440, 3088)), vector=[-0.0447, 0.4075])
sleep(1)
#返回App 到 home page
poco("Navigate up").click()
sleep(2)










