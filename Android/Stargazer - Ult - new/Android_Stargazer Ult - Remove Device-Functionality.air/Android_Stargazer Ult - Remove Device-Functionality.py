# -*- encoding=utf8 -*-
__author__ = "xjin"
from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
poco = AndroidUiautomationPoco()
auto_setup(__file__)

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-309
   下列20到50行对应 测试用例：https://nutriu.atlassian.net/browse/CH-309
"""

"""
"""

# 打开 Air+ App
start_app("com.philips.ph.homecare")
sleep(10)

#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(2)

#点击右上角的设置按钮，进入设备设置页面
poco("com.philips.ph.homecare:id/menu_setting_id").click()
sleep(2)

#验证App是否进入Settings 页面
assert_equal(str(poco(text="Settings").attr("enabled")), "True", "当前页面在设备设置页面")
sleep(2)

#向上滑动屏幕
swipe(Template(r"tpl1736407074806.png", record_pos=(-0.056, 0.676), resolution=(1440, 3088)), vector=[-0.036, -0.3824])
sleep(1)

#点击Remove the Device 按钮
poco("com.philips.ph.homecare:id/philipsSetting_remove_id").click()
sleep(1)

#点击Yes
poco("android:id/button1").click()
sleep(2)

#验证设备是否成功移除
assert_exists(Template(r"tpl1736407466036.png", record_pos=(-0.005, -0.047), resolution=(1440, 3088)), "App主页没有设备，设备已经删除成功")
sleep(2)

#本脚本执行之后，必须要再添加设备到设备列表才能进行本shell。
#这也就是原来说的数据还愿。


