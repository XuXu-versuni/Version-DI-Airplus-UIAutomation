# -*- encoding=utf8 -*-
__author__ = "xfdzl"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",], project_root="C:/Users/xfdzl/Desktop/air+ - android-0529/air+ - navigation_articles - more.air/air+ - navigation_articles - more-1")


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)


# # #如果不需要多台机器联合测试，就可以使用#在代码的最前面给代码屏蔽掉
# # #设置多机联合执行验证
dev1 = connect_device("Android://127.0.0.1:5037/103cdef4")  # 第一台手机
#dev2 = connect_device("Android://127.0.0.1:5037/R58N12E57DV")  # 第二台手机


#底部“文章”

poco("com.philips.ph.homecare:id/navigation_articles").click()
sleep(3.0)

swipe([536,2000],[536,1000])
swipe([536,1000],[536,2000])
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/articles_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[0].swipe([-0.4325, 0.0279])
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/articles_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[0].swipe([0.4325, 0.0279])


poco(text="建议").click()
poco(text="总体").click()
poco(text="病毒").click()
sleep(2.0)
#poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/articles_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[1].click()
poco(text="307").click()
sleep(1.0)
poco("com.android.systemui:id/back").click()
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/navigation_articles").offspring("com.philips.ph.homecare:id/navigation_bar_item_icon_view").click()


