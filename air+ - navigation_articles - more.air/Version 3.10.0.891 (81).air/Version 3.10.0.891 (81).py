# -*- encoding=utf8 -*-
__author__ = "xfdzl"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.proxy import UIObjectProxy
from airtest.core.api import connect_device
import re
auto_setup(__file__)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
element=UIObjectProxy(poco=poco,name='com.philips.ph.homecare:id/policy_dialog_check',)
element=UIObjectProxy(poco=poco,name='com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon_container')
element=UIObjectProxy(poco=poco,name='com.philips.ph.homecare:id/navigation_settings')
element=UIObjectProxy(poco=poco,name='com.sec.android.app.launcher:id/apps_icon')

# #引用login的shell脚本
# from airtest.core.api import using
# using("air+-login.air")
# from common import common_functionassert_not_equal("实际值", "预测值", "请填写测试点.")

# common_function()
#避免中英文版本中的元素定义不同或者在源代码中会混用，这里采用全英文元素名称，即使只做了中文定义，也会判断寻找英文定义
#下同其他的shell


#如果提示start_btn报错，大概率是渲染树太深，暂时没找到，可以重新来一下   
swipe([514,835],[514,1435])
#启动添加设备
try:
    poco("com.philips.ph.homecare:id/dashboard_footer_btn").click()
except:
    poco("com.philips.ph.homecare:id/dashboard_section_add_btn").click()
sleep(1.0)
try:
    poco("com.philips.ph.homecare:id/philips_pairing_start_btn").click()
except:
    touch(Template(r"tpl1718617981895.png", record_pos=(0.018, 0.839), resolution=(1080, 2340)))


poco("com.philips.ph.homecare:id/philips_pairing_mode_next_btn").click()
#这里不同的手机，系统提示授权不一样，可能需要添加不同手机的授权shell，这里的是pixel5手机
sleep(11)
#不同手机搜索WiFi、buletuch的时间不一样


#unicorn 配网+设备控制
def validate_wifi(wifi):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, wifi):
        return True
    else:
        return False
wifi = "PHILIPS_MX_AC3421_13"
if validate_wifi(wifi):
    print("wifi名字没错")
else:
    print("设备WiFi名字不是PHILIPS_MX_AC3421_13，测试False")
    
    
#bluetooch配网-连接设备页面的发现设备，
try:
    poco(text="PHILIPS_MX_AC3421_13").click()
except:
    poco("com.philips.ph.homecare:id/appliance_item_layout_id").click()
sleep(1.0)

#基于实验lab内的设备连接的哪个WiFipoco("com.android.systemui:id/back").click()
try:
    poco(text="WLAN_Guest_temp").click()
except:
    poco(text="2F LAB").click()

poco("com.philips.ph.homecare:id/dialogEdit_edittext_id").click()
text("Versuni@23")
poco("android:id/button1").click()
sleep(13.0)
try:
    poco(text="Kitchen").click()
except:
    poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("android.widget.ScrollView").offspring("com.philips.ph.homecare:id/philips_pairing_name_list").child("android.widget.LinearLayout")[5].child("android.widget.RadioButton").click()
poco("com.philips.ph.homecare:id/philips_pairing_name_next_btn").click()
poco("com.philips.ph.homecare:id/philips_pair_finish_info_btn").click()
poco("com.philips.ph.homecare:id/philips_pair_mac_copy_btn").click()
try:
    poco("转到上一层级").click()
except:
    poco("Navigate up").click()

# poco("com.android.systemui:id/back").click()
# poco("com.android.systemui:id/back").click()
# poco("com.philips.ph.homecare:id/test_html_id").swipe([-0.6392, -0.0095])
# poco("com.philips.ph.homecare:id/dashboard_delete").click()
# poco("com.philips.ph.homecare:id/test_html_id").swipe([-0.8841, -0.0095])
# poco("com.philips.ph.homecare:id/dashboard_delete").click()
# poco("Navigate up").click()poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android.view.ViewGroup").swipe([-0.6673, -0.0104])


poco("com.philips.ph.homecare:id/philips_pair_finish_ok_btn").click()
sleep(1.0)
#设备功能项验证
#设备详情页面检测。no1直接页面操作比对结果
#poco("com.philips.ph.homecare:id/dashboard_control_auto_btn").click()
# pos = exists(Template(r"tpl1716529814365.png"))
# if pos:
#     touch(pos)
#验证“移除 unicorn 水箱警告”的功能
poco("com.philips.ph.homecare:id/dashboard_purifier_container").click()
sleep(1.0)
screen70=Template(r"tpl1718612464127.png", record_pos=(0.006, 0.699), resolution=(1080, 2340))

screen100=Template(r"tpl1718612464127.png",threshold=1, record_pos=(-0.001, 0.707), resolution=(1080, 2340))

assert_exists(screen70,"检查unicorn设备水箱弹窗逻辑")
# try:
#     assert_exists(screen100,"检查unicorn设备水箱安装到位不弹窗")
# except Exception: 
#     print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++断   言   失     败+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
assert_not_exists(screen100,"检查unicorn设备水箱安装到位会弹窗是bug")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++断   言   成     功+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/purifier_control_warn_container").child("android.widget.RelativeLayout")[0].child("com.philips.ph.homecare:id/appliance_warn_close_id").click()
poco("com.philips.ph.homecare:id/appliance_warn_close_id").click()

sleep(1.0)
poco("com.android.systemui:id/back").click()

#unicorn设备在home页功能验证
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/home_recyclerView_id").child("com.philips.ph.homecare:id/dashboard_purifier_container")[0].offspring("com.philips.ph.homecare:id/dashboard_control_power_btn").click()

screen1 = Template(r"tpl1717585665237.png", record_pos=(0.002, -0.051), resolution=(1080, 2400))
screen2 = Template(r"tpl1717585785499.png", record_pos=(0.002, -0.003), resolution=(1080, 2400))

assert_exists(screen1,"开关状态逻辑")
try:
    assert_exists(screen1,"开关状态没有影响到其他功能button")
except Exception as b1:
    print(str(b1))
assert_not_exists(screen2,"检查unicorn设备开关状态没有影响其他button")

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/home_recyclerView_id").child("com.philips.ph.homecare:id/dashboard_purifier_container")[0].offspring("com.philips.ph.homecare:id/dashboard_control_power_btn").click()



