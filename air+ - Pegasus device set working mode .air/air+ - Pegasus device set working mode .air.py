# -*- encoding=utf8 -*-
__author__ = "Wmeng1"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
# poco脚本初始化
poco = AndroidUiautomationPoco(use_airtest_input = True,screenshot_each_action = False)
auto_setup(__file__)

"""本shell 对应 测试用例：https://nutriu.atlassian.net/browse/CH-50
例子：下列XXX到YYY行对应 测试用例：https://nutriu.atlassian.net/browse/CH-50
"""

#Oneplus10
#Pegasus 3in1 device（CH-1547-CH-1559;CH-1581)
# CH-1547
# 检查设备控制功能的默认显示（前置条件：厂测后跑这条case）
# Template(r"tpl1730171470198.png", record_pos=(0.001, 0.449), resolution=(1080, 2412))（默认显示：开关：Power on；模式：Auto，风速：Auto；功能：Fan；温度：灰置；Timer：关闭；旋转：off；灯光：100%）

#进入设备控制页面
poco(desc="https://air-matters.com/app/philips/dark_mode/AMF870_15.png").click()
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(),"Air Quality","进入设备控制页面成功")
swipe(Template(r"tpl1730166215530.png", record_pos=(0.035, 0.281), resolution=(1080, 2412)), vector=[0.0, -0.3377])
# 功能为Circulation，检查默认的模式按钮和风速按钮（厂测后的默认显示：模式：Auto；风速：Auto）
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1730179970117.png", record_pos=(-0.206, 0.477), resolution=(1080, 2412)),"功能为Circulation，切换成功")
# 模式设置为默认状态（模式：Auto；风速：Auto） CH-1550
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Auto").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# 阈值要根据手机适配设置
assert_exists(Template(r"tpl1730180188375.png", threshold=0.98, record_pos=(-0.003, 0.075), resolution=(1080, 2412)),"默认显示：模式：Auto；风速：Auto")

# CH-1548
# Circulation下，设置风速为1
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# 阈值要根据手机适配设置
assert_exists(Template(r"tpl1729481262797.png", threshold = 0.98, record_pos=(0.215, 0.676), resolution=(1080, 2412)),"设置风速为1成功")

#  CH-1549
# Circulation下，设置功能为Heating
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
swipe([621,1564],[-621,-1564])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1730186730163.png", record_pos=(-0.195, 0.105), resolution=(1080, 2412)),"Heating功能设置成功")

# CH-1550 and CH-1551
# 功能为Circulation，设置模式为Auto mode，然后设置Oscillation为350°
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1730179970117.png", record_pos=(-0.206, 0.477), resolution=(1080, 2412)),"功能为Circulation，切换成功")
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Auto").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# 阈值要根据手机适配设置
assert_exists(Template(r"tpl1730180188375.png", threshold=0.98, record_pos=(-0.003, 0.075), resolution=(1080, 2412)),"模式设置为Auto成功")

poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([0.841, -0.0052])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# 阈值要根据手机适配设置
assert_exists(Template(r"tpl1728975091959.png", threshold = 0.98, record_pos=(0.008, 0.985), resolution=(1080, 2412)),"设置Oscillation=350°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

# CH-1552 and CH-1553
# 功能为Circulation，设置模式为Sleep mode，然后设置Oscillation为350°
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1730179970117.png", record_pos=(-0.206, 0.477), resolution=(1080, 2412)),"功能为Circulation，切换成功")
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Sleep").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1730188488287.png", record_pos=(-0.193, -0.003), resolution=(1080, 2412)),"模式设置为Sleep mode成功")

poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([0.841, -0.0052])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1728975091959.png", threshold = 0.98, record_pos=(0.008, 0.985), resolution=(1080, 2412)),"设置Oscillation=350°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

# CH-1556 and CH-1557
# 功能为Circulation，设置模式为Turbo mode，然后设置Oscillation为350°
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1730179970117.png", record_pos=(-0.206, 0.477), resolution=(1080, 2412)),"功能为Circulation，切换成功")
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Turbo").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# 阈值要根据手机适配设置
assert_exists(Template(r"tpl1730188804785.png", threshold=0.98, record_pos=(-0.202, 0.001), resolution=(1080, 2412)),"模式设置为Turbo mode成功")

poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([0.841, -0.0052])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1728975091959.png", threshold = 0.98, record_pos=(0.008, 0.985), resolution=(1080, 2412)),"设置Oscillation=350°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

# CH-1558 and CH-1559
# 功能为Circulation，设置模式为AI mode，然后设置Oscillation为350°(前置条件：AI打开状态）
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Auto").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# 阈值要根据手机适配设置
assert_exists(Template(r"tpl1730180188375.png", threshold=0.98, record_pos=(-0.003, 0.075), resolution=(1080, 2412)),"模式设置为Auto成功")
swipe(Template(r"tpl1730190195686.png", record_pos=(0.318, -0.085), resolution=(1080, 2412)), vector=[-0.1382, -0.4457])
# 进入Setting页面
poco(text="Device Settings").click()
assert_equal(poco("android.widget.TextView").get_text(),"Settings","Setting页面进入成功")
swipe(Template(r"tpl1730190277692.png", record_pos=(0.078, 0.515), resolution=(1080, 2412)), vector=[-0.0608, -0.2414])
# 进入Auto+页面
poco(text="Auto+ mode (Beta)").click()
assert_equal(poco("android.widget.TextView").get_text(),"Auto+","Auto+页面进入成功")
# Enable AI mode
poco("com.philips.ph.homecare:id/autoplus_switch_id").click()
# 阈值要根据手机适配设置
assert_exists(Template(r"tpl1730191258573.png", threshold=0.98, record_pos=(0.011, -0.753), resolution=(1080, 2412)),"Enable AI mode成功")

# 返回上一级页面，检查AI mode显示是否正常
poco("Navigate up").click()
swipe(Template(r"tpl1730191451401.png", record_pos=(0.042, -0.721), resolution=(1080, 2412)), vector=[0.1189, 0.2872])
poco("Navigate up").click()
swipe(Template(r"tpl1730191479559.png", record_pos=(0.177, -0.34), resolution=(1080, 2412)), vector=[0.0664, 0.2142])
# 阈值要根据手机适配设置
assert_exists(Template(r"tpl1730191502023.png", threshold=0.98, record_pos=(-0.214, -0.31), resolution=(1080, 2412)),"AI mode显示正确")

# AI mode关闭，恢复初始化状态
swipe(Template(r"tpl1730190195686.png", record_pos=(0.318, -0.085), resolution=(1080, 2412)), vector=[-0.1382, -0.4457])
# 进入Setting页面
poco(text="Device Settings").click()
assert_equal(poco("android.widget.TextView").get_text(),"Settings","Setting页面进入成功")
swipe(Template(r"tpl1730190277692.png", record_pos=(0.078, 0.515), resolution=(1080, 2412)), vector=[-0.0608, -0.2414])
# 进入Auto+页面
poco(text="Auto+ mode (Beta)").click()
assert_equal(poco("android.widget.TextView").get_text(),"Auto+","Auto+页面进入成功")
# Disable AI mode
poco("com.philips.ph.homecare:id/autoplus_switch_id").click()
# 阈值要根据手机适配设置
assert_exists(Template(r"tpl1730192328447.png", threshold=0.98, record_pos=(0.004, -0.768), resolution=(1080, 2412)),"Disable AI mode成功")
# 返回上一级页面，检查Working mode显示是否正常
poco("Navigate up").click()
swipe(Template(r"tpl1730191451401.png", record_pos=(0.042, -0.721), resolution=(1080, 2412)), vector=[0.1189, 0.2872])
poco("Navigate up").click()
swipe(Template(r"tpl1730191479559.png", record_pos=(0.177, -0.34), resolution=(1080, 2412)), vector=[0.0664, 0.2142])
# 阈值要根据手机适配设置
assert_exists(Template(r"tpl1730192733290.png", threshold=0.95, record_pos=(-0.206, -0.305), resolution=(1080, 2412)),"AI mode关闭，模式显示为Auto")






