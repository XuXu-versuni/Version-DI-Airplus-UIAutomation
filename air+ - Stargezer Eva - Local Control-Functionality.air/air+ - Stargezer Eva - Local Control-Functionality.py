
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

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-271
   下列21到124行对应 测试用例：https://nutriu.atlassian.net/browse/CH-271
"""

# 打开 Air+ App
poco(text="Air+").click()
sleep(10)
#进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
sleep(3)
#打开工作模式切换按钮
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
sleep(1)
#选择Sleep mode ，确认设备切换到sleep mode
poco(text="Sleep").click()
sleep(1)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
assert_exists(Template(r"tpl1733453268791.png", record_pos=(0.015, 0.337), resolution=(1440, 3088)), "工作模式当前为sleep mode")
sleep(1)
#切换工作模式为Auto mode
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
sleep(1)
poco(text="Auto").click()
sleep(1)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
#检查当前模式是否为Auto Mode
assert_exists(Template(r"tpl1733470801808.png", record_pos=(0.01, 0.337), resolution=(1440, 3088)), "当前工作模式为Auto mode")
sleep(1)
#选择切换湿度按钮
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
sleep(1)
#湿度默认50%，现在切换湿度为55%
swipe(Template(r"tpl1733454770356.png", record_pos=(0.176, 0.392), resolution=(1440, 3088)), vector=[-0.0057, -0.0339])
sleep(1)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#验证当前湿度是否切换到55%
assert_exists(Template(r"tpl1733454838287.png", record_pos=(0.235, 0.469), resolution=(1440, 3088)), "当前湿度模式为55%")
sleep(1)
#打开环境灯光按钮，切换为off
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_off").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#检查环境灯光是否为off 状态
assert_exists(Template(r"tpl1733454962927.png", record_pos=(-0.198, 0.468), resolution=(1440, 3088)), "当前环境灯光状态为off")
sleep(2)
#选择切换灯光模式按钮切换为low 状态
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
sleep(2)
poco(text="Low").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#检查灯光是否为low 状态
assert_exists(Template(r"tpl1733455039003.png", record_pos=(-0.208, 0.595), resolution=(1440, 3088)), "当前灯光模式为Low ")
sleep(1)
#打开童锁
poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").click()
sleep()
#验证童锁功能是否打开
assert_equal(str(poco(text="Child Lock").attr("checked")), "True", "童锁成功打开")
sleep(2)
#设备关机
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
sleep(2)
#验证设备当前是否为关机状态
assert_equal(str(poco(text="Power").attr("checked")), "False", "当前状态为关机状态")
sleep(2)
#设备开机
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
sleep(2)
#验证设备当前是否为开机状态
assert_equal(str(poco(text="Power").attr("checked")), "True", "当前状态为开机状态")
sleep(2)
#切换灯光为Bright
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
sleep(2)
poco(text="Bright").click()
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#检查当前灯光状态是否为Bright
assert_exists(Template(r"tpl1733470365466.png", record_pos=(-0.203, 0.598), resolution=(1440, 3088)), "当前灯光状态为Bright")
sleep(2)
#关闭童锁功能
poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").click()
sleep(2)
#验证童锁功能是否关闭
assert_equal(str(poco(text="Child Lock").attr("checked")), "False", "童锁成功关闭")
sleep(2)
#切换湿度为50%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
sleep(2)
swipe(Template(r"tpl1733471898613.png", record_pos=(0.173, 0.244), resolution=(1440, 3088)), vector=[0.0003, 0.0351])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#验证当前湿度是否切换到55%
assert_exists(Template(r"tpl1733471937517.png", record_pos=(0.215, 0.072), resolution=(1440, 3088)), "当前湿度为50%")
sleep(1)
#返回App to home page
poco("Navigate up").click()
sleep(2)











