
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

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-2847
   下列20到74行对应 测试用例：https://nutriu.atlassian.net/browse/CH-2847
"""
# 打开 Air+ App
poco(text="Air+").click()
sleep(10)

#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)

#向上滑动屏幕
swipe(Template(r"tpl1732858788543.png", record_pos=(-0.038, 0.777), resolution=(1440, 3088)), vector=[0.0147, -0.5531])
sleep(2)

#点击Device settings 
poco("com.philips.ph.homecare:id/purifier_control_settings").click()
sleep(2)

#验证App 是否 定向到 settings 页面
assert_equal(str(poco(text="Settings").attr("enabled")), "True", "设备当前在settings 页面")
sleep(3)

# 设备beep sound 默认是开的状态，检查目前状态
assert_equal(str(poco(text="Beep sound").attr("checked")), "True", "beep sound 功能状态 为 开")
sleep(2)

#将 beep sound 功能设置为OFF 状态
poco("com.philips.ph.homecare:id/philipsSetting_volume_id").click()
sleep(2)

#验证当前beep sound 功能状态是否为OFF
assert_equal(str(poco(text="Beep sound").attr("checked")), "False", "beep sound 功能状态 为 off")
sleep(2)

#重新将beep sound 功能状态设置为ON
poco("com.philips.ph.homecare:id/philipsSetting_volume_id").click()
sleep(2)

# 设备beep sound 默认是开的状态，检查目前状态
assert_equal(str(poco(text="Beep sound").attr("checked")), "True", "beep sound 功能状态 为 开")
sleep(2)

# 设备beep sound 默认是开的状态，检查目前状态
assert_equal(str(poco(text="Beep sound").attr("checked")), "True", "beep sound 功能状态 为 开")
sleep(2)

#返回App到控制页面
poco("Navigate up").click()
sleep(1)

#向下滑动
swipe(Template(r"tpl1732861788387.png", record_pos=(0.001, -0.781), resolution=(1440, 3088)), vector=[-0.0601, 0.5733])
sleep(2)

#返回App 到App 主页
poco("Navigate up").click()
sleep(2)


