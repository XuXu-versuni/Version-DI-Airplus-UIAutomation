# -*- encoding=utf8 -*-
__author__ = "XXu"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
#from poco.drivers.unity3d import UnityPoco
#from poco.drivers.std import StdPoco
#from poco.utils.device import VirtualDevice
#from poco.drivers.cocosjs import CocosJsPoco
#from DrissionPage import SessionPage
auto_setup(__file__)




#如果不需要多台机器联合测试，就可以使用#在代码的最前面给代码屏蔽掉
#设置多机联合执行验证
dev1 = connect_device("Android://127.0.0.1:5037/103cdef4")  # 连上第一台手机
dev2 = connect_device("Android://127.0.0.1:5037/R58N12E57DV")  # 第二台手机




#poco = CocosJsPoco()
#poco = StdPoco(15004, VirtualDevice('localhost'))
#poco = UnityPoco()
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
#page = SessionPage()



#这里接前一个shell---《air+-Configure network.air》
#设备较多，后面可能需要每台设备一个shell
#这里使用的是 "Nala"，前提条件是该设备已经配网

#先控制viewgroup面板
poco("com.philips.ph.homecare:id/dashboard_control_power_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/dashboard_control_power_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/dashboard_control_auto_btn").click()
sleep(1.0)
#取消选择
poco("com.philips.ph.homecare:id/dialog_control_sheet_cancel").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/dashboard_control_auto_btn").click()
sleep(1.0)
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.philips.ph.homecare:id/philips_control_sheet_list").child("android.widget.LinearLayout")[2].click()
sleep(1.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/dashboard_control_auto_btn").click()
sleep(1.0)
#还原设置
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.philips.ph.homecare:id/philips_control_sheet_list").child("android.widget.LinearLayout")[0].click()
sleep(1.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1.0)
#吊起设备控制详情页面
poco("com.philips.ph.homecare:id/dashboard_control_more_btn").click()

#设备设置调用“设置”中的设备设置项，可以直接用“air+ - setting.air”的shell
#说明书
swipe([500,1800],[500,500])
poco("com.philips.ph.homecare:id/purifier_control_manual").click()
sleep(2.0)
#抓取标识符图片---举的例子
screen70 = Template(r"tpl1716970893174.png", record_pos=(0.006, -0.072), resolution=(1080, 2400))
#threshold值修改，匹配度到100%
screen100 = Template(r"tpl1716970903383.png", threshold=1,record_pos=(-0.007, 0.007), resolution=(1080, 2400))
assert_exists(screen70,"检查图片内容是否匹配")        
# try:
#     assert_not_exists(screen100,"检查图片内容匹配度不是100%时不存在！")
# except Exception as a:
#     print(str(a))
#     assert_exists(screen100,"检查图片内容匹配度是100%时存在！")
sleep(1.0)
poco("转到上一层级").click()

swipe([500,500],[500,800])
sleep(1.0)
#运行状况
poco("com.philips.ph.homecare:id/purifier_control_health").click()
sleep(1.0)
swipe([500,1800],[500,500])
#清洁过滤器
poco("com.philips.ph.homecare:id/filter_item_clean_instruction_id").click()
sleep(1.0)
#swipe((0.203, 0.055), resolution=(1080, 2400)), vector=[-0.1116, -0.1923])

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dimWeb_layout_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View").child("android.view.View")[1].swipe([-0.2783, -0.4306])
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dimWeb_layout_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View").child("android.view.View")[1].swipe([-0.3681, -0.3944])
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dimWeb_layout_id").child("android.webkit.WebView").swipe([-0.3336, -0.5134])
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dimWeb_layout_id").child("android.webkit.WebView").swipe([-0.2346, -0.2205])
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dimWeb_layout_id").child("android.webkit.WebView").swipe([-0.2208, -0.47])
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dimWeb_layout_id").child("android.webkit.WebView").swipe([-0.2231, -0.5041])
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dimWeb_layout_id").child("android.webkit.WebView").swipe([-0.2139, -0.5466])
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dimWeb_layout_id").child("android.webkit.WebView").swipe([-0.2507, -0.4575])
poco("com.philips.ph.homecare:id/dimWeb_close_btn").click()
sleep(1.0)

#更换过滤器
poco("com.philips.ph.homecare:id/filter_item_replace_instruction_id").click()
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dimWeb_layout_id").child("android.webkit.WebView").swipe([-0.0805, -0.4544])
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dimWeb_layout_id").child("android.webkit.WebView").swipe([-0.138, -0.5486])
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dimWeb_layout_id").child("android.webkit.WebView").swipe([-0.1081, -0.589])
poco("com.philips.ph.homecare:id/dimWeb_close_btn").click()
sleep(1.0)

#清洁传感器
poco("com.philips.ph.homecare:id/filter_item_instruction_id").click()

#poco("com.philips.ph.homecare:id/dimWeb_webView_id").swipe([-0.1633, -0.5031])
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dimWeb_layout_id").child("android.webkit.WebView").swipe([-0.1035, -0.5704])
poco("com.philips.ph.homecare:id/dimWeb_close_btn").click()
sleep(1.0)
poco("转到上一层级").click()





#控制说明
poco("com.philips.ph.homecare:id/purifier_control_info").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/web_back_btn_id").click()
poco("com.philips.ph.homecare:id/purifier_control_info").click()
sleep(1.0)
# #poco('android.widget.TextView',type='android.widget.TextView',text='设备功能').click()

# poco("android.widget.LinearLayout").offspring("com.philips.ph.homecare:id/web_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View").child("android.view.View").child("android.widget.TextView")[1].click()
# sleep(1.0)
# poco("android.widget.LinearLayout").offspring("com.philips.ph.homecare:id/web_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View").child("android.view.View").child("android.widget.TextView")[0].click()
# sleep(1.0)
poco("com.philips.ph.homecare:id/web_back_btn_id").click()
#计划
poco("com.philips.ph.homecare:id/purifier_control_schedule").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/schedule_empty_create_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/schedule_weekdays_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/schedule_done_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/schedule_item_layout_id").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/schedule_remove_btn").click()
poco("android:id/button1").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/schedule_calendar_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/schedule_list_btn").click()
poco("转到上一层级").click()
sleep(1.0)

#控制module
poco("com.philips.ph.homecare:id/philips_control_light_btn_id").click()

#判断button是否真的变色/有效，同时注意听设备声音
screen70 = Template(r"tpl1716976834014.png", record_pos=(0.225, 0.5), resolution=(1080, 2400))
#threshold值修改，匹配度到100%
screen100 = Template(r"tpl1716976825816.png", record_pos=(0.225, 0.498), resolution=(1080, 2400))
assert_exists(screen70,"检查灯光开关是否有效")  
#还原状态值
poco("com.philips.ph.homecare:id/philips_control_light_btn_id").click()

sleep(1.0)




