# -*- encoding=utf8 -*-
__author__ = "xfdzl"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.proxy import UIObjectProxy
auto_setup(__file__)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
element=UIObjectProxy(poco=poco,name='com.philips.ph.homecare:id/policy_dialog_check',)
element=UIObjectProxy(poco=poco,name='com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon_container')
#element=UIObjectProxy(poco=poco,name='com.philips.ph.homecare:id/policy_dialog_check')
element=UIObjectProxy(poco=poco,name='com.philips.ph.homecare:id/navigation_settings')
#lement=UIObjectProxy(poco=poco,name='com.philips.ph.homecare:id/policy_dialog_check')


res = element.exists()
print(res)
if res:
    element.click()
        

#登录之前要重置app的数据
#登录初始化后的app
time.sleep(2.0)

touch(Template(r"tpl1715405031457.png", record_pos=(-0.351, -0.02), resolution=(1080, 2400)))

sleep(2.0)


touch(Template(r"tpl1715413987760.png", record_pos=(-0.348, -0.048), resolution=(1080, 2400)))
#poco("com.philips.ph.homecare:id/policy_dialog_message").click('隐私政策')
sleep(2.0)

poco("转到上一层级").click()
sleep(1.0)
touch(Template(r"tpl1715414019257.png", record_pos=(-0.154, -0.039), resolution=(1080, 2400)))

#poco("com.philips.ph.homecare:id/policy_dialog_message").click()
sleep(2.0)
poco("转到上一层级").click()
sleep(1.0)


poco("com.philips.ph.homecare:id/policy_dialog_check").click()
sleep(1.0)

poco("android:id/button1").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/main_coordinator_id").swipe([-0.7348, 0.0329])
sleep(1.0)
poco("com.philips.ph.homecare:id/main_coordinator_id").swipe([-0.8786, 0.0339])
sleep(1.0)
poco("com.philips.ph.homecare:id/welcome_enter_app_btn").click()
sleep(1.0)
#同意页面详情场景
poco("com.philips.ph.homecare:id/consent_link_btn").click()
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

#poco("com.philips.ph.homecare:id/navigation_settings").click()
#sleep(1.0)
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
poco("android.widget.ScrollView").click()
sleep(1.0)
poco("android:id/button1").click()
sleep(1.0)

#重启app
poco(zOrders="{'global': 0, 'local': 9}").click()
sleep(100.0)

#不共享位置，再次确认获取位置权限
#拒绝



#允许获取位置信息

poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
sleep(2.0)

poco("com.philips.ph.homecare:id/dashboard_place_level_color").swipe([-1, 0.0411])
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
sleep(1.0)
poco("com.philips.ph.homecare:id/places_recyclerView_id").click()
sleep(1.0)

poco("com.philips.ph.homecare:id/places_recyclerView_id").click()
sleep(1.0)
poco("转到上一层级").click()

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dashboard_places_container").child("com.philips.ph.homecare:id/dashboard_place_container")[1].child("android.view.ViewGroup").swipe([-0.8261, 0.0329])
sleep(1.0)
poco("com.philips.ph.homecare:id/dashboard_footer_btn").click()
sleep(1.0)
poco("转到上一层级").swipe([0.0114, 0.0])
sleep(1.0)
poco(text="当前地点").swipe([0.7599, -0.0298])
sleep(1.0)
poco("转到上一层级").click()
sleep(1.0)
#wea详情
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/dashboard_places_container").child("com.philips.ph.homecare:id/dashboard_place_container")[1].offspring("com.philips.ph.homecare:id/dashboard_place_level_color").click()
sleep(3.0)

poco("info").click()
sleep(1.0)
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/web_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[1].child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[0].child("android.widget.TextView")[1].click()
sleep(1.0)

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/web_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[1].child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").click()
sleep(1.0)

poco(text="/11").click()
sleep(1.0)

poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/web_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[1].child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/web_layout_id").swipe([0.0137, -0.7651])
sleep(1.0)

poco(text="每天").click()
sleep(3.0)

#页面有问题，可以查询到返回建，返回
poco("转到上一层级").click()
sleep(1.0)
poco("转到上一层级").click()




#已经点对点之后的设备控制
poco("com.philips.ph.homecare:id/dashboard_control_power_btn").click()
sleep(3.0)
poco("com.philips.ph.homecare:id/dashboard_control_power_btn").click()
sleep(3.0)
poco("com.philips.ph.homecare:id/dashboard_control_power_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/dashboard_control_auto_btn").click()
sleep(1.0)
#自动风量
poco("com.philips.ph.homecare:id/dashboard_control_auto_btn").click()
sleep(1.0)

#中等风量
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.philips.ph.homecare:id/philips_control_sheet_list").child("android.widget.LinearLayout")[2]
sleep(1.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(2.0)

#灯光调整
poco("com.philips.ph.homecare:id/dashboard_control_light_brightness_btn").click()
sleep(1.0)

poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.philips.ph.homecare:id/philips_control_sheet_list").child("android.widget.LinearLayout")[1]

#poco("androidx.appcompat.widget.LinearLayoutCompat")ng("com.philips.ph.homecare:id/philips_control_sheet_list").child("android.widget.LinearLayout")[1]
sleep(1.0)

poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1.0)

#关闭灯光
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.philips.ph.homecare:id/philips_control_sheet_list").child("android.widget.LinearLayout")[2]
sleep(1.0)

poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(1.0)

#设备详情页面
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android.view.ViewGroup").click()
sleep(1.0)

#反复验证页面打开功能
poco("转到上一层级").click()
sleep(1.0)
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android.view.ViewGroup").click()
sleep(1.0)


poco("转到上一层级").click()
sleep(1.0)
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android.view.ViewGroup").click()
sleep(1.0)

poco("转到上一层级").click()
sleep(1.0)
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android.view.ViewGroup").click()
sleep(1.0)

#页面详情，


poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([0.1095, -0.3584])
sleep(1.0)
poco("com.philips.ph.homecare:id/purifier_control_scenario_more").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/schedule_calendar_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/menu_add_id").click()
sleep(1.0)
poco("转到上一层级").click()
sleep(1.0)
poco("转到上一层级").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/purifier_control_history").click()
sleep(1.0)
poco("android.widget.ScrollView").swipe([-0.0571, -0.3522])

sleep(1.0)
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
sleep(1.0)
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
poco("com.philips.ph.homecare:id/air_quality_left_btn").click()
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/air_quality_content_id").child("com.philips.ph.homecare:id/reading_item_container_id")[0].click()
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/air_quality_content_id").child("android.widget.FrameLayout")[0].child("com.philips.ph.homecare:id/trends_chart_view_id").click()
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("android:id/content").offspring("com.philips.ph.homecare:id/air_quality_content_id").child("com.philips.ph.homecare:id/reading_item_container_id")[0].swipe([0.0046, 0.5545])
sleep(1.0)

#周月年
poco("com.philips.ph.homecare:id/air_quality_week_btn").click()
sleep(1.0)

poco("com.philips.ph.homecare:id/air_quality_month_btn").click()
sleep(1.0)

poco("com.philips.ph.homecare:id/air_quality_year_btn").click()
sleep(1.0)

poco("转到上一层级").click()

#控制







#场景二，共享位置




