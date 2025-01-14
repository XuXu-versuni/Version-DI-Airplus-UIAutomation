# -*- encoding=utf8 -*-
__author__ = "Mengjie"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
#poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

# 开关按钮：打开状态；童锁按钮：关闭；模式按钮：Auto；湿度按钮：50%；Lamp modes：Air Quality；风速按钮：Auto；灯光亮度按钮：Automatic；Timer按钮：off（默认显示）

# 本shell对应的测试用例：
# https://nutriu.atlassian.net/browse/CH-53 (AppUI-Default Index and Working mode)（先做厂测，再检查默认显示）

#启动Air+ app
start_app("com.philips.ph.homecare")
sleep(2.0)
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")

# https://nutriu.atlassian.net/browse/CH-53
sleep(3.0)
# #如果需要，滑动页面到指定设备位置
# swipe(Template(r"tpl1736748556293.png", record_pos=(0.028, 0.125), resolution=(904, 2316)), vector=[0.0022, -0.1418])
# #这里的ui树中有多个dashboard_primary_reading_name这个元素名，以下的语句就会报错，找不到
assert_equal(poco("com.philips.ph.homecare:id/dashboard_primary_reading_name").get_text(),"PM2.5","指数默认显示PM2.5")


#xuxu改造,供多元素判断使用，多多复用
#
#
#
#
#
#
# # 获取所有匹配的元素
# elements = poco("com.philips.ph.homecare:id/dashboard_primary_reading_name")

# # 遍历所有元素并检查属性值
# for element in elements:
#     # 获取元素的 text 属性（可以是其他属性，比如 description 或其他）
#     text = element.attr("text")
#     if text == "PM2.5":
#         print("找到属性值为 PM2.5 的元素")
#         # 可以在这里添加断言，比如：
#         assert text == "PM2.5", "属性值匹配失败"
#         break
# else:
#     print("未找到属性值为 PM2.5 的元素")


# # 进入设备控制页面
# poco(desc="https://air-matters.com/app/philips/dark_mode/AC3420_10.png").click()
# poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([-0.0213, -0.6634])
# assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"),True,"设备默认是打开状态")
# assert_equal(poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").attr("checked"),False,"设备默认童锁是关闭状态")
# assert_exists(Template(r"tpl1736302668562.png", threshold=0.98, record_pos=(-0.213, -0.579), resolution=(1080, 2412)), "设备默认工作模式显示Auto")
# assert_exists(Template(r"tpl1736302720017.png", threshold=0.98, record_pos=(0.23, -0.572), resolution=(1080, 2412)), "设备默认的目标湿度显示50%")
# assert_exists(Template(r"tpl1736302778729.png", threshold=0.98, record_pos=(-0.206, -0.435), resolution=(1080, 2412)), "设备默认的灯光模式显示Air Quality")
# assert_exists(Template(r"tpl1736302785334.png", threshold=0.98, record_pos=(0.219, -0.44), resolution=(1080, 2412)), "设备默认的风速显示Auto")
# assert_exists(Template(r"tpl1736302791237.png", threshold=0.98, record_pos=(-0.2, -0.285), resolution=(1080, 2412)), "设备默认的灯光亮度显示Automatic")
# assert_exists(Template(r"tpl1736302795121.png", threshold=0.98, record_pos=(0.211, -0.276), resolution=(1080, 2412)), "设备默认的timer显示off")
# # 返回到app主页
# poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([0.0213, 0.6634])
# poco(desc="Navigate up").click()



