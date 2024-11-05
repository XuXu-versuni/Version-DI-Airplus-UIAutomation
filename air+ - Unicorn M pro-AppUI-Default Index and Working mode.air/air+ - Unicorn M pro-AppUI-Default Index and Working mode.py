# -*- encoding=utf8 -*-
__author__ = "xjinp"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
poco = AndroidUiautomationPoco()
auto_setup(__file__)


"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-53
例子：下列XXX到YYY行对应 测试用例：https://nutriu.atlassian.net/browse/CH-53
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

#检查 Unicorn 工作模式显示 工作模式为: Auto,Sleep,Medium,Turbo

# 检查Auto模式是否在工作模式中
assert_exists(Template(r"tpl1730360500996.png", record_pos=(0.042, 0.068), resolution=(1440, 3088)), "Auto 显示正确")
sleep(1)

# 检查 Sleep 模式是否在工作模式中
assert_exists(Template(r"tpl1730360599094.png", record_pos=(0.011, 0.204), resolution=(1440, 3088)), "Sleep 显示正确")
sleep(1)

# 检查 Medium 模式是否在工作模式中
assert_exists(Template(r"tpl1730360643450.png", record_pos=(0.034, 0.349), resolution=(1440, 3088)), "Medium 显示正确")
sleep(1)

# 检查 Turbo 模式是否在工作模式中
assert_exists(Template(r"tpl1730360652208.png", record_pos=(0.038, 0.476), resolution=(1440, 3088)), "Turbo 显示正确")
sleep(1)

#点击cancel 按钮返回到设备控制页面
poco("com.philips.ph.homecare:id/dialog_control_sheet_cancel").click()
sleep(2)

#接下来 Unicorn M pro 正常AI Auto+ mode，下一步打开Auto+ mode，验证设备工作模式是否显示Auto+ mode
# 进入 device settings page
poco("com.philips.ph.homecare:id/purifier_control_settings").click()
sleep(1)

#点击 Auto+ mode(Beta)
poco("com.philips.ph.homecare:id/philipsSetting_autoplus_id").click()
sleep(1)

#打开 Auto+ mode
poco("com.philips.ph.homecare:id/autoplus_switch_id").click()
sleep(1)

#验证是否打开成功
assert_exists(Template(r"tpl1730362114530.png", record_pos=(0.019, -0.773), resolution=(1440, 3088)), "成功打开Auto+ mode")
sleep(5)

#返回到App device settings 页面
poco("Navigate up").click()
sleep(1)

#返回到App设备控制页面
poco("Navigate up").click()
sleep(1)

#点击工作模式选项
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
sleep(2)

# 检查 Auto+ 模式是否在工作模式中
assert_exists(Template(r"tpl1730362632615.png", record_pos=(-0.012, 0.068), resolution=(1440, 3088)), "Auto+ 显示正确")
sleep(1)

#点击cancel 按钮返回到设备控制页面
poco("com.philips.ph.homecare:id/dialog_control_sheet_cancel").click()
sleep(2)

#向下滑动
swipe(Template(r"tpl1730362780662.png", record_pos=(-0.097, -0.831), resolution=(1440, 3088)), vector=[0.099, 0.6598])
sleep(2)

#返回App主页
poco("Navigate up").click()
sleep(2)

















