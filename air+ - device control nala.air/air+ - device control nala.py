# -*- encoding=utf8 -*-
__author__ = "xfdzl"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
from poco.proxy import UIObjectProxy
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

#这里是单独对nali设备进行的设备控制的uiautomation
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/home_recyclerView_id").child("com.philips.ph.homecare:id/dashboard_purifier_container")[1].offspring("android.view.ViewGroup").click()


exists(Template(r"tpl1719898876198.png", record_pos=(-0.002, -0.08), resolution=(1080, 2340)))

swipe([564,1840],[564,840])
#验证在设备关闭状态下，各单元的显示是否正确
exists(Template(r"tpl1719899270101.png", record_pos=(0.004, 0.03), resolution=(1080, 2340)))

#断言状态对不对

screen01 = Template(r"tpl1719899924483.png", record_pos=(-0.374, 0.188), resolution=(1080, 2340))
screen02 = 
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/home_recyclerView_id").child("com.philips.ph.homecare:id/dashboard_purifier_container")[1].offspring("com.philips.ph.homecare:id/dashboard_control_power_btn")
#poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/home_recyclerView_id").child("com.philips.ph.homecare:id/dashboard_purifier_container")[1].offspring("com.philips.ph.homecare:id/dashboard_control_power_btn")

flag = True
if flag:
    print("zhuangtaishizhen")
    
text("com.philips.ph.homecare:id/dashboard_control_power_btn") = True










