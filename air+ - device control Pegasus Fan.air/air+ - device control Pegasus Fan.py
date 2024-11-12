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
# 设备当前默认工作方式为circulation，默认模式为auto，默认选择角度为OFF下运行
# 设备信息：Samsung S22 Android 14


#启动Air+ app
start_app("com.philips.ph.homecare")

#点击设备卡片进入设备控制页面
poco("com.philips.ph.homecare:id/dashboard_card_content").click()

#断言是否进入设备控制页面
assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(), "Air Quality","已进入设备控制页面")

#切换功能为Fan
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
swipe(Template(r"tpl1728976254396.png", record_pos=(-0.003, 0.274), resolution=(1080, 2340)), vector=[-0.1948, -0.0429])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前功能按钮为Fan
assert_exists(Template(r"tpl1728983682159.png", record_pos=(-0.195, 0.493), resolution=(1080, 2340)), "当前功能为Fan")

#在Fan功能下检查默认的工作模式和风速
#断言工作按钮默认模式为Auto
assert_exists(Template(r"tpl1728983001809.png", record_pos=(-0.211, 0.444), resolution=(1080, 2340),threshold = 0.98), "当前工作模式为Auto")
#断言功能为Fan下，风速按钮默认模式为Auto
assert_exists(Template(r"tpl1728983793744.png", record_pos=(0.214, 0.346), resolution=(1080, 2340)), "当前风速为Auto")

#在控制页面滑动到旋转按钮位置
swipe(Template(r"tpl1729058387722.png", record_pos=(0.381, -0.048), resolution=(1080, 2340)), vector=[-0.0922, -0.3113])
sleep(3)


#Fan功能下，工作模式切换到Auto，旋转角度切换到45
#将设备旋转角度设置为45°
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
sleep(1)
swipe(Template(r"tpl1728987071066.png", record_pos=(-0.37, 0.579), resolution=(1080, 2340)), vector=[0.0454, 0.0142])
sleep(3)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3)
#断言旋转角度是否为45 【实际旋转角度其它数字后运行该代码不会报错】
assert_exists(Template(r"tpl1728987141479.png", record_pos=(-0.008, 0.785), resolution=(1080, 2340), threshold = 0.9), "当前旋转角度为45°")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")

#Fan功能下，工作模式切换到sleep，旋转角度切换到90
#模式切到sleep
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Sleep").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前模式是否为sleep
assert_exists(Template(r"tpl1728982642558.png", record_pos=(-0.206, -0.032), resolution=(1080, 2340)), "当前模式为睡眠模式")

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

#Fan功能下，工作模式切换到Turbo，旋转角度切换到90
#模式切到turbo
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Turbo").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前模式是否为Turbo
assert_exists(Template(r"tpl1728986203279.png", record_pos=(-0.208, 0.482), resolution=(1080, 2340)), "当前模式为turbo")

#切换旋转角度为90
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
#断言当前旋转角度为90
assert_exists(Template(r"tpl1729135393966.png", record_pos=(0.0, 0.486), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为90")




#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")

#Fan功能下，工作模式切换到AI，旋转角度切换到180
#模式切换为Auto
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Auto").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前模式是否为Auto
assert_exists(Template(r"tpl1728992471968.png", record_pos=(-0.194, -0.232), resolution=(1080, 2340), threshold = 1), "当前模式为auto")

#滑动到设备控制页面底部，打开AI功能
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
#将工作模式切换到Fan
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0104, -0.0517])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前是否为Auto+ 模式(当前功能在Fan下，期望结果仍然显示Auto）
assert_exists(Template(r"tpl1729151730021.png", record_pos=(-0.206, 0.177), resolution=(1080, 2340), threshold = 0.98), "当前为Auto" )

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

#AI关闭恢复初始
swipe([692,1827],[692,855])
sleep(2)
poco("com.philips.ph.homecare:id/purifier_control_settings").click()
poco("com.philips.ph.homecare:id/philipsSetting_autoplus_id").click()
poco("com.philips.ph.homecare:id/autoplus_switch_id").click()
sleep(5)
poco("Navigate up").click()
poco("Navigate up").click()
poco("com.philips.ph.homecare:id/purifier_control_video").swipe([-0.0469, 0.2948])


#功能为Fan，风速为1，选择旋转角度为270°
#风速设置为1
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0261, 0.2238])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为1
assert_exists(Template(r"tpl1729062095186.png", record_pos=(0.21, 0.705), resolution=(1080, 2340), threshold = 0.98), "当前风速为1")

#设置旋转角度为270
poco("com.philips.ph.homecare:id/philips_control_layout_id").swipe([0.0339, -0.148])
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


#功能为Fan，风速为2，选择旋转角度为350°
#风速设置为2
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0156, -0.0337])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为2
assert_exists(Template(r"tpl1729063689030.png", record_pos=(0.207, 0.341), resolution=(1080, 2340),threshold = 0.98), "当前风速为2")

#设置旋转角度为350
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[931,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前旋转角度为350
assert_exists(Template(r"tpl1729063906281.png", record_pos=(0.003, 0.641), resolution=(1080, 2340),threshold = 0.98), "当前旋转角度为350")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


#功能为Fan，风速为3，选择旋转角度为45°
#风速设置为3
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0156, -0.0337])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为3
assert_exists(Template(r"tpl1729134964508.png", record_pos=(0.214, 0.185), resolution=(1080, 2340),threshold = 0.98), "当前风速为3")

#设置旋转角度为45
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[194,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前旋转角度为45
assert_exists(Template(r"tpl1729135113288.png", record_pos=(0.004, 0.485), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为45")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


#功能为Fan，风速为4，选择旋转角度为90°
#风速设置为4
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0156, -0.0337])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为4
assert_exists(Template(r"tpl1729135259741.png", record_pos=(0.214, 0.19), resolution=(1080, 2340), threshold = 0.98), "当前风速为4")

#设置旋转角度为90
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[306,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
#断言当前旋转角度为90
assert_exists(Template(r"tpl1729135393966.png", record_pos=(0.0, 0.486), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为90")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


#功能为Fan，风速为5，选择旋转角度为180°
#风速设置为5
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0156, -0.0337])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为5
assert_exists(Template(r"tpl1729143781959.png", record_pos=(0.205, -0.002), resolution=(1080, 2340), threshold = 0.98), "当前风速为5")

#设置旋转角度为180
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[526,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
#断言当前旋转角度为180
assert_exists(Template(r"tpl1729143915500.png", record_pos=(-0.003, 0.296), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为180")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


#功能为Fan，风速为6，选择旋转角度为270°
#风速设置为6
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0156, -0.0337])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为6
assert_exists(Template(r"tpl1729143977654.png", record_pos=(0.21, -0.006), resolution=(1080, 2340), threshold = 0.98), "当前风速为6")

#设置旋转角度为270
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[743,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
#断言当前旋转角度为270
assert_exists(Template(r"tpl1729144053102.png", record_pos=(-0.003, 0.294), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为270")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


#功能为Fan，风速为7，选择旋转角度为350°
#风速设置为7
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0156, -0.0337])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为7
assert_exists(Template(r"tpl1729144156597.png", record_pos=(0.21, -0.007), resolution=(1080, 2340), threshold = 0.98), "当前风速为7")

#设置旋转角度为350
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[934,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
#断言当前旋转角度为350
assert_exists(Template(r"tpl1729144250572.png", record_pos=(-0.002, 0.296), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为90")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


#功能为Fan，风速为8，选择旋转角度为45°
#风速设置为8
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0156, -0.0337])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为8
assert_exists(Template(r"tpl1729144553948.png", record_pos=(0.218, -0.01), resolution=(1080, 2340), threshold = 0.98), "当前风速为8")

#设置旋转角度为45
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[197,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
#断言当前旋转角度为45
assert_exists(Template(r"tpl1729144628700.png", record_pos=(0.004, 0.294), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为45")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


#功能为Fan，风速为9，选择旋转角度为90°
#风速设置为9
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0156, -0.0337])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为9
assert_exists(Template(r"tpl1729144803751.png", record_pos=(0.208, -0.005), resolution=(1080, 2340), threshold = 0.98), "当前风速为9")

#设置旋转角度为90
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[306,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
#断言当前旋转角度为90
assert_exists(Template(r"tpl1729135393966.png", record_pos=(0.0, 0.486), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为90")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


#功能为Fan，风速为10，选择旋转角度为180°
#风速设置为10
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0156, -0.0337])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2)
#断言当前风速为10
assert_exists(Template(r"tpl1729144918850.png", record_pos=(0.207, -0.004), resolution=(1080, 2340), threshold = 0.98), "当前风速为10")

#设置旋转角度为180
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([143,1793],[520,1793])
sleep(2)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1)
#断言当前旋转角度为180
assert_exists(Template(r"tpl1729145372232.png", record_pos=(-0.004, 0.295), resolution=(1080, 2340), threshold = 0.98), "当前旋转角度为180")

#将旋转角度恢复初始
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.6036, 0.0099])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言旋转角度显示初始值off
assert_exists(Template(r"tpl1728985167328.png", record_pos=(0.012, 0.644), resolution=(1080, 2340)), "旋转角度显示off")


#将设备功能恢复初始Circulation，工作模式初始为Auto
#切换功能为Circulation
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当前功能为circulation
assert_exists(Template(r"tpl1729236333802.png", record_pos=(-0.205, -0.218), resolution=(1080, 2340), threshold = 0.98), "当前功能为circulation")

#切换工作模式为auto
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Auto").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
#断言当然工作模式为auto
assert_exists(Template(r"tpl1729236166234.png", record_pos=(-0.197, -0.364), resolution=(1080, 2340), threshold = 0.98), "当前工作模式为auto")



