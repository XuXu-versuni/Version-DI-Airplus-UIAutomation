# -*- encoding=utf8 -*-
__author__ = "xfdzl"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# element=UIObjectProxy(poco=poco,name="zOrders:{'global':0, 'local'5}")
# element=UIObjectProxy(poco=poco,name="zOrders :  {'global': 0, 'local': 14}")
# element=UIObjectProxy(poco=poco,name="zOrders :  {'global': 0, 'local': 2}")
auto_setup(__file__)

'''
本代码要和Py_ADB_Log.py联动做切换语言会不会导致appcrash的验证
'''


# #循环遍历同名节点，比如有很多一样的"android.widget.LinearLayout "
# def find_point(poco,root_name,child_name,timeout = 0.1):
#     start = time.time()
#     result = []
#     while len(result) == 0 and (time.time() - start < timeout):
#         freeze = poco.freeze()
#         root = freeze(root_name)
#         if root.exists():
#             queue = []
#             queue.append(root)
#             while len(queue) > 0:
#                 node = queue[0]
#                 queue.pop(0)
#                 if node.get_name() == child_name:
#                     result.append(node)
#                 if node.child().exists(): 
#                     for item in node.child():
#                         queue.append(item)
#         sleep(0.1)
#     return result


# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[0].child("android.widget.RadioButton")

# item_text_obj = poco(text="Chinese, Simplified")  # 找到待测名称对应的元素
# foo_parent = item_text_obj.parent()
# foo_childs = foo_parent.child()
# target_obj = foo_childs[3].child()[1].child()[2]
# target_obj.click()


# # 索引错误会导致找不到元素或点错元素
# # target_obj = foo_childs[4].child()[0].child()[0]  
# target_obj = foo_childs[4].child()[1].child()[0]  # 这才是正确的索引
# target_obj.click()






# button_list = ["","","","","","","","","","","","",]

# poco("zOrders :  {'global': 0, 'local': 2}").click() 

# def perform_operations():
# time.sleep(2.0)
# #poco("zOrders:{'global':0, 'local'5}").click()
# poco("com.philips.ph.homecare:id/navigation_settings").click()
# poco("com.philips.ph.homecare:id/settings_display_id").click()
# time.sleep(2.0)
# #poco("zOrders :  {'global': 0, 'local': 14} ").click()

# poco("com.philips.ph.homecare:id/display_language").click()
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[0].click()
# poco("com.philips.ph.homecare:id/menu_done_id").click()
# poco("android:id/button1").click()
# sleep(2.0)
# start_app('com.philips.ph.homecare')
    # 等待应用启动并加载完成
    #wait_startup(timeout=30)
# pass



# # 定义一个函数来执行一系列操作

#     # 这里添加你需要循环执行的操作
#     # 例如：截图、滑动、点击等
#     pass

# # 找到当前页面上所有的按钮元素
# # 注意：这里的定位方式可能需要根据你的实际应用进行调整
# buttons = find_elements("class_name", "android.widget.Button")

# # 逐一循环点击找到的按钮
# for button in buttons:
#     # 执行一系列操作
#     perform_operations()

#     # 点击当前按钮
#     click(button)


time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
poco("com.philips.ph.homecare:id/display_language").click()
sleep(2.0)
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[0].click()
poco(text="Arabic").click()
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
time.sleep(2.0)
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
time.sleep(2.0)
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


time.sleep(2.0)
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
time.sleep(2.0)
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
poco(text="Norwegian Bokmål").click()

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
