__author__ = "xjinp"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
poco = AndroidUiautomationPoco()
auto_setup(__file__)
# 打开 App
poco(text="Air+").click()
sleep(2)

# 点击 Add a device
poco("com.philips.ph.homecare:id/dashboard_footer_btn").click()
sleep(2)
# 返回App主页
poco("Navigate up").click()

sleep(1)
#‘主页有Add a device’这个按钮，验证当前页面是否有 add a device 按钮
assert_equal(poco("com.philips.ph.homecare:id/dashboard_footer_btn").attr("enabled"),True,msg="有 add a device 按钮，返回主页成功")
             
# 再次点击 Add a device 按钮 进入 connect device 页面
poco("com.philips.ph.homecare:id/dashboard_footer_btn").click()
sleep(2)

# 点击 let's Start 进行下一步
poco("com.philips.ph.homecare:id/philips_pairing_start_btn").click()
sleep(2)

# 设备未触发配网
sleep(5)

# 点击Next 进行下一步 然后等待5秒，让app页面刷新完成
poco("com.philips.ph.homecare:id/philips_pairing_mode_next_btn").swipe([0.053, -0.0059])
sleep(15)

# 点击 connect another device 进行下一步验证
poco("com.philips.ph.homecare:id/philips_pairing_searching_another").click()

sleep(15)

# App 会提示 N devices found

assert_exists(Template(r"tpl1729057637233.png", record_pos=(-0.018, 0.657), resolution=(1440, 3088)), "Pass")


# # 点击connect Philips setup
# poco("android:id/button1").click()
# sleep(5)

# # 选择添加手动网络 配网
# poco("com.philips.ph.homecare:id/philips_pairing_searching_manual").click()
# poco("com.philips.ph.homecare:id/philips_pairing_wifi_manually_btn").click()

# #输入 WiFi 名称
# poco("com.philips.ph.homecare:id/philips_pairing_wifi_input_ssid").click()
# text("2F-LAB")

# #输入WiFi 密码
# poco("com.philips.ph.homecare:id/philips_pairing_wifi_input_password").click()
# text("qwer1234")

# #点击下一步
# poco("com.philips.ph.homecare:id/philips_pairing_wifi_input_next_btn").click()

# sleep(15)
# # 选择你要配网的WiFi 网络 输入WiFi 密码
# # poco(text="2F-LAB").click()
# # poco("com.philips.ph.homecare:id/dialogEdit_edittext_id").click()
# # text("qwer1234")
# # poco("android:id/button1").click()

# # 选择你想要设置的设备名称，点击下一步 next
# poco(text="Bedroom").click()
# sleep(2)

# # 点击 next
# poco("com.philips.ph.homecare:id/philips_pairing_name_next_btn").click()

# # 点击完成
# poco("com.philips.ph.homecare:id/philips_pair_finish_ok_btn").click()
# sleep(1)


# assert_not_exists(Template(r"tpl1728553068294.png", record_pos=(0.002, -0.059), resolution=(1440, 3088)), "App 页面没有这个按钮，代表设备已存在，设备已经成功配网成功")






