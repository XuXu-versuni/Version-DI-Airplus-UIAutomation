# -*- encoding=utf8 -*-
__author__ = "xfdzl"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.proxy import UIObjectProxy
from airtest.core.api import connect_device

auto_setup(__file__)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
element=UIObjectProxy(poco=poco,name='com.philips.ph.homecare:id/policy_dialog_check',)
element=UIObjectProxy(poco=poco,name='com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon_container')
element=UIObjectProxy(poco=poco,name='com.philips.ph.homecare:id/navigation_settings')
element=UIObjectProxy(poco=poco,name='com.sec.android.app.launcher:id/apps_icon')

res = element.exists()
print(res)
if res:
    element.click()
       
        
        
# #如果不需要多台机器联合测试，就可以使用#在代码的最前面给代码屏蔽掉  
# #设置多机联合执行验证
# dev1 = connect_device("Android://127.0.0.1:5037/103cdef4")  # 第一台手机
# dev2 = connect_device("Android://127.0.0.1:5037/R58N12E57DV")  # 第二台手机

#登录之前尽量要重置app的数据
# 登录初始化后的app
# time.sleep(2.0)
start_app("com.philips.ph.homecare")
sleep(2.0)

#检查声明跳转是否正确
touch([200,1152])
sleep(2.0)
try:
    poco("转到上一层级").click()
except:
    poco("Navigate up").click()

sleep(1.0)
touch([377,1152])
sleep(2.0)
try:
    poco("转到上一层级").click()
except:
    poco("Navigate up").click()
sleep(1.0)
touch([157,1347])
sleep(2.0)
touch([905,1515])
sleep(1.0)
poco("com.philips.ph.homecare:id/main_coordinator_id").swipe([-0.7348, 0.0329])
sleep(1.0)
poco("com.philips.ph.homecare:id/main_coordinator_id").swipe([-0.8786, 0.0339])
sleep(1.0)
poco("com.philips.ph.homecare:id/welcome_enter_app_btn").click()
sleep(1.0)
#同意页面详情场景
poco("com.philips.ph.homecare:id/consent_link_btn").click()
sleep(3.0)

touch(Template(r"tpl1715407877324.png", record_pos=(-0.419, -0.98), resolution=(1080, 2400)))

poco("com.philips.ph.homecare:id/consent_accept_btn").click()
sleep(1.0)
#查看隐私政策h5页面
poco("com.philips.ph.homecare:id/config_privacy_id").click()
sleep(2.0)
poco("转到上一层级").click()
poco("com.philips.ph.homecare:id/config_terms_id").click()
sleep(3.0)
poco("转到上一层级").click()
sleep(1.0)
#进行授权隐私设置
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/config_privacy_layout_id").child("android.widget.RadioButton").click()
sleep(1.0)
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/config_terms_layout_id").child("android.widget.RadioButton").click()
sleep(1.0)
#取消勾选，查看“继续”button的状态
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/config_privacy_layout_id").child("android.widget.RadioButton").click()
sleep(1.0)
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/config_terms_layout_id").child("android.widget.RadioButton").click()
sleep(1.0)
#继续选中勾选，检查button状态
poco("com.philips.ph.homecare:id/main_coordinator_id").click()
sleep(1.0)
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/config_privacy_layout_id").child("android.widget.RadioButton").click()
#sleep(1.0)
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/config_terms_layout_id").child("android.widget.RadioButton").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/config_continue_id").click()
sleep(1.0)
#位置授权
poco("com.philips.ph.homecare:id/ai_location_introduce_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/ai_location_introduce_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/ai_location_introduce_btn").click()
sleep(1.0)


#场景一，不共享位置
#不论场景如何先处理设置中的Internal中的backend的值
poco("com.philips.ph.homecare:id/ai_location_accept_btn").click()
sleep(1.0)

#拒绝获取信息
poco("com.android.permissioncontroller:id/permission_deny_button").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/ai_location_accept_btn").click()
sleep(1.0)
poco("com.android.permissioncontroller:id/permission_deny_button").click()
sleep(1.0)
poco("android.widget.ImageButton").click()
sleep(1.0)

#打开设置按钮
poco("com.philips.ph.homecare:id/navigation_settings").click()
sleep(1.0)

poco("com.philips.ph.homecare:id/settings_internal_id").click()
sleep(1.0)

poco("com.philips.ph.homecare:id/developer_philips_env_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/developer_info_btn").click()
sleep(1.0)

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/developer_container_id").offspring("com.philips.ph.homecare:id/developer_env_list").child("android.widget.LinearLayout")[0].child("android.widget.RadioButton")
sleep(1.0)

poco("转到上一层级").click()
sleep(1.0)
poco("转到上一层级").click()
sleep(1.0)

poco("android:id/button1").click()
sleep(1.0)


#重启app
start_app("com.philips.ph.homecare")
sleep(10.0)


#允许获取位置信息
poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
poco("com.philips.ph.homecare:id/dashboard_footer_btn").click()
sleep(2.0)

#先切到设置页面
poco("com.philips.ph.homecare:id/navigation_settings").click()
sleep(1.0)

#再切回家用主功能页防止天气数据页面没出来
poco("com.philips.ph.homecare:id/navigation_home").click()
sleep(1.0)


poco("com.philips.ph.homecare:id/dashboard_footer_btn").click()
sleep(1.0)

#添加新位置信息
poco("com.philips.ph.homecare:id/places_edit_add_id").click()
sleep(1.0)
#搜索
poco("com.philips.ph.homecare:id/menu_search").click()
sleep(1.0)

poco("com.philips.ph.homecare:id/search_src_text").click()
text("南京")
sleep(2.0)
poco("com.philips.ph.homecare:id/menu_search").click()


########20240517以上shell和业务功能全部调试完毕

#多层级UI数，需要到下一层底层定位值

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/places_recyclerView_id").child("android.widget.LinearLayout")[1].click()
sleep(1.0)
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/places_recyclerView_id").child("android.widget.LinearLayout").click()
sleep(1.0)
#继续检测多层级返回数据以及页面
poco("com.philips.ph.homecare:id/places_edit_add_id").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/menu_search").click()
sleep(1.0)


text("三里街")
sleep(1.0)
#选择结果的第一行
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/places_recyclerView_id").child("android.widget.LinearLayout")[0].click()
sleep(1.0)
#继续选择UI数层级，返回的多层行政区域数据
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/places_recyclerView_id").child("android.widget.LinearLayout").child("android.widget.LinearLayout").click()
sleep(1.0)
#返回定位数据后的“家用页面”查看返回的weather页面，以及返回数据是否正常显示
poco("转到上一层级").click()

poco(text="管理位置").click()
sleep(1.0)
#点击编辑
poco("com.philips.ph.homecare:id/menu_edit_id").click()
sleep(1.0)
#修改定位地点顺序
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/fragment_container_id").offspring("com.philips.ph.homecare:id/places_edit_list_id").child("android.widget.LinearLayout")[2].offspring("com.philips.ph.homecare:id/places_edit_reorder_id").swipe([0.0183, -0.0729])
sleep(1.0)
poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(1.0)
poco("转到上一层级").click()

#返回“家用”主页面
swipe([1070,500],[10,500])
swipe([210,500],[10,500])
swipe([1070,500],[10,500])
swipe([210,500],[10,500])
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dashboard_places_container").child("com.philips.ph.homecare:id/dashboard_place_container")[0].offspring("com.philips.ph.homecare:id/dashboard_place_level_color").swipe([0.8672, -0.0103])
sleep(1.0)

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dashboard_places_container").child("com.philips.ph.homecare:id/dashboard_place_container")[0].offspring("com.philips.ph.homecare:id/dashboard_place_level_color").swipe([0.6162, -0.0164])
sleep(1.0)

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dashboard_places_container").child("com.philips.ph.homecare:id/dashboard_place_container")[0].offspring("com.philips.ph.homecare:id/dashboard_place_level_color").swipe([-0.6116, 0.0175])
sleep(1.0)

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dashboard_places_container").child("com.philips.ph.homecare:id/dashboard_place_container")[0].offspring("com.philips.ph.homecare:id/dashboard_place_level_color").swipe([-0.7325, 0.0349])
sleep(1.0)

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dashboard_places_container").child("com.philips.ph.homecare:id/dashboard_place_container")[1].offspring("com.philips.ph.homecare:id/dashboard_place_level_color").swipe([-0.6709, 0.0216])
sleep(1.0)

#在编辑位置删除一个位置
poco(text="管理位置").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/menu_edit_id").click()
sleep(1.0)

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/fragment_container_id").offspring("com.philips.ph.homecare:id/places_edit_list_id").child("android.widget.LinearLayout")[2].offspring("com.philips.ph.homecare:id/places_edit_trash_id").click()
sleep(1.0)

poco("com.philips.ph.homecare:id/places_edit_delete_id").click()
sleep(1.0)

poco("com.philips.ph.homecare:id/menu_done_id").click()
sleep(1.0)

poco("转到上一层级").click()
poco(text="当前地点").swipe([0.8968, -0.0216])
sleep(1.0)

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dashboard_places_container").child("com.philips.ph.homecare:id/dashboard_place_container")[0].offspring("com.philips.ph.homecare:id/dashboard_place_level_color").swipe([0.5431, -0.0031])


#设置页面UI验证
poco("com.philips.ph.homecare:id/navigation_settings").click()
poco("com.philips.ph.homecare:id/settings_support_id").click()
sleep(1.0)
#支持中的设备使用和过滤网维护页面
poco("com.philips.ph.homecare:id/support_maintenance_id").click()
sleep(3.0)
poco(text="产品信息").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/find_product_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/uid_search_decoy_hint_text").click()
text("8000")
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.philips.ph.homecare:id/productListView").child("com.philips.ph.homecare:id/productselection_ratingtheme")[0].click()
sleep(1.0)
poco("com.philips.ph.homecare:id/detailedscreen_select_button").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/savedscreen_button_continue").click()
sleep(1.0)

poco("com.android.systemui:id/back").click()
sleep(1.0)

#连接和“”
poco("com.philips.ph.homecare:id/support_asked_id").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/support_faq_id").click()
sleep(2.0)
poco("com.android.systemui:id/back").click()
poco("转到上一层级").click()
sleep(1.0)

#通知
poco("com.philips.ph.homecare:id/settings_notification_id").click()
sleep(1.0)
#反复开关
poco("com.android.settings:id/switch_widget").click()
poco("com.android.settings:id/switch_widget").click()
poco("com.android.settings:id/switchWidget").click()
poco("com.android.settings:id/switchWidget").click()
poco("android:id/switch_widget").click()
poco("android:id/switch_widget").click()
poco("com.android.systemui:id/back").click()
sleep(1.0)


#显示设置
poco("com.philips.ph.homecare:id/settings_display_id").click()
sleep(1.0)

poco("com.philips.ph.homecare:id/display_weather_switch").click()
poco("com.philips.ph.homecare:id/display_weather_switch").click()
poco("com.philips.ph.homecare:id/display_unit_imperial_btn").click()
poco("com.philips.ph.homecare:id/display_unit_metric_btn").click()
poco("com.philips.ph.homecare:id/display_language").click()
sleep(1.0)

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[1].child("android.widget.RadioButton").click()
sleep(1.0)

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/language_list_id").child("android.widget.LinearLayout")[2].child("android.widget.RadioButton").click()
sleep(1.0)

poco("com.android.systemui:id/back").click()
sleep(1.0)
poco("com.android.systemui:id/back").click()

#管理同意

poco("com.philips.ph.homecare:id/settings_consent_id").click()
sleep(1.0)

poco("com.philips.ph.homecare:id/consent_cookie_switch").click()
sleep(1.0)

poco("android:id/button1").click()
sleep(1.0)

poco("com.philips.ph.homecare:id/consent_cookie_switch").click()
sleep(1.0)
poco("com.android.systemui:id/back").click()

#应用权限poco("com.android.systemui:id/back").click()

poco("com.philips.ph.homecare:id/settings_permissions_id").click()
sleep(1.0)
#关于poco("com.android.systemui:id/back").click()

poco("com.philips.ph.homecare:id/settings_about_id").click()




#文章button视后期需要，前期沟通是可能会变。




