# -*- encoding=utf8 -*-

# -*- coding: UTF-8 -*-

__author__ = "xfdzl"

from airtest.core.api import *
from airtest.core.api import connect_device, start_app, stop_app, swipe
from airtest.core.error import AirtestError
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
element = UIObjectProxy(poco=poco,name = "com.philips.ph.homecare:id/display_language")
element = UIObjectProxy(poco = poco,name = "android:id/button1")
# element=UIObjectProxy(poco=poco,name="zOrders:{'global':0, 'local'5}")
# element=UIObjectProxy(poco=poco,name="zOrders :  {'global': 0, 'local': 14}")
# element=UIObjectProxy(poco=poco,name="zOrders :  {'global': 0, 'local': 2}")
auto_setup(__file__)



'''
本代码要和Py_ADB_Log.py、Android-crash-log.py 联动做切换语言会不会导致appcrash的验证
'''
#本代码适配完成lg的pixel5手机，三星的A70手机，其他手机视频             请照葫芦画瓢


time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
poco(text="Arabic").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')
    
time.sleep(3.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[2].click()
poco(text="Bulgarian").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')

#这里是中文，默认启动就是中文，切成中文后再启动这个脚本shell
# time.sleep(2.0)
# poco("com.philips.ph.homecare:id/navigation_settings").click()
# poco("com.philips.ph.homecare:id/settings_display_id").click()
# time.sleep(2.0)
# poco("com.philips.ph.homecare:id/display_language").click()
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[3].click()
# poco("com.philips.ph.homecare:id/menu_done_id").click()
# poco("android:id/button1").click()
# sleep(2.0)
# start_app('com.philips.ph.homecare')

time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(3.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
poco(text="Chinese, Traditional").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')


time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(3.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[5].click()
poco(text="Chinese, Traditional(Hong Kong)").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')

time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[6].click()
poco(text="Czech").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')


time.sleep(3.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(3.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[7].click()
poco(text="Danish").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')


time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[8].click()
poco(text="Dutch").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')


time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[9].click()
poco(text="English").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')


time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[10].click()
poco(text="Estonian").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')


time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[11].click()
poco(text="Finnish").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')


time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[12].click()
poco(text="French").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')


time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
poco(text="German").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')



time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
poco(text="Hungarian").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')



time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
poco(text = "Indonesia").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')



time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
poco(text="Italian").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')



time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
poco(text="Japanese").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')




time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
poco(text="Korean").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')




time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
poco(text="Latvian").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')



time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
poco(text="Lithuanian").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')



time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
poco(text="Malay").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')



time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
touch(Template(r"tpl1720441848759.png", record_pos=(-0.279, 0.363), resolution=(1080, 2400)))
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')



time.sleep(3.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
poco(text="Persian").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')

time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
poco(text="Polish").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')


time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
swipe([500,2100],[500,400])
poco(text="Portuguese").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')



time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
swipe([500,2100],[500,400])
poco(text="Romanian").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')




time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
swipe([500,2100],[500,400])
poco(text="Slovak").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')




time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
swipe([500,2100],[500,400])
poco(text="Spanish").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')




time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
swipe([500,2100],[500,400])
poco(text="Swedish").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')




time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
swipe([500,2100],[500,400])
poco(text="Thai").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')




time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
swipe([500,2100],[500,400])
poco(text="Turkish").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')





time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
swipe([500,2100],[500,400])
poco(text="Ukrainian").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')




time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
swipe([500,2100],[500,400])
swipe([500,2100],[500,400])
poco(text="Vietnamese").click()

sleep(2.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(2.0)
poco("android:id/button1").click()
sleep(2.0)
start_app('com.philips.ph.homecare')
