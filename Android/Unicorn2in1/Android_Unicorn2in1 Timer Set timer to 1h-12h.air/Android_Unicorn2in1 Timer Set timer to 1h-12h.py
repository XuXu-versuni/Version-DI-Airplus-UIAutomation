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
# https://nutriu.atlassian.net/browse/CH-1595 (Timer - Set timer to 1h-12h)

#启动Air+ app
start_app("com.philips.ph.homecare")
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")
# 进入设备控制页面
poco(desc="https://air-matters.com/app/philips/dark_mode/AC3420_10.png").click()
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([-0.0213, -0.6634])

# https://nutriu.atlassian.net/browse/CH-1595 
# timer设置为1
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.0396, -0.0354])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735873358792.png", threshold = 0.98, record_pos=(0.209, 0.481), resolution=(1080, 2412)), "timer设置为1h")
# timer重置为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.0091, 0.0286])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735873476333.png", threshold = 0.98, record_pos=(0.218, 0.48), resolution=(1080, 2412)), "timer设置为off")
sleep(3.0)
# timer设置为2h
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.0213, -0.0572])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735876073351.png", threshold = 0.98, record_pos=(0.215, -0.001), resolution=(1080, 2412)), "timer设置为2h")
# timer重置为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.0152, 0.0627])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735873476333.png", threshold = 0.98, record_pos=(0.218, 0.48), resolution=(1080, 2412)), "timer设置为off")
# timer设置为3h
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735876214229.png", record_pos=(0.2, 0.468), resolution=(1080, 2412)), vector=[-0.0243, -0.0804])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735876264655.png", threshold = 0.98, record_pos=(0.222, 0.003), resolution=(1080, 2412)), "timer设置为3h")
# timer重置为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735876387623.png", record_pos=(0.242, 0.265), resolution=(1080, 2412)), vector=[-0.0183, 0.0885])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735873476333.png", threshold = 0.98, record_pos=(0.218, 0.48), resolution=(1080, 2412)), "timer设置为off")
# timer设置为4h
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735876627144.png", record_pos=(0.248, 0.462), resolution=(1080, 2412)), vector=[-0.0122, -0.1267])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735878309993.png", threshold = 0.98, record_pos=(0.213, -0.001), resolution=(1080, 2412)), "timer设置为4h")

# timer重置为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735876719598.png", record_pos=(0.154, 0.262), resolution=(1080, 2412)), vector=[0.0183, 0.1172])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735873476333.png", threshold = 0.98, record_pos=(0.218, 0.48), resolution=(1080, 2412)), "timer设置为off")
# timer设置为5h
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735878453505.png", record_pos=(0.177, 0.443), resolution=(1080, 2412)), vector=[0.0282, -0.1439])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735878576397.png", threshold = 0.98, record_pos=(0.221, 0.0), resolution=(1080, 2412)), "timer设置为5h")

# timer重置为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735878521472.png", record_pos=(0.163, 0.231), resolution=(1080, 2412)), vector=[-0.0226, 0.149])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735873476333.png", threshold = 0.98, record_pos=(0.218, 0.48), resolution=(1080, 2412)), "timer设置为off")
# timer设置为6h
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735878911117.png", record_pos=(0.163, 0.462), resolution=(1080, 2412)), vector=[0.0085, -0.1578])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735878839086.png", threshold = 0.98, record_pos=(0.219, 0.007), resolution=(1080, 2412)), "timer设置为6h")
# timer重置为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735878857229.png", record_pos=(0.239, 0.327), resolution=(1080, 2412)), vector=[-0.0846, 0.1767])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735873476333.png", threshold = 0.98, record_pos=(0.218, 0.48), resolution=(1080, 2412)), "timer设置为off")
# timer设置为7h
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735882634425.png", record_pos=(0.098, 0.409), resolution=(1080, 2412)), vector=[0.031, -0.1906])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735882177888.png", threshold = 0.98, record_pos=(0.208, -0.001), resolution=(1080, 2412)), "timer设置为7h")

# timer重置为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735882199374.png", record_pos=(0.174, 0.29), resolution=(1080, 2412)), vector=[0.062, 0.2058])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735873476333.png", threshold = 0.98, record_pos=(0.218, 0.48), resolution=(1080, 2412)), "timer设置为off")
# timer设置为8h
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735882923025.png", record_pos=(0.168, 0.482), resolution=(1080, 2412)), vector=[-0.0028, -0.2235])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735882834921.png", threshold = 0.98, record_pos=(0.217, 0.005), resolution=(1080, 2412)), "timer设置为8h")
# timer重置为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735882857537.png", record_pos=(0.301, 0.217), resolution=(1080, 2412)), vector=[-0.0395, 0.2588])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735873476333.png", threshold = 0.98, record_pos=(0.218, 0.48), resolution=(1080, 2412)), "timer设置为off")
# timer设置为9h
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735883051923.png", record_pos=(0.129, 0.527), resolution=(1080, 2412)), vector=[0.0338, -0.2512])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735883070091.png", threshold = 0.98, record_pos=(0.208, -0.001), resolution=(1080, 2412)), "timer设置为9h")
# timer重置为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735883184723.png", record_pos=(0.219, 0.237), resolution=(1080, 2412)), vector=[-0.2002, 0.2689])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735873476333.png", threshold = 0.98, record_pos=(0.218, 0.48), resolution=(1080, 2412)), "timer设置为off")
# timer设置为10h
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735883374176.png", record_pos=(-0.032, 0.519), resolution=(1080, 2412)), vector=[-0.0959, -0.2929])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735883292665.png", threshold = 0.98, record_pos=(0.219, 0.001), resolution=(1080, 2412)), "timer设置为10h")

# timer重置为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735883455121.png", record_pos=(-0.032, 0.265), resolution=(1080, 2412)), vector=[-0.0226, 0.2853])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735873476333.png", threshold = 0.98, record_pos=(0.218, 0.48), resolution=(1080, 2412)), "timer设置为off")
# timer设置为11h
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735883579198.png", record_pos=(-0.024, 0.524), resolution=(1080, 2412)), vector=[-0.0282, -0.308])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735883596634.png", threshold = 0.98, record_pos=(0.199, 0.007), resolution=(1080, 2412)), "timer设置为11h")
# timer重置为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735883620690.png", record_pos=(0.005, 0.206), resolution=(1080, 2412)), vector=[-0.0169, 0.3118])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735873476333.png", threshold = 0.98, record_pos=(0.218, 0.48), resolution=(1080, 2412)), "timer设置为off")
# timer设置为12h
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735883954186.png", record_pos=(0.047, 0.513), resolution=(1080, 2412)), vector=[0.0648, -0.3699])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735883977467.png", threshold = 0.98, record_pos=(0.224, 0.01), resolution=(1080, 2412)), "timer设置为12h")
# timer重置为off
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
swipe(Template(r"tpl1735884013191.png", record_pos=(-0.066, 0.132), resolution=(1080, 2412)), vector=[0.0451, 0.3333])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
sleep(3.0)
assert_exists(Template(r"tpl1735873476333.png", threshold = 0.98, record_pos=(0.218, 0.48), resolution=(1080, 2412)), "timer设置为off")
# 返回到app主页
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([0.0213, 0.6634])
poco(desc="Navigate up").click()

