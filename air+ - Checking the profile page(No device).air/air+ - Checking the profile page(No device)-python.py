# -*- encoding=utf8 -*-
__author__ = "Mengjie"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import logging

# 初始化日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

# 常量定义
DEVICE_DESC = "https://air-matters.com/app/philips/dark_mode/AMF870_15.png"
DEVICE_TEXT = "mengjie"
APP_PACKAGE = "com.philips.ph.homecare"

# 进入控制页面
# 进入控制页面
def enter_control_page():
    """
    该函数用于进入设备的控制页面。
    它首先记录了进入控制页面的意图，然后尝试找到指定的设备节点。
    如果设备节点不存在，则记录错误并抛出异常。
    最后，如果找到设备节点，则点击它以进入控制页面。
    """
    # 记录进入控制页面的操作
    logger.info("Entering control page...")
    
    # 根据设备的描述和文本寻找设备节点
    device_node = poco(desc=DEVICE_DESC, text=DEVICE_TEXT)
    
    # 检查设备节点是否存在
    if not device_node.exists():
        # 如果设备节点不存在，记录错误并抛出异常
        logger.error("Device with desc '{}' and text '{}' not found.".format(DEVICE_DESC, DEVICE_TEXT))
        raise Exception("Device with desc '{}' and text '{}' not found.".format(DEVICE_DESC, DEVICE_TEXT))
    
    # 如果设备节点存在，则点击它以进入控制页面
    device_node.click()


# 检查当前页面是否为主页
# 检查当前页面是否为主页
def check_home_page():
    """
    此函数用于检查当前应用页面是否为主页。
    通过断言主页的特定元素是否存在来验证。
    """
    logger.info("Checking home page...")
    # 断言主页的特定图像元素存在，以确认页面为主页且未连接设备
    assert_exists(Template(r"tpl1725355176952.png", record_pos=(-0.009, -0.356), resolution=(1080, 2340)), "app在主页并且未连接设备")

# 检查app settings是否更改为profile
def check_profile_text():
    """
    检查应用设置是否已更改为Profile。
    此函数通过断言应用界面上的一个标签的文本是否为"Profile"来实现。
    如果文本与预期不符，将抛出断言错误。
    """
    # 记录检查Profile文字的日志信息
    logger.info("Checking profile text...")
    # 断言导航栏标签的文本是否为"Profile"，如果不符将抛出断言错误
    assert_equal(poco("com.philips.ph.homecare:id/navigation_bar_item_small_label_view").get_text(), "Profile", "检查Profile文字")


# 点击Profile进入app profile页面
def click_profile():
    """
    This function clicks the Profile button to enter the app's profile page.
    There are no parameters for this function.
    """
    # Log the action of clicking Profile
    logger.info("Clicking Profile...")
    # Perform the click action at the specified coordinates
    touch((529, 2108))

# 检查app设置页面是否正确显示Profile文字
def check_profile_page():
    """
    此函数用于验证在app的设置页面中是否显示了正确的文字'Profile'。
    它通过日志记录和断言来确保页面的正确性。
    """
    # 记录检查profile页面的日志
    logger.info("Checking profile page...")
    # 断言app设置页面上的TextView组件显示的文字为'Profile'
    # 这是为了确保页面加载正确且显示符合预期
    assert_equal(poco("android.widget.TextView").get_text(), "Profile", "app设置页面显示Profile文字")

# 检查Guest文字显示
def check_guest_text():
    logger.info("Checking guest text...")
    assert_equal(poco("com.philips.ph.homecare:id/settings_account_name").get_text(), "Guest", "检查app设置页面显示Guest文字")

# 点击Guest进入OneID登录页面
def click_guest():
    logger.info("Clicking Guest...")
    touch(Template(r"tpl1725357731410.png", record_pos=(0.056, -0.726), resolution=(1080, 2340)))

# 检查是否进入OneID登录页面
def check_oneid_login_page():
    logger.info("Checking OneID login page...")
    assert_exists(Template(r"tpl1725357780597.png", record_pos=(0.01, -0.389), resolution=(1080, 2340)), "已进入OneID登录页面")

# 返回上一层进入app设置页面
def back_to_profile():
    logger.info("Returning to profile page...")
    touch((833, 2260))

# 点击添加设备按钮进入配网流程页面
def click_add_device():
    logger.info("Clicking add device button...")
    touch((537, 600))

# 检查是否进入配网流程页面
def check_setup_page():
    logger.info("Checking setup page...")
    assert_exists(Template(r"tpl1725359531946.png", record_pos=(-0.006, -0.026), resolution=(1080, 2340)), "进入配网流程页面")

# 在配网流程页面点击左上角返回按钮，返回app设置页面
def back_to_profile_from_setup():
    logger.info("Returning to profile page from setup...")
    touch((61, 163))

# 点击display功能，进入display页面
def click_display():
    logger.info("Clicking display...")
    poco("com.philips.ph.homecare:id/settings_display_id").click()

# 关闭主页天气显示
def turn_off_weather():
    logger.info("Turning off weather...")
    poco("com.philips.ph.homecare:id/display_weather_switch").click()

# 去app主页检查天气卡片已关闭
def check_weather_card_removed():
    logger.info("Checking weather card removed...")
    poco("Navigate up").click()
    poco(text="Home").click()
    assert_not_exists(Template(r"tpl1725360934942.png", record_pos=(0.0, -0.563), resolution=(1080, 2340)), "天气卡片不存在")

# 打开主页天气显示
def turn_on_weather():
    """
    此函数用于在应用的设置界面打开天气显示功能
    它通过模拟用户交互，点击相应的界面元素来实现
    """
    logger.info("Turning on weather...")
    # 进入设置界面
    poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/navigation_settings").offspring("com.philips.ph.homecare:id/navigation_bar_item_icon_view").click()
    # 点击显示设置项
    poco("com.philips.ph.homecare:id/settings_display_id").click()
    # 打开天气显示开关
    poco("com.philips.ph.homecare:id/display_weather_switch").click()

# 去app主页检查天气卡片已显示
def check_weather_card_shown():
    logger.info("Checking weather card shown...")
    poco("Navigate up").click()
    poco(text="Home").click()
    assert_exists(Template(r"tpl1725361322936.png", record_pos=(-0.003, -0.559), resolution=(1080, 2340)), "天气卡片已存在")

# 点击定位功能
def click_locations():
    logger.info("Clicking locations...")
    poco(text="Locations").click()

# 检查是否进入定位页面
def check_locations_page():
    logger.info("Checking locations page...")
    assert_exists(Template(r"tpl1730356394331.png", record_pos=(0.003, -0.708), resolution=(1080, 2340), threshold=0.98), "推送通知状态显示enable")

# 打开允许通知按钮
def enable_notifications():
    logger.info("Enabling notifications...")
    poco("com.philips.ph.homecare:id/notification_app_id").click()
    poco("com.android.settings:id/switch_widget").click()
    assert_equal(poco("com.android.settings:id/switch_widget").attr("checked"), True, "已打开app通知")

# 返回到app profile 页面
def back_to_profile_from_notifications():
    logger.info("Returning to profile page from notifications...")
    poco("Navigate up").click()

# 检查app profile页面
def check_profile_page_after_return():
    logger.info("Checking profile page after return...")
    assert_equal(poco("android.widget.TextView").get_text(), "Profile", "进入app设置页面")

# 检查app profile页面support功能
def check_support_page():
    logger.info("Checking support page...")
    poco("com.philips.ph.homecare:id/settings_support_id").click()
    assert_equal(poco("android.widget.TextView").get_text(), "Support", "进入app support页面")

# 点击FAQ按钮
def click_faq():
    logger.info("Clicking FAQ...")
    poco("com.philips.ph.homecare:id/support_faq_id").click()
    assert_exists(Template(r"tpl1730358329247.png", record_pos=(-0.292, -0.827), resolution=(1080, 2340)), "当前已进入FAQ页面")

# 返回到support页面
def back_to_support_from_faq():
    logger.info("Returning to support page from FAQ...")
    poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
    assert_equal(poco("android.widget.TextView").get_text(), "Support", "进入app support页面")

# 点击访问官网按钮
def click_website():
    """
    该函数通过模拟用户点击操作，访问应用程序的官方支持页面。
    首先，它记录了点击操作的开始。
    然后,使用poco库找到具有特定ID的元素并执行点击操作。
    等待3秒,以确保页面有足够的时间加载。
    最后,断言浏览器URL栏中的文本与预期的URL相匹配,以确认正确加载了目标页面。
    """
    logger.info("点击网站...")
    poco("com.philips.ph.homecare:id/support_website_id").click()
    sleep(3)
    assert_equal(poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_url_bar_text").get_text(), "https://www.philips.co.uk/c-w/support-home.html", "进入app support页面")

# 返回到support页面
def back_to_support_from_website():
    logger.info("Returning to support page from website...")
    poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
    poco("Navigate up").click()
    assert_equal(poco("android.widget.TextView").get_text(), "Profile", "进入app设置页面")

# 检查app profile页面About功能
def check_about_page():
    logger.info("Checking about page...")
    poco("com.philips.ph.homecare:id/settings_about_id").click()
    assert_equal(poco("android.widget.TextView").get_text(), "About", "进入app about页面")
# 检查app profile页面关于页面内容,这里仅做示例，实际应用中需要根据实际情况进行修改。
def check_about_page_content():
    logger.info("检查app页面~~")
    poco("com.philips.ph.homecare:id/settings_about_id").click()
    assert_exists(Template(r"tpl1730360578375.png", record_pos=(-0.003, -0.708), resolution=(1080, 2340), threshold=0.98), "app页面已显示")


# 点击网站按钮
def click_about_website():
    logger.info("Clicking about website...")
    poco("com.philips.ph.homecare:id/about_website_id").click()
    sleep(5)
    assert_exists(Template(r"tpl1730359785748.png", record_pos=(-0.204, -0.966), resolution=(1080, 2340), threshold=0.98), "当前已进入philips网站")

# 返回到about页面
def back_to_about_from_website():
    logger.info("Returning to about page from website...")
    poco("com.sec.android.app.sbrowser:id/custom_tab_toolbar_close_icon").click()
    assert_equal(poco("android.widget.TextView").get_text(), "About", "进入app about页面")

# 点击terms of use 按钮
def click_terms_of_use():
    logger.info("Clicking terms of use...")
    poco("com.philips.ph.homecare:id/about_terms_id").click()
    assert_equal(poco("android.widget.TextView").get_text(), "Terms & Conditions", "进入terms页面")

# 返回到about页面
def back_to_about_from_terms():
    """
    从terms页面返回到about页面。
    这个函数通过模拟用户点击导航返回按钮来实现页面跳转。
    """
    logger.info("Returning to about page from terms...")
    poco("Navigate up").click()

    
def main():
    try:
        # 启动Air+ app
        start_app(APP_PACKAGE)
        
        # 检查当前页是否在主页
        check_home_page()
        
        # 检查app settings更改为profile
        check_profile_text()
        
        # 点击Porfile进入app profile页面
        click_profile()
        
        # 检查app设置页面显示profile文字
        check_profile_page()
        
        # 检查Guest文字显示
        check_guest_text()
        
        # 点击Guest进入Oneid登录页面
        click_guest()
        
        # 检查是否进入OneID登录页面
        check_oneid_login_page()
        
        # 返回上一层进入app设置页面
        back_to_profile()
        
        # 点击添加设备按钮进入配网流程页面
        click_add_device()
        
        # 检查是否进入配网流程页面
        check_setup_page()
        
        # 在配网流程页面点击左上角返回按钮，返回app设置页面
        back_to_profile_from_setup()
        
        # 点击display功能，进入display页面
        click_display()
        
        # 关闭主页天气显示
        turn_off_weather()
        
        # 去app主页检查天气卡片已关闭
        check_weather_card_removed()
        
        # 打开主页天气显示
        turn_on_weather()
        
        # 去app主页检查天气卡片已显示
        check_weather_card_shown()
        
        # 点击定位功能
        click_locations()
        
        # 检查是否进入定位页面
        check_locations_page()
        
        # 打开允许通知按钮
        enable_notifications()
        
        # 返回到app profile 页面
        back_to_profile_from_notifications()
        
        # 检查app profile页面
        check_profile_page_after_return()
        
        # 检查app profile页面support功能
        check_support_page()
        
        # 点击FAQ按钮
        click_faq()
        
        # 返回到support页面
        back_to_support_from_faq()
        
        # 点击访问官网按钮
        click_website()
        
        # 返回到support页面
        back_to_support_from_website()
        
        # 检查app profile页面About功能
        check_about_page()
        
        # 点击网站按钮
        click_about_website()
        
        # 返回到about页面
        back_to_about_from_website()
        
        # 点击terms of use 按钮
        click_terms_of_use()
        
        # 返回到about页面
        back_to_about_from_terms()

    except Exception as e:
        logger.error("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
