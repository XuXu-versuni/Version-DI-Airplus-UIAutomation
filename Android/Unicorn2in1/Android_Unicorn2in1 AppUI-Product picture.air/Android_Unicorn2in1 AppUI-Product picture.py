# -*- encoding=utf8 -*-
__author__ = "Mengjie"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
#poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

# 本shell对应的测试用例：
# https://nutriu.atlassian.net/browse/CH-57 (AppUI-Product picture)

#启动Air+ app
start_app("com.philips.ph.homecare")
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")
sleep(3.0)
# https://nutriu.atlassian.net/browse/CH-57
assert_exists(Template(r"tpl1736402013666.png", threshold=0.98, record_pos=(-0.296, 0.142), resolution=(1080, 2412)), "检查产品图片")
# 进入设备控制页面
poco(desc="https://air-matters.com/app/philips/dark_mode/AC3420_10.png").click()
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([-0.2243, -0.8636])
poco(text="Device Settings").click()
poco("android.widget.ScrollView").swipe([0.0779, -0.5874])
poco(text="Help & Support").click()
poco(text="My Philips Air Purifier does not remove odors properly").click()
poco("com.philips.ph.homecare:id/feedback_edit_id").click()
text("123")
poco(text="Send").click()
assert_equal(poco("com.google.android.gm:id/subject").get_text(),"AC3420/10 diagnostics","检查设备的model id")
# 返回到app主页
poco(desc="转到上一层级").click()
poco(desc="返回").click()
start_app("com.philips.ph.homecare")
poco(text="I have sent the email successfully").click()
poco(desc="返回").click()
poco(desc="返回").click()














