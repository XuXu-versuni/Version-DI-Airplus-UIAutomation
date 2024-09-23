# -*- encoding=utf8 -*-
__author__ = "XXu"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.proxy import UIObjectProxy
from airtest.core.api import device
from airtest.core.assertions import *
auto_setup(__file__)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

element=UIObjectProxy(poco=poco,name="zOrders:{'global':0, 'local':3}")

# #如果不需要多台机器联合测试，就可以使用#在代码的最前面给代码屏蔽掉
# #设置多机联合执行验证
# dev1 = connect_device("Android://127.0.0.1:5037/103cdef4")  # 第一台手机
# dev2 = connect_device("Android://127.0.0.1:5037/R58N12E57DV")  # 第二台手机



#我的设备 “+”
poco("com.philips.ph.homecare:id/dashboard_section_add_btn").click()
#poco("转到上一层级").click()
#poco("com.philips.ph.homecare:id/dashboard_footer_btn").click()

#开始
try:
    poco("com.philips.ph.homecare:id/philips_pairing_start_btn").click()
except:
    poco("com.philips.ph.homecare:id/philips_pair_location_permission_btn").click()
    poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
assert_equal("如何让 Wi-Fi 图标呈橙色闪烁？", "如何让 Wi-Fi 图标呈橙色闪烁？", "判断文字button是否有误.")

poco("com.philips.ph.homecare:id/philips_pairing_mode_setup_btn").click()
sleep(1.0)

#滑动寻找页面元素
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.webkit.WebView").swipe([-0.0437, -0.5797])
sleep(3.0)

    
try:
    poco("空气净化器 1000i 系列").click()
except:
    poco("Purifiers Series 1000i").click()

sleep(3.0)
#抓取标识符图片---举的例子

exists(Template(r"tpl1719885936584.png", record_pos=(0.001, -0.479), resolution=(1080, 2340)))
sleep(1.0)
try:
    poco("返回").click()
except:
    poco("Back").click()

try:
    poco("com.android.systemui:id/back").click()
except:
    poco("Navigate up").click()
#这个时候要触发设备进入配网模式！！！！！！！！！！！！！！！！！
#开始准备验证链接，前提是设备打开wifi配网模式，预留给配置15s时间,这里是针对可以修改wifi网络的设备，不涉及蓝牙配网
#下一页
poco("com.philips.ph.homecare:id/philips_pairing_mode_next_btn").click()
sleep(10.0)
#链接其他设备
poco("com.philips.ph.homecare:id/philips_pairing_searching_another").click()
sleep(1.0)
#打开设置
try:
    poco("com.philips.ph.homecare:id/philips_pair_wifi_setting_btn").click()
except:
    poco("android:id/button1").click()

sleep(1.0)
#防止设备wifi不在其内，打开系统wifi
try:
    poco("com.android.settings:id/see_more").click()
except:
    poco("com.philips.ph.homecare:id/philips_pairing_searching_help").click()
sleep(1.0)

poco(text="PHILIPS Setup").click()
sleep(3.0)
poco("com.android.systemui:id/back").click()
sleep(6.0)
#保持链接
#逻辑判断刷新之后设备WiFi(PHLIPIS Setup)是否存在
#给设备输入新wifi密码，刷新WiFi列表
pos = exists(Template(r"tpl1716529814365.png"))
if pos:
    touch(pos)
sleep(3.0)

poco("com.philips.ph.homecare:id/philips_pairing_searching_refresh").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/philips_pairing_searching_refresh").click()
sleep(2.0)


#再次连接公网WiFi（WLAN_Guest_temp）
poco(text="WLAN_Guest_temp").click()

#吊起键盘输入密码
poco("com.philips.ph.homecare:id/dialogEdit_edittext_id").click()
text("Versuni@23")
poco("android:id/button1").click()
#这个过程等待app把数据写入设备
sleep(120.0)



#配置设备空间
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("android.widget.ScrollView").offspring("com.philips.ph.homecare:id/philips_pairing_name_list").child("android.widget.LinearLayout")[3].click()
sleep(1.0)
poco("com.philips.ph.homecare:id/philips_pairing_name_next_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/personalize_questionnaire_next").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/personalize_questionnaire_next").click()
poco("com.philips.ph.homecare:id/philips_pair_finish_ok_btn").click()


#设备详情页面检测。no1直接页面操作比对结果
poco("com.philips.ph.homecare:id/dashboard_control_power_btn").click()
sleep(1.0)
#assert_exists(Template(r"tpl1716376740124.png", record_pos=(0.038, 0.257), resolution=(1080, 2400)), "")

assert_exists(Template(r"tpl1716376773692.png", record_pos=(0.029, 0.256), resolution=(1080, 2400)), "判断开关button是否真的联动了其他button")




