# -*- encoding=utf8 -*-
__author__ = "Mengjie"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
#poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

# https://nutriu.atlassian.net/browse/CH-2808（Light control- Automatic/Bright/Low /off functionality）

#启动Air+ app
start_app("com.philips.ph.homecare")
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")
# 进入设备控制页面
poco(desc="https://air-matters.com/app/philips/dark_mode/AC3421_13.png").click()
sleep(2.0)
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([-0.0213, -0.6634])

# https://nutriu.atlassian.net/browse/CH-2808
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Automatic").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1736229293859.png", threshold = 0.98, record_pos=(-0.201, 0.255), resolution=(1080, 2412)), "灯光亮度显示为Automatic")
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Bright").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1736230345877.png", threshold = 0.98, record_pos=(-0.212, 0.253), resolution=(1080, 2412)), "灯光亮度显示为Bright")
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Low").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1736230458819.png", threshold = 0.98, record_pos=(-0.198, 0.245), resolution=(1080, 2412)), "灯光亮度显示为Low")
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Off").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1736231850571.png", threshold = 0.98, record_pos=(-0.195, 0.25), resolution=(1080, 2412)), "灯光亮度显示为off")
# 返回app主页
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([0.0213, 0.6634])
poco(desc="Navigate up").click()

