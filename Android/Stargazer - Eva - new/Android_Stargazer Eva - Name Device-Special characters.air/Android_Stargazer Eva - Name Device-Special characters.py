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

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-274
   下列20到57行对应 测试用例：https://nutriu.atlassian.net/browse/CH-274
"""

# 打开 Air+ App
start_app("com.philips.ph.homecare")
sleep(10)

#点击设备进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(2)

#点击设置按钮进入设备设置页面
poco("com.philips.ph.homecare:id/menu_setting_id").click()
sleep(2)

#验证是否进入设备设置页面
assert_equal(str(poco(text="Settings").attr("enabled")), "True", "当前页面在设备设置页面")
sleep(2)

#点击设置 Device name
poco("com.philips.ph.homecare:id/philipsSetting_name_id").click()
sleep(1)

#点击设备名称输入框，设置新的设备名称
poco("com.philips.ph.homecare:id/dialog_name_edit").click()
sleep(1)
text("!@#$^&*")
#点击确认Apply 设置。
poco("com.philips.ph.homecare:id/dialog_name_apply").click()
sleep(8)

#回到App控制页面
poco("Navigate up").click()
sleep(2)
#检查设备名称是否显示正确
assert_exists(Template(r"tpl1736229500770.png", record_pos=(0.0, -0.924), resolution=(1440, 3088)), "显示正确")


#回到App主页面
poco("Navigate up").click()
sleep(2)
