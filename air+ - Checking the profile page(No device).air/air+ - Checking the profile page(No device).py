# -*- encoding=utf8 -*-
__author__ = "ytian1"

from airtest.core.api import *
from airtest.core.api import using
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
# element = UIObjectProxy(poco = poco,name = "com.philips.ph.homecare:id/display_theme_auto")
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

"""本shell 对应 测试用例：
    尚需补充到jira中（20241105）

例子：下列XXX到YYY行对应 测试用例：https://nutriu.atlassian.net/browse/CH-50
"""


#前置条件：已安装Air+ app，打开app默认同意所有权限，未连接设备
#设备信息：Samsung S22 Android 14


#启动Air+ app
start_app("com.philips.ph.homecare")
#检查当前页是否在主页
assert_exists(Template(r"tpl1725355176952.png", record_pos=(-0.009, -0.356), resolution=(1080, 2340)), "app在主页并且未连接设备")

#检查app settings更改为profile
assert_equal(poco("com.philips.ph.homecare:id/navigation_bar_item_small_label_view").get_text(), "Profile", "检查Profile文字")

#点击Porfile进入app profile页面
touch((529,2108))
#在app设置页面检查profile文字
assert_equal(poco("android.widget.TextView").get_text(), "Profile","app设置页面显示Profile文字")
#检查Guest文字显示
assert_equal(poco("com.philips.ph.homecare:id/settings_account_name").get_text(), "Guest","检查app设置页面显示Guest文字")

#点击Guest进入Oneid登录页面
touch(Template(r"tpl1725357731410.png", record_pos=(0.056, -0.726), resolution=(1080, 2340)))
#检查是否进入OneID登录页面
assert_exists(Template(r"tpl1725357780597.png", record_pos=(0.01, -0.389), resolution=(1080, 2340)), "已进入OneID登录页面")

#返回上一层进入app设置页面
touch((833,2260))
#点击添加设备按钮进入配网流程页面
touch((537,600))
#检查是否进入配网流程页面
assert_exists(Template(r"tpl1725359531946.png", record_pos=(-0.006, -0.026), resolution=(1080, 2340)), "进入配网流程页面")
#在配网流程页面点击左上角返回按钮，返回app设置页面
touch((61,163))

#点击display功能，进入display页面
poco("com.philips.ph.homecare:id/settings_display_id").click()
#关闭主页天气显示
poco("com.philips.ph.homecare:id/display_weather_switch").click()
#去app主页检查天气卡片已关闭
poco("Navigate up").click()
poco(text="Home").click()
assert_not_exists(Template(r"tpl1725360934942.png", record_pos=(0.0, -0.563), resolution=(1080, 2340)), "天气卡片不存在")

#去app设置页面显示功能中,打开天气卡片在app主页显示
poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/navigation_settings").offspring("com.philips.ph.homecare:id/navigation_bar_item_icon_view").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
poco("com.philips.ph.homecare:id/display_weather_switch").click()

#去app主页检查天气卡片已显示
poco("Navigate up").click()
poco(text="Home").click()
assert_exists(Template(r"tpl1725361322936.png", record_pos=(-0.003, -0.559), resolution=(1080, 2340)), "天气卡片已存在")

#去app设置进入显示功能页面
poco(text="Profile").click()
poco("com.philips.ph.homecare:id/settings_display_id").click()
#点击定位功能
poco(text="Locations").click()
#断言是否进入定位页面
assert_equal(poco("android.widget.TextView").get_text(), "Locations","进入定位页面")

#返回上一层，进入显示功能页面
poco("Navigate up").click()
#点击Imperial
poco(text="Imperial").click()
#返回app主页断言当地天气是否显示华摄氏度
poco("Navigate up").click()
poco(text="Home").click()
assert_exists(Template(r"tpl1725439093701.png", record_pos=(-0.094, -0.743), resolution=(1080, 2340)), "天气卡片温度显示华摄氏度")

#去app设置页面显示功能天气卡片单位选择Metric
poco(text="Profile").click()
poco(text="Display").click()
poco(text="Metric").click()

#去app主页断言天气卡片是否显示摄氏度
poco("Navigate up").click()
poco(text="Home").click()
# try：

# except
assert_exists(Template(r"tpl1725439594137.png", record_pos=(-0.089, -0.74), resolution=(1080, 2340)), "天气卡片温度显示摄氏度")

#去app设置页面选择显示按钮，进入显示页面
poco(text="Profile").click()
poco(text="Display").click()
#点击app显示页面light按钮
poco("com.philips.ph.homecare:id/display_theme_light").click()
assert_equal(poco("com.philips.ph.homecare:id/display_theme_light_btn").attr("checked"),True,msg="当前模式为Light")

#点击app显示页面Dark按钮
poco("com.philips.ph.homecare:id/display_theme_dark").click()
assert_equal(poco("com.philips.ph.homecare:id/display_theme_dark_btn").attr("checked"), True,"当前模式为Dark")
#点击app显示页面automatic按钮
poco("com.philips.ph.homecare:id/display_theme_auto").click()
assert_equal(poco("com.philips.ph.homecare:id/display_theme_auto_btn").attr("checked"),True,msg="当前模式为auto")
#点击语言按钮
poco("com.philips.ph.homecare:id/display_language").click()
#检查已进入语言页面
assert_exists(Template(r"tpl1725362519192.png", record_pos=(-0.002, -0.037), resolution=(1080, 2340)), "已进入语言列表页面")


# ST.PROJECT_ROOT = r"C:\Users\ytian1\OneDrive - Versuni\Desktop\Tool\1_shell\airtest1.3" 
# using("air+ - V1.3-shell\air+ change_language.air")
# using("air+ change_language.air")


# sys.path.append("C:\Users\ytian1\OneDrive - Versuni\Desktop\Tool\1_shell\airtest1.3\airtest1.3\air+ - V1.3-shell\air+ change_language.air")



#返回到app 设置页面并且断言是否进入app设置页面
poco("Navigate up").click()
sleep(2)
poco("Navigate up").click()
sleep(2)
assert_equal(poco("android.widget.TextView").get_text(), "Profile","进入app设置页面")

#点击manage consennt按钮
poco("com.philips.ph.homecare:id/settings_consent_id").click()
#断言是否进入manage consent页面
assert_equal(poco("android.widget.TextView").get_text(), "Manage consent","进入Manage consent页面")

#打开share analytics data 按钮
poco(text="Share Analytics Data").click()
sleep(1)
#断言分析数据按钮是打开的状态
assert_equal(poco("com.philips.ph.homecare:id/consent_cookie_switch").attr("checked"),True,msg = "分享数据分析按钮是打开的状态")

#关闭分享数据分析按钮
poco("com.philips.ph.homecare:id/consent_cookie_switch").click()
sleep(3)
poco("android:id/button1").click()
sleep(1)
#检查分析数据按钮仍然是关闭的状态
assert_equal(poco("com.philips.ph.homecare:id/consent_cookie_switch").attr("checked"),False,msg = "分享数据分析按钮是关闭的状态")

#打开分享分析数据按钮
poco("com.philips.ph.homecare:id/consent_cookie_switch").click()
sleep(1)
#检查分析数据按钮仍然是打开的状态
assert_equal(poco("com.philips.ph.homecare:id/consent_cookie_switch").attr("checked"),True,msg = "分享数据分析按钮是打开的状态")



#点击what does this mean按钮
touch(Template(r"tpl1725443004782.png", record_pos=(0.194, -0.499), resolution=(1080, 2340)))
#断言是否进入了what does this mean页面
assert_equal(poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_title_bar_text").get_text(),"What does this mean?",msg = "已进入what does this mean页面")

#返回到app profile 页面
poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
poco("com.android.systemui:id/back").click()
sleep(2)
#断言当前页面是否在app profile页面
assert_equal(poco("android.widget.TextView").get_text(), "Profile","进入app设置页面")

#检查System permission页面各个功能
#在app profile页面点击System permission按钮
poco("com.philips.ph.homecare:id/settings_permissions_id").click()
#断言当前页面是否在app系统权限页面
assert_equal(poco("android.widget.TextView").get_text(), "App info","已进入app系统权限页面")

#检查通知功能
#点击通知按钮进入通知页面
poco(text="Notifications").click()
assert_equal(poco("com.android.settings:id/switch_text").get_text(), "Allow notifications","已进入app通知页面")

#关闭app通知按钮
poco("com.android.settings:id/switch_widget").click()
assert_equal(poco("com.android.settings:id/switch_widget").attr("checked"), False,"当前已关闭通知权限")
assert_exists(Template(r"tpl1730192848648.png", record_pos=(-0.058, -0.37), resolution=(1080, 2340)), "当前已关闭app所有的通知")

#打开app通知按钮
poco("com.android.settings:id/switch_widget").click()
assert_equal(poco("com.android.settings:id/switch_widget").attr("checked"), True,"当前已打开通知权限")
#断言默认选中允许声音和震动
assert_equal(poco("com.android.settings:id/notification_radio_button").attr("checked"), True,"当前选中允许声音和震动")
#断言选中允许声音和震动后，通知类型有lock screen， badge， popup
assert_exists(Template(r"tpl1730271141022.png", record_pos=(0.0, 0.337), resolution=(1080, 2340), threshold = 0.98), "通知方式为允许声音和震动，通知类型有lock screen， badge， popup")


#通知方式选中silent
poco(text="Silent").click()
#断言当前选中的是静默通知
assert_exists(Template(r"tpl1730270428399.png", record_pos=(-0.272, -0.106), resolution=(1080, 2340), threshold = 0.98), "当前选中静默通知")
#断言选中静默后通知类型中，会缺少个pop up显示
assert_not_exists(Template(r"tpl1730270792919.png", record_pos=(0.3, 0.331), resolution=(1080, 2340)), "通知方式为静默，通知类型pop up方式不显示")

#断言默认锁屏通知为显示内容
assert_exists(Template(r"tpl1730271700286.png", record_pos=(-0.167, 0.66), resolution=(1080, 2340), threshold = 0.98), "当前锁屏通知为显示内容")
#切换锁屏通知为隐藏内容
poco("android:id/summary").click()
poco(text="Hide content").click()
#断言锁屏通知为隐藏内容
assert_exists(Template(r"tpl1730272122671.png", record_pos=(-0.169, 0.661), resolution=(1080, 2340), threshold = 0.98), "当前锁屏通知为隐藏内容")

#将通知页面所有功能恢复到默认
poco(text="Allow sound and vibration").click()
assert_equal(poco("com.android.settings:id/notification_radio_button").attr("checked"), True,"当前选中允许声音和震动")
poco("android:id/summary").click()
poco(text="Show content").click()
assert_exists(Template(r"tpl1730271700286.png", record_pos=(-0.167, 0.66), resolution=(1080, 2340), threshold = 0.98), "当前锁屏通知为显示内容")

#返回到app系统权限页面”App info“
poco("Navigate up").click()
assert_equal(poco("android.widget.TextView").get_text(), "App info","已进入app系统权限页面")

#检查权限功能页面
#在app系统权限页面点击权限按钮
poco(text="Permissions").click()
assert_exists(Template(r"tpl1730273232001.png", record_pos=(-0.028, -0.469), resolution=(1080, 2340)), "已进入app系统权限页面")

#返回到app系统权限页面”App info“
poco("Navigate up").click()
assert_equal(poco("android.widget.TextView").get_text(), "App info","已进入app系统权限页面")

#检查screen time功能页面
#在app系统权限页面点击screen time 按钮
poco(text="Screen time").click()
assert_equal(poco("com.samsung.android.forest:id/selected_day_textView").get_text(), "Today","已进入screen time页面")

#返回到app系统权限页面”App info“
poco("Navigate up").click()
assert_equal(poco("android.widget.TextView").get_text(), "App info","已进入app系统权限页面")

#在app系统权限页面检查移除权限按钮
#默认移除权限按钮是打开的状态、
assert_equal(poco("android:id/switch_widget").attr("checked"), True,"当前移除权限功能按钮是打开的状态")
#关闭移除权限按钮
poco("android:id/switch_widget").click()
assert_equal(poco("android:id/switch_widget").attr("checked"), False,"当前移除权限功能按钮是关闭的状态")
#恢复移除权限按钮默认状态
poco("android:id/switch_widget").click()
assert_equal(poco("android:id/switch_widget").attr("checked"), True,"当前移除权限功能按钮是打开的状态")

#在app系统权限页面检查设置默认功能
#点击设置默认按钮
poco(text="Set as default").click()
assert_equal(poco("android.widget.TextView").get_text(), "Set as default","已进入设置默认页面")
#关闭 打开支持链接按钮
poco("android:id/switch_widget").click()
assert_exists(Template(r"tpl1730277754618.png", record_pos=(0.011, -0.257), resolution=(1080, 2340), threshold = 0.98), "关闭 打开支持链接按钮")
#激活 打开支持链接按钮
poco("android:id/switch_widget").click()
assert_exists(Template(r"tpl1730277649887.png", record_pos=(0.016, -0.267), resolution=(1080, 2340), threshold = 0.98), "激活 打开支持链接按钮")

#点击支持web地址按钮
poco(text="Supported web addresses").click()
assert_equal(poco("android.widget.TextView").get_text(), "Supported web addresses","已进入支持web地址页面")
assert_exists(Template(r"tpl1730277919579.png", record_pos=(-0.178, -0.551), resolution=(1080, 2340)), "当前页面显示支持web地址链接")

#返回到app系统权限页面”App info“
poco("Navigate up").click()
poco("Navigate up").click()
assert_equal(poco("android.widget.TextView").get_text(), "App info","已进入app系统权限页面")

#滑动页面
swipe([717,1771],[717,771])
sleep(3)

#在app系统权限页面检查手机数据功能
#点击mobile data按钮
poco(text="Mobile data").click()
assert_equal(poco("android.widget.TextView").get_text(), "Application data usage","已进入app数据使用页面")
#返回到app系统权限页面”App info“
poco("Navigate up").click()
assert_equal(poco("android.widget.TextView").get_text(), "App info","已进入app系统权限页面")

#在app系统权限页面检查电池页面
#点击battery按钮
poco(text="Battery").click()
assert_equal(poco("android.widget.TextView").get_text(), "Battery","已进入battery页面")
#返回到app系统权限页面”App info“
poco("Navigate up").click()
assert_equal(poco("android.widget.TextView").get_text(), "App info","已进入app系统权限页面")

#在app系统权限页面检查存储页面
#点击storage按钮
poco(text="Storage").click()
assert_equal(poco("android.widget.TextView").get_text(), "Storage","已进入存储页面")
#返回到app系统权限页面”App info“
poco("Navigate up").click()
assert_equal(poco("android.widget.TextView").get_text(), "App info","已进入app系统权限页面")

#返回到app profile 页面
poco("Navigate up").click()
#断言当前页面是否在app profile页面
assert_equal(poco("android.widget.TextView").get_text(), "Profile","进入app设置页面")

#检查app profile页面通知管理功能
#在app profile页面点击通知管理按钮
poco("com.philips.ph.homecare:id/settings_notification_id").click()
assert_equal(poco("android.widget.TextView").get_text(), "Notification settings","已进入通知管理页面")
#点击推送通知按钮
poco("com.philips.ph.homecare:id/notification_app_id").click()
assert_equal(poco("android.widget.TextView").get_text(), "App notifications","已进入app通知页面")
#关闭允许通知按钮，检查推送通知按钮推送通知状态显示disable
poco("com.android.settings:id/switch_widget").click()
assert_equal(poco("com.android.settings:id/switch_widget").attr("checked"), False,"已进入app通知页面")
poco("Navigate up").click()
assert_exists(Template(r"tpl1730355689027.png", record_pos=(0.014, -0.729), resolution=(1080, 2340), threshold =0.98), "推送通知状态显示disable")
#打开允许通知按钮，检查推送通知按钮推送通知状态显示enable
poco("com.philips.ph.homecare:id/notification_app_id").click()
poco("com.android.settings:id/switch_widget").click()
assert_equal(poco("com.android.settings:id/switch_widget").attr("checked"), True,"已打开app通知")
poco("Navigate up").click()
assert_exists(Template(r"tpl1730356394331.png", record_pos=(0.003, -0.708), resolution=(1080, 2340), threshold =0.98), "推送通知状态显示enable")

#返回到app profile 页面
poco("Navigate up").click()
#断言当前页面是否在app profile页面
assert_equal(poco("android.widget.TextView").get_text(), "Profile","进入app设置页面")

#滑动页面
swipe([628,1539],[628,889])
sleep(3)

#检查app profile页面support功能
poco("com.philips.ph.homecare:id/settings_support_id").click()
assert_equal(poco("android.widget.TextView").get_text(), "Support","进入app support页面")
#点击FAQ按钮
poco("com.philips.ph.homecare:id/support_faq_id").click()
assert_exists(Template(r"tpl1730358329247.png", record_pos=(-0.292, -0.827), resolution=(1080, 2340)), "当前已进入FAQ页面")
#返回到support页面
poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
assert_equal(poco("android.widget.TextView").get_text(), "Support","进入app support页面")

#点击访问官网按钮
poco("com.philips.ph.homecare:id/support_website_id").click()
sleep(3)
assert_equal(poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_url_bar_text").get_text(), "https://www.philips.co.uk/c-w/support-home.html","进入app support页面")

#返回到support页面
poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
poco("Navigate up").click()
assert_equal(poco("android.widget.TextView").get_text(), "Profile","进入app设置页面")

#检查app profile页面About功能
poco("com.philips.ph.homecare:id/settings_about_id").click()
assert_equal(poco("android.widget.TextView").get_text(), "About","进入app about页面")

#点击网站按钮
poco("com.philips.ph.homecare:id/about_website_id").click()
sleep(5)
assert_exists(Template(r"tpl1730359785748.png", record_pos=(-0.204, -0.966), resolution=(1080, 2340),threshold = 0.98), "当前已进入philips网站")
#返回到about页面
poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
assert_equal(poco("android.widget.TextView").get_text(), "About","进入app about页面")

#点击terms of use 按钮
poco("com.philips.ph.homecare:id/about_terms_id").click()
assert_equal(poco("android.widget.TextView").get_text(), "Terms & Conditions","进入terms页面")
#返回到about页面
poco("Navigate up").click()
assert_equal(poco("android.widget.TextView").get_text(), "About","进入app about页面")

#点击privacy policy按钮
poco("com.philips.ph.homecare:id/about_privacy_id").click()
assert_equal(poco("android.widget.TextView").get_text(), "Privacy Policy","进入app  privacy policy页面")
#返回到about页面
poco("Navigate up").click()
assert_equal(poco("android.widget.TextView").get_text(), "About","进入app about页面")

#点击打开开源组件按钮
poco("com.philips.ph.homecare:id/about_open_source_id").click()
assert_equal(poco("android.widget.TextView").get_text(), "Open Source Components","进入app 开源组件页面")
#返回到about页面
poco("Navigate up").click()
assert_equal(poco("android.widget.TextView").get_text(), "About","进入app about页面")

#点击app邀评按钮
poco("com.philips.ph.homecare:id/about_review_app_id").click()
assert_equal(poco("com.philips.ph.homecare:id/enjoy_sheet_title").get_text(), "Enjoying the Air+ app?","弹出app邀评页面")
#返回到app主页
poco("com.android.systemui:id/back").click()
poco("com.android.systemui:id/back").click()
poco(text="Home").click()
sleep(3)
