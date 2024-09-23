# -*- encoding=utf8 -*-
__author__ = "xfdzl"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device

# 如果不需要多台机器联合测试，就可以使用#在代码的最前面给代码屏蔽掉
# 设置多机联合执行验证
# dev1 = connect_device("Android://127.0.0.1:5037/103cdef4")  # 第一台手机
# dev2 = connect_device("Android://127.0.0.1:5037/R58N12E57DV")  # 第二台手机

auto_setup(__file__)
poco = AndroidUiautomationPoco()

poco("com.android.systemui:id/home").click()
poco(text="飞利浦智净家").long_click()
# poco(text="Air+").long_click()



#三星A70手机      
poco("android.widget.FrameLayout").offspring("com.sec.android.app.launcher:id/drag_layer").offspring("应用程序信息, 按钮").offspring("com.sec.android.app.launcher:id/icon").click()
# #小米11手机
# poco("android.widget.FrameLayout").offspring("android:id/content").offspring("com.miui.home:id/system_shortcut_menu").child("android.widget.LinearLayout")[0].child("com.miui.home:id/item_icon").click()

poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.android.settings:id/content_frame").child("android.widget.LinearLayout").offspring("com.android.settings:id/recycler_view").child("android.widget.LinearLayout")[2].child("android.widget.RelativeLayout").click()
poco("com.android.settings:id/button1").click()
poco("com.android.settings:id/button1").click()
poco("com.android.systemui:id/home").click()
start_app("com.philips.ph.homecare")
#每次验证app需要重置app的时候可以操作。其他时期不要操作，防止造的数据丢失！！！！！！！！！！！！