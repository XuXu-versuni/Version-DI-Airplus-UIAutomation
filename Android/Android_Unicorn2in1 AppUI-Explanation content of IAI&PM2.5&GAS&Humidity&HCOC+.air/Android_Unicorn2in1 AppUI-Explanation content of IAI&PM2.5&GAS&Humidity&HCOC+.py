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
# https://nutriu.atlassian.net/browse/CH-56 (AppUI-Explanation content of IAI/PM2.5/GAS/Humidity/HCOC+)

#启动Air+ app
start_app("com.philips.ph.homecare")
assert_equal(poco("com.philips.ph.homecare:id/dashboard_section_title").get_text(),"My Devices","app打开成功")

# https://nutriu.atlassian.net/browse/CH-56
# 进入设备控制页面
poco(desc="https://air-matters.com/app/philips/dark_mode/AC3420_10.png").click()
poco(text="Air Quality").click()
sleep(3.0)
assert_equal(poco("android.widget.TextView").get_text(),"Air quality explained","指数解释页面打开成功")
assert_equal(poco("reading_pm25").get_text(),"PM2.5","PM2.5指数")
poco(text="PM2.5 are fine, inhalable particles with a diameter of 2.5 micrometers or smaller. In comparison: a human hair is about 70 micrometers in diameter. PM2.5 is a common air pollutant and due to its size, can be inhaled and impact your health. Outdoor, it’s emitted from vehicles, industries, fires and construction sites while stoves, fireplaces, pet dander and mould can be a source of PM2.5 indoors. Thanks to your device’s multi-layer filtration system, 99.97% of these particles are captured from the air.").swipe([-0.0717, -0.2094])
assert_equal(poco("android.widget.TextView").get_text(),"PM2.5 are fine, inhalable particles with a diameter of 2.5 micrometers or smaller. In comparison: a human hair is about 70 micrometers in diameter. PM2.5 is a common air pollutant and due to its size, can be inhaled and impact your health. Outdoor, it’s emitted from vehicles, industries, fires and construction sites while stoves, fireplaces, pet dander and mould can be a source of PM2.5 indoors. Thanks to your device’s multi-layer filtration system, 99.97% of these particles are captured from the air.","PM2.5的解释文案显示")
poco(text="PM2.5 are fine, inhalable particles with a diameter of 2.5 micrometers or smaller. In comparison: a human hair is about 70 micrometers in diameter. PM2.5 is a common air pollutant and due to its size, can be inhaled and impact your health. Outdoor, it’s emitted from vehicles, industries, fires and construction sites while stoves, fireplaces, pet dander and mould can be a source of PM2.5 indoors. Thanks to your device’s multi-layer filtration system, 99.97% of these particles are captured from the air.").swipe([-0.1466, -0.2709])
sleep(3.0)
assert_exists(Template(r"tpl1736304121378.png", threshold=0.98, record_pos=(0.012, 0.644), resolution=(1080, 2412)), "PM2.5的指数等级显示")
swipe(Template(r"tpl1736304224612.png", record_pos=(-0.157, -0.169), resolution=(1080, 2412)), vector=[0.0187, 0.303])
assert_equal(poco("reading_iai").get_text(),"IAI","IAI指数")
poco(text="IAI").click()
poco(text="The most common airborne allergens are pollen, animal dander, dust mites and mold. Some of these allergens are seasonal, while others can bother people with allergies year round. And while certain allergens, like pollen, are most common outdoors, they can still impact you or your family indoors. Once you know what’s at the root of your allergies, there are some quick fixes you can make to manage them. But more importantly, your device filters 99.97% of airborne allergens out of the air.").swipe([-0.0343, -0.1879])
assert_equal(poco("android.widget.TextView").get_text(),"The most common airborne allergens are pollen, animal dander, dust mites and mold. Some of these allergens are seasonal, while others can bother people with allergies year round. And while certain allergens, like pollen, are most common outdoors, they can still impact you or your family indoors. Once you know what’s at the root of your allergies, there are some quick fixes you can make to manage them. But more importantly, your device filters 99.97% of airborne allergens out of the air.","IAI的解释文案显示")
assert_exists(Template(r"tpl1736316813163.png", threshold=0.98, record_pos=(0.002, 0.605), resolution=(1080, 2400)), "IAI的指数等级显示")
swipe(Template(r"tpl1736304224612.png", record_pos=(-0.157, -0.169), resolution=(1080, 2412)), vector=[0.0187, 0.303])
assert_equal(poco("reading_humidity").get_text(),"Humidity","Humidity指数")
poco(text="Humidity").click()
poco(text="Comfortable humidity levels are anywhere between 40% and 60%. Levels above 70% are known to cause the growth of mold, mildew, bacteria and dust mites over time. When levels drop below 30%, you may experience dry skin, allergies, headaches and irritated eyes. Besides using your humidifier, it is important to regularly open your windows for airflow, keep the heating at a low temperature and put plants around the house in order to maintain the best indoor humidity levels.").swipe([-0.0093, -0.157])
assert_equal(poco("android.widget.TextView").get_text(),"Comfortable humidity levels are anywhere between 40% and 60%. Levels above 70% are known to cause the growth of mold, mildew, bacteria and dust mites over time. When levels drop below 30%, you may experience dry skin, allergies, headaches and irritated eyes. Besides using your humidifier, it is important to regularly open your windows for airflow, keep the heating at a low temperature and put plants around the house in order to maintain the best indoor humidity levels.","Humidity的解释文案显示")
assert_exists(Template(r"tpl1736317478929.png", threshold=0.98, record_pos=(0.004, 0.666), resolution=(1080, 2400)), "Humidity的指数等级显示")
poco(text="Back").click()
poco(desc="Navigate up").click()






