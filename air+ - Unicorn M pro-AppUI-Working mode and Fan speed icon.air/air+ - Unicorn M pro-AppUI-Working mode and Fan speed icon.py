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


"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-60
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
#点击工作模式选项
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
sleep(2)

#检查 Unicorn 工作模式和图标是否显示正确
assert_exists(Template(r"tpl1730360500996.png", record_pos=(0.042, 0.068), resolution=(1440, 3088)), "Auto 显示正确")
sleep(1)

# 检查 Sleep 工作模式和图标是否显示正确
assert_exists(Template(r"tpl1730360599094.png", record_pos=(0.011, 0.204), resolution=(1440, 3088)), "Sleep 显示正确")
sleep(1)

# 检查 Medium 工作模式和图标是否显示正确
assert_exists(Template(r"tpl1730360643450.png", record_pos=(0.034, 0.349), resolution=(1440, 3088)), "Medium 显示正确")
sleep(1)

# 检查 Turbo 工作模式和图标是否显示正确
assert_exists(Template(r"tpl1730360652208.png", record_pos=(0.038, 0.476), resolution=(1440, 3088)), "Turbo 显示正确")
sleep(1)

#点击cancel 按工作模式和图标是否显示正确
poco("com.philips.ph.homecare:id/dialog_control_sheet_cancel").click()
sleep(2)

#点击fan speed 控制列表
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
sleep(1)

#选择切换风速3
poco(text="3").click()
sleep(1)

# 确认切换
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)

#验证App 是否切换到了风速3
assert_exists(Template(r"tpl1730445336961.png", record_pos=(0.213, 0.451), resolution=(1440, 3088)), "设备风速为3")
sleep(1)

#检查manual 工作模式图标显示
assert_exists(Template(r"tpl1730445437450.png", record_pos=(0.02, 0.323), resolution=(1440, 3088)), "manual 工作模式图标显示正确")
sleep(2)


#返回App主页
poco("Navigate up").click()
sleep(2)

















