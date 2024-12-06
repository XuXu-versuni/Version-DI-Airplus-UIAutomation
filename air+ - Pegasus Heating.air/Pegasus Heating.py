# -*- encoding=utf8 -*-
__author__ = "ytian1"

from airtest.core.api import *
from airtest.core.api import using
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
# element = UIObjectProxy(poco = poco,name = "com.philips.ph.homecare:id/display_theme_auto")
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

# 前置条件：已安装Air+ app，连接一台Pegasus 3in1设备
# 设备当前默认工作方式为circulation，默认模式为auto，默认选择角度为OFF,温度为27°下运行
# 设备信息：Samsung S22 Android 14

# CH-1510 Heating - Check the default mode and speed （65~75）
# CH-1511 Heating - Heating mode switch to Fan mode  （79~85）
# CH-1512 Heating - Heating mode switch to Purification （97~101）
# CH-1513 Heating - Set heating temp settings to Max  （113~119）
# CH-1514 Heating - Set heating temp settings to Min  （123~130）
# CH-1515 Heating - The working method is heating, select the Auto mode （132~137）
# CH-1516 Heating - The working method is Heating and select the Auto mode, then set the oscillation （140~155）
# CH-1518 Heating - The working method is heating, select the Sleep mode （159~165）
# CH-1519 Heating - The working method is Heating and select the Sleep mode, then set the oscillation （169~181）
# CH-1522 Heating - The working method is heating, select the Turbo clean mode （185~192）
# CH-1523 Heating - The working method is Heating and select the Turbo clean mode, then set the oscillation （195~207）
# CH-1524 Heating - The working method is heating, select the AI mode (211~233)
# CH-1525 Heating - The working method is Heating and select the AI mode, then set the oscillation (236~261)
# CH-1526 Heating - The working method is Heating, select the speed 1 (264~271)
# CH-1527 Heating - The working method is Heating and select the Speed 1, than set the Oscillation (274~289)
# CH-1528 Heating - The working method is Heating, select the speed 2 （292~299）
# CH-1529 Heating - The working method is Heating and select the Speed 2, than set the Oscillation （303~318）
# CH-1530 Heating - The working method is Heating, select the speed 3 （321~328）
# CH-1531 Heating - The working method is Heating and select the Speed 3, than set the Oscillation （332~344）
# CH-1532 Heating - The working method is Heating, select the speed 4 (347~354)
# CH-1533 Heating - The working method is Heating and select the Speed 4, than set the Oscillation (357~369)
# CH-1534 Heating - The working method is Heating, select the speed 5   (372~379)
# CH-1535 Heating  - The working method is Heating and select the Speed 5, than set the Oscillation (383~ 397)
# CH-1536 Heating - The working method is Heating, select the speed 6 (401~408)
# CH-1537 Heating  - The working method is Heating and select the Speed 6, than set the Oscillation (411~425)
# CH-1538 Heating - The working method is Heating, select the speed 7 (428~435)
# CH-1539 Heating - The working method is Heating and select the Speed 7, than set the Oscillation (439~454)
# CH-1540 Heating - The working method is Heating, select the speed 8 (457~464) 
# CH-1541 Heating - The working method is Heating and select the Speed 8, than set the Oscillation (468~480)
# CH-1542 Heating - The working method is Heating, select the speed 9 (484~491)
# CH-1543 Heating - The working method is Heating and select the Speed 9, than set the Oscillation (495~507)
# CH-1544 Heating - The working method is Heating, select the speed 10 （511~520）
# CH-1545 Heating - The working method is Heating and select the Speed 10, than set the Oscillation （524~538）
# CH-1546 Heating - Select the heating mode check device and App icon （71）
# CH-1613 Heating - Switch to heating from other modes, check the default button state (79~109)

#启动Air+ app
start_app("com.philips.ph.homecare")

#点击设备卡片进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_card_content").click()

#断言是否进入设备控制页面
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(), "Air Quality","已进入设备控制页面")
swipe([802,1914],[802,819])
sleep(2)

#CH-1510 Heating - Check the default mode and speed（65~75）
#切换功能为Heating
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0391, -0.0975])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前功能是否为heating
assert_exists(Template(r"tpl1732775243354.png", record_pos=(-0.205, -0.042), resolution=(1080, 2340)), "当前功能为Heating")
#断言默认的工作模式为Auto
assert_exists(Template(r"tpl1732775314135.png", record_pos=(-0.215, -0.156), resolution=(1080, 2340)), "当前工作模式为Auto")
#断言默认的风速为Auto
assert_exists(Template(r"tpl1732775337373.png", record_pos=(0.22, -0.151), resolution=(1080, 2340)), "当前风速为Auto")

#CH-1613 Heating - Switch to heating from other modes, check the default button state(79~109)
#CH-1511 Heating - Heating mode switch to Fan mode （79~85）
#切换功能为Fan
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0078, -0.0457])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前功能为Fan
assert_exists(Template(r"tpl1732775841699.png", record_pos=(-0.197, -0.004), resolution=(1080, 2340)), "当前功能为Fan")

#切换功能为Heating
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0391, -0.0975])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前功能是否为heating
assert_exists(Template(r"tpl1732775243354.png", record_pos=(-0.205, -0.042), resolution=(1080, 2340)), "当前功能为Heating")


# CH-1512 Heating - Heating mode switch to Purification （97~101）
#切换功能为Circulation
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前功能为Circulation
assert_exists(Template(r"tpl1732776898079.png", record_pos=(-0.195, 0.006), resolution=(1080, 2340)), "当前功能为Circulation")

#切换功能为Heating
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0391, -0.0975])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前功能是否为heating
assert_exists(Template(r"tpl1732775243354.png", record_pos=(-0.205, -0.042), resolution=(1080, 2340)), "当前功能为Heating")


#CH-1513 Heating - Set heating temp settings to Max （113~119）
#切换温度为37°
poco("com.philips.ph.homecare:id/philips_control_temperature_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0235, -0.3417])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前温度为37°
assert_exists(Template(r"tpl1732778262475.png", record_pos=(0.232, 0.303), resolution=(1080, 2340)), "当前温度为37°")


# CH-1514 Heating - Set heating temp settings to Min （123~130）
#切换温度为1°
poco("com.philips.ph.homecare:id/philips_control_temperature_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0156, -0.0241])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前温度为1°
assert_exists(Template(r"tpl1732778474918.png", record_pos=(0.227, 0.297), resolution=(1080, 2340)), "当前温度为1°")

#CH-1515 Heating - The working method is heating, select the Auto mode （132~137）
#切换工作模式为Auto
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Auto").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前工作模式为Auto
assert_exists(Template(r"tpl1728983001809.png", record_pos=(-0.211, 0.444), resolution=(1080, 2340),threshold = 0.98), "当前工作模式为Auto")

# CH-1516 Heating - The working method is Heating and select the Auto mode, then set the oscillation （140~155）
#将设备旋转角度设置为45°
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
sleep(1)
swipe(Template(r"tpl1728987071066.png", record_pos=(-0.37, 0.579), resolution=(1080, 2340)), vector=[0.0454, 0.0142])
sleep(3)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言旋转角度是否为45 
assert_exists(Template(r"tpl1728987141479.png", record_pos=(-0.008, 0.785), resolution=(1080, 2340), threshold = 0.9), "当前旋转角度为45°")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


#CH-1518 Heating - The working method is heating, select the Sleep mode （159~165）
#切换工作模式为Sleep
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Sleep").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前模式是否为sleep
assert_exists(Template(r"tpl1728982642558.png", record_pos=(-0.206, -0.032), resolution=(1080, 2340)), "当前模式为睡眠模式")


# CH-1519 Heating - The working method is Heating and select the Sleep mode, then set the oscillation （169~181）
#切换旋转角度为90
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前旋转角度为90
assert_exists(Template(r"tpl1729135393966.png", record_pos=(0.0, 0.486), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为90")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


# CH-1522 Heating - The working method is heating, select the Turbo clean mode （185~192）
#模式切到turbo
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Turbo").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前模式是否为Turbo
assert_exists(Template(r"tpl1728986203279.png", record_pos=(-0.208, 0.482), resolution=(1080, 2340)), "当前模式为turbo")
#断言当前功能自动切换到为Circulation
assert_exists(Template(r"tpl1732780304992.png", record_pos=(-0.202, 0.298), resolution=(1080, 2340)), "当前功能为circulation")

# CH-1523 Heating - The working method is Heating and select the Turbo clean mode, then set the oscillation （195~207）
#切换旋转角度为180
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
sleep(1)
swipe([146,1793], [520,1793])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728990637796.png", record_pos=(0.008, 0.582), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度180")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


# CH-1524 Heating - The working method is heating, select the AI mode (211~233)
#切换功能为Heating
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0391, -0.0975])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前功能是否为heating
assert_exists(Template(r"tpl1732775243354.png", record_pos=(-0.205, -0.042), resolution=(1080, 2340)), "当前功能为Heating")

swipe(Template(r"tpl1728987279257.png", record_pos=(0.203, -0.152), resolution=(1080, 2340)), vector=[-0.0742, -0.3376])

sleep(2)
poco("com.philips.ph.homecare:id/purifier_control_settings").click()
poco("com.philips.ph.homecare:id/philipsSetting_autoplus_id").click()
poco("com.philips.ph.homecare:id/autoplus_switch_id").click()
sleep(5)
poco("Navigate up").click()
poco("Navigate up").click()
sleep(2)
#滑动页面到旋转功能按钮处
swipe([774,734],[774,1523])
sleep(3)
#断言当前是否为Auto+ 模式(当前功能在Heating下，期望结果仍然显示Auto）
assert_exists(Template(r"tpl1729151730021.png", record_pos=(-0.206, 0.177), resolution=(1080, 2340), threshold = 0.98), "当前为Auto" )

# CH-1525 Heating - The working method is Heating and select the AI mode, then set the oscillation (236~261)
#设置旋转角度为270
# poco("com.philips.ph.homecare:id/philips_control_layout_id").swipe([0.0339, -0.148])
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[737,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前旋转角度为270
assert_exists(Template(r"tpl1729063280481.png", record_pos=(0.0, 0.645), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为270")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")

#AI关闭恢复初始
swipe([692,1827],[692,855])
sleep(2)
poco("com.philips.ph.homecare:id/purifier_control_settings").click()
poco("com.philips.ph.homecare:id/philipsSetting_autoplus_id").click()
poco("com.philips.ph.homecare:id/autoplus_switch_id").click()
sleep(5)
poco("Navigate up").click()
poco("Navigate up").click()
sleep(3)

# CH-1526 Heating - The working method is Heating, select the speed 1 (264~271)
#风速设置为1（期望结果为OFF)
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0261, 0.2238])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为off
assert_exists(Template(r"tpl1732785140659.png", record_pos=(0.221, -0.256), resolution=(1080, 2340)), "当前风速为OFF")


# CH-1527 Heating - The working method is Heating and select the Speed 1, than set the Oscillation (274~289)
#设置旋转角度为350
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[934,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
#断言当前旋转角度为350
assert_exists(Template(r"tpl1729144250572.png", record_pos=(-0.002, 0.296), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为350")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


# CH-1528 Heating - The working method is Heating, select the speed 2 （292~299）
#设置风速2
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0156, -0.0337])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为off
assert_exists(Template(r"tpl1732785140659.png", record_pos=(0.221, -0.256), resolution=(1080, 2340)), "当前风速为OFF")


# CH-1529 Heating - The working method is Heating and select the Speed 2, than set the Oscillation（303~318）
#设置旋转角度为45
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
sleep(1)
swipe(Template(r"tpl1728987071066.png", record_pos=(-0.37, 0.579), resolution=(1080, 2340)), vector=[0.0454, 0.0142])
sleep(3)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言旋转角度是否为45 
assert_exists(Template(r"tpl1728987141479.png", record_pos=(-0.008, 0.785), resolution=(1080, 2340), threshold = 0.9), "当前旋转角度为45°")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")

# CH-1530 Heating - The working method is Heating, select the speed 3 （321~328）
#风速设置为3
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0031, -0.0871])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为off
assert_exists(Template(r"tpl1732785140659.png", record_pos=(0.221, -0.256), resolution=(1080, 2340)), "当前风速为OFF")


# CH-1531 Heating - The working method is Heating and select the Speed 3, than set the Oscillation （332~344）
#切换旋转角度为90
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前旋转角度为90
assert_exists(Template(r"tpl1729135393966.png", record_pos=(0.0, 0.486), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为90")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")

# CH-1532 Heating - The working method is Heating, select the speed 4 (347~354)
#风速设置为4
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe([675,1572],[675,1324])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为off
assert_exists(Template(r"tpl1732785140659.png", record_pos=(0.221, -0.256), resolution=(1080, 2340)), "当前风速为OFF")

# CH-1533 Heating - The working method is Heating and select the Speed 4, than set the Oscillation (357~369)
#切换旋转角度为180
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
sleep(1)
swipe([146,1793], [520,1793])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728990637796.png", record_pos=(0.008, 0.582), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度180")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")

# CH-1534 Heating - The working method is Heating, select the speed 5  (372~379)
#风速设置为5
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe([675,1572],[675,1300])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为off
assert_exists(Template(r"tpl1732785140659.png", record_pos=(0.221, -0.256), resolution=(1080, 2340)), "当前风速为OFF")


# CH-1535 Heating  - The working method is Heating and select the Speed 5, than set the Oscillation (383~ 397)
#设置旋转角度为270
# poco("com.philips.ph.homecare:id/philips_control_layout_id").swipe([0.0339, -0.148])
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[737,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前旋转角度为270
assert_exists(Template(r"tpl1729063280481.png", record_pos=(0.0, 0.645), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为270")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


# CH-1536 Heating - The working method is Heating, select the speed 6 (401~408)
#风速设置为6
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe([675,1572],[675,1200])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为off
assert_exists(Template(r"tpl1732785140659.png", record_pos=(0.221, -0.256), resolution=(1080, 2340)), "当前风速为OFF")

# CH-1537 Heating  - The working method is Heating and select the Speed 6, than set the Oscillation (411~425)
#设置旋转角度为350
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[934,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
#断言当前旋转角度为350
assert_exists(Template(r"tpl1729144250572.png", record_pos=(-0.002, 0.296), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为350")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")

# CH-1538 Heating - The working method is Heating, select the speed 7 (428~435)
#风速设置为7
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe([675,1572],[675,1190])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为off
assert_exists(Template(r"tpl1732785140659.png", record_pos=(0.221, -0.256), resolution=(1080, 2340)), "当前风速为OFF")


# CH-1539 Heating - The working method is Heating and select the Speed 7, than set the Oscillation (439~454)
#设置旋转角度为45
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
sleep(1)
swipe(Template(r"tpl1728987071066.png", record_pos=(-0.37, 0.579), resolution=(1080, 2340)), vector=[0.0454, 0.0142])
sleep(3)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言旋转角度是否为45 
assert_exists(Template(r"tpl1728987141479.png", record_pos=(-0.008, 0.785), resolution=(1080, 2340), threshold = 0.9), "当前旋转角度为45°")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")

# CH-1540 Heating - The working method is Heating, select the speed 8 (457~464)
#风速设置为8
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe([675,1572],[675,1120])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为off
assert_exists(Template(r"tpl1732785140659.png", record_pos=(0.221, -0.256), resolution=(1080, 2340)), "当前风速为OFF")


# CH-1541 Heating - The working method is Heating and select the Speed 8, than set the Oscillation (468~480)
#切换旋转角度为90
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前旋转角度为90
assert_exists(Template(r"tpl1729135393966.png", record_pos=(0.0, 0.486), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为90")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


# CH-1542 Heating - The working method is Heating, select the speed 9 (484~491)
#风速设置为9
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe([675,1572],[675,1090])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为off
assert_exists(Template(r"tpl1732785140659.png", record_pos=(0.221, -0.256), resolution=(1080, 2340)), "当前风速为OFF")


# CH-1543 Heating - The working method is Heating and select the Speed 9, than set the Oscillation (495~507)
#切换旋转角度为180
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
sleep(1)
swipe([146,1793], [520,1793])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728990637796.png", record_pos=(0.008, 0.582), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度180")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


# CH-1544 Heating - The working method is Heating, select the speed 10 （511~520）
#风速设置为10
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe([675,1572],[675,1000])
sleep(3)
#断言当前选中的风速为10
assert_exists(Template(r"tpl1732868209991.png", record_pos=(0.007, 0.222), resolution=(1080, 2340),threshold = 0.98), "当前风速为10")
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为off
assert_exists(Template(r"tpl1732785140659.png", record_pos=(0.221, -0.256), resolution=(1080, 2340)), "当前风速为OFF")


# CH-1545 Heating - The working method is Heating and select the Speed 10, than set the Oscillation （524~538）
#设置旋转角度为270
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[737,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前旋转角度为270
assert_exists(Template(r"tpl1729063280481.png", record_pos=(0.0, 0.645), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为270")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")

#返回到App主页
poco("com.android.systemui:id/back").click()
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(), "My Devices","当前在App主页")






