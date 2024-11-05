# -*- encoding=utf8 -*-
__author__ = "xjinp"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
poco = AndroidUiautomationPoco()
auto_setup(__file__)


"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-50
例子：下列XXX到YYY行对应 测试用例：https://nutriu.atlassian.net/browse/CH-50
"""


# 打开 Air+ App
poco(text="Air+").click()
sleep(10)

#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)

#打开 Air quality explained 页面
poco("com.philips.ph.homecare:id/purifier_control_readings_title").click()
sleep(3)

#验证App 是否进入Air quality explained 页面
assert_exists(Template(r"tpl1730358593029.png", record_pos=(0.003, -0.378), resolution=(1440, 3088)), "成功进入 Air quality explained 页面")
sleep(3)
# 向上滑动
swipe(Template(r"tpl1730358672277.png", record_pos=(0.017, 0.557), resolution=(1440, 3088)), vector=[-0.0729, -0.3752])
sleep(3)

#验证PM2.5level 显示是否正确
assert_exists(Template(r"tpl1730358758317.png", record_pos=(0.011, 0.562), resolution=(1440, 3088)), "App显示正确，返回值正确")
sleep(3)

# 返回到App主页
poco("com.philips.ph.homecare:id/web_back_btn_id").click()
sleep(3)

#检查App 主页是否存在显示 PM2.5,Gas,IAI
assert_exists(Template(r"tpl1730358972998.png", record_pos=(-0.01, 0.212), resolution=(1440, 3088)), "成功显示")
sleep(3)
#返回app主页
poco("Navigate up").click()
sleep(1)




