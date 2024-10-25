# -*- encoding=utf8 -*-
__author__ = "Mengjie"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
#poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

#Stargazer Eva设备
#进入控制页面
poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
#上下滑动屏幕
poco("com.philips.ph.homecare:id/philips_control_layout_id").swipe([-0.0539, -0.5587])
poco("com.philips.ph.homecare:id/philips_control_layout_id").swipe([-0.0488, 0.8438])
poco("com.philips.ph.homecare:id/purifier_control_scroll").swipe([-0.1412, -0.2345])
sleep(3.0)
#设备关机控制
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
#判断设备是否关机
assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"),False,msg="设备关机.")

sleep(3.0)
#设备开机控制
poco("com.philips.ph.homecare:id/philips_control_power_btn_id").click()
#判断设备是否开机
assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"),True,msg="设备开机.")

#童锁打开控制
poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").click()
assert_equal(poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").attr("checked"),True,msg="童锁打开.")

sleep(3.0)
#童锁关闭控制
poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").click()
assert_equal(poco("com.philips.ph.homecare:id/philips_control_childlock_btn_id").attr("checked"),False,msg="童锁关闭.")


#模式切换控制
# poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
# poco("com.philips.ph.homecare:id/work_mode_item_title").click()
# poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# text("Auto")
# touch(Template(r"tpl1723718869652.png", record_pos=(0.03, 0.31), resolution=(1080, 2412)))
# touch(Template(r"tpl1723718931320.png", record_pos=(0.037, 0.204), resolution=(1080, 2412)))
# touch(Template(r"tpl1723718945036.png", record_pos=(0.021, 0.732), resolution=(1080, 2412)))

sleep(3.0)
#模式切换为Auto
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Auto").click()
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731182521.png", record_pos=(0.012, 0.547), resolution=(1080, 2412)), "Auto模式切换成功")

sleep(3.0)
#模式切换为Sleep
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Sleep").click()
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731452159.png", record_pos=(0.006, 0.557), resolution=(1080, 2412)), "Sleep模式切换成功")

sleep(3.0)
#模式切换为Medium
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="Medium").click()
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731497712.png", record_pos=(0.017, 0.551), resolution=(1080, 2412)), "Medium模式切换成功")

sleep(3.0)
#模式切换为High
poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
poco(text="High").click()
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731551102.png", record_pos=(0.002, 0.553), resolution=(1080, 2412)), "High模式切换成功")



# #Auto
# poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
# poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.philips.ph.homecare:id/philips_control_sheet_list").child("android.widget.LinearLayout")[0].click()
# poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()

# #Sleep
# poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.philips.ph.homecare:id/philips_control_sheet_list").child("android.widget.LinearLayout")[1].click()
# poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
# #Medium
# poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.philips.ph.homecare:id/philips_control_sheet_list").child("android.widget.LinearLayout")[2].click()
# poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()
# #High
# poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.philips.ph.homecare:id/philips_control_sheet_list").child("android.widget.LinearLayout")[3].click()
# poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
# poco("com.philips.ph.homecare:id/philips_control_auto_btn_id").click()



#环境灯光控制
# touch(Template(r"tpl1723719063049.png", record_pos=(-0.206, 0.447), resolution=(1080, 2412)))
# touch(Template(r"tpl1723719094228.png", record_pos=(-0.249, -0.087), resolution=(1080, 2412)))
# touch(Template(r"tpl1723719099598.png", record_pos=(0.03, 0.756), resolution=(1080, 2412)))

sleep(3.0)
#湿度灯的切换
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_humidity").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731828009.png", threshold = 0.98, record_pos=(-0.208, 0.695), resolution=(1080, 2412)), "Huimidity切换成功")


sleep(3.0)
#环境灯的切换（Ambient:Warm）
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_warm").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731935717.png", threshold = 0.98, record_pos=(-0.206, 0.628), resolution=(1080, 2412)), "Ambient:Warm切换成功")


sleep(3.0)
#环境灯的切换（Ambient:Dawn）
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_dawn").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726731985254.png", threshold = 0.98, record_pos=(-0.206, 0.626), resolution=(1080, 2412)), "Ambient:Dawn切换成功")

sleep(3.0)
#环境灯的切换（Ambient:Calm）
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_calm").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732012578.png", threshold = 0.98, record_pos=(-0.201, 0.623), resolution=(1080, 2412)), "Ambient:Calm切换成功")

sleep(3.0)
#环境灯的切换（Ambient:Breath）
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_breath").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732052079.png", threshold = 0.98, record_pos=(-0.199, 0.629), resolution=(1080, 2412)), "Ambient:Breath切换成功")

sleep(3.0)
#灯光关闭
poco("com.philips.ph.homecare:id/philips_control_light_mode_btn_id").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_lamp_off").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732109040.png", threshold = 0.98, record_pos=(-0.206, 0.629), resolution=(1080, 2412)), "灯光关闭成功")


#灯光亮度控制
sleep(3.0)
#灯光切换为亮
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Bright").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732266066.png", threshold = 0.98, record_pos=(-0.211, 0.781), resolution=(1080, 2412)), "灯光切换为亮成功")

sleep(3.0)
#灯光切换为暗
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Low").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732335858.png", threshold = 0.98, record_pos=(-0.208, 0.778), resolution=(1080, 2412)), "灯光切换为暗成功")


sleep(3.0)
#灯光切换为关闭
poco("com.philips.ph.homecare:id/philips_control_light_brightness_btn_id").click()
poco(text="Off").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732379261.png", threshold = 0.98, record_pos=(-0.198, 0.784), resolution=(1080, 2412)), "灯光切换为关闭成功")


# assert_equal("Humidity between 40% and 60% is ideal for your health and comfort.", "Humidity between 40% and 60% is ideal for your health and comfort. ", "请填写测试点.")


# assert_equal(poco("com.philips.ph.homecare:id/philips_control_sheet_message").get_text(),"Humidity between 40% and 60% is ideal for your health and comfort.","目标湿度控制功能的文案显示正确")

# assert_equal(poco("com.philips.ph.homecare:id/philips_control_sheet_message").attr("checked"),False,"kuhoiuho")



#要比对文本，文本的具体句子就是元素值，应该用get；要是用attr来断定属性text的值是不是真或者假
# #公式
# assert_equal(poco("元素名").get_text(),"文本值","需要输出的断言结果")
# assert_equal(poco("元素名").attr("属性名"),属性值,"需要输出的断言结果")




sleep(3.0)
#目标湿度控制-30%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.5, 0.5])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726732810609.png", threshold = 0.98, record_pos=(0.209, 0.706), resolution=(1080, 2412)), "目标湿度30%切换成功")

sleep(3.0)
# 目标湿度控制-35%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.008, -0.0287])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729663414303.png", threshold = 0.98, record_pos=(0.218, 0.202), resolution=(1080, 2412)),"目标湿度35%切换成功")

sleep(3.0)
# 目标湿度控制-40%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.008, -0.0287])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729664764540.png", threshold = 0.98, record_pos=(0.211, 0.715), resolution=(1080, 2412)),"目标湿度控制-40%")

sleep(3.0)
# 目标湿度控制-45%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.008, -0.0287])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729664943095.png", threshold = 0.98, record_pos=(0.226, 0.706), resolution=(1080, 2412)),"目标湿度控制-45%")

sleep(3.0)
# 目标湿度控制-50%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.008, -0.0287])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729665085402.png", threshold = 0.98, record_pos=(0.23, 0.704), resolution=(1080, 2412)),"目标湿度控制-50%")

sleep(3.0)
# 目标湿度控制-55%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.008, -0.0287])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729665288520.png", threshold = 0.98, record_pos=(0.223, 0.706), resolution=(1080, 2412)),"目标湿度控制-55%")


sleep(3.0)
# 目标湿度控制-60%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.008, -0.0287])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729665469785.png", threshold = 0.98, record_pos=(0.229, 0.626), resolution=(1080, 2412)),"目标湿度控制-60%")


sleep(3.0)
# 目标湿度控制-65%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.008, -0.0287])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729666084526.png", threshold = 0.98, record_pos=(0.229, 0.708), resolution=(1080, 2412)),"目标湿度控制-65%")

sleep(3.0)
#目标湿度控制-70%
poco("com.philips.ph.homecare:id/philips_control_humidity_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.5, -0.5])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1726733595868.png", threshold = 0.98, record_pos=(0.209, 0.701), resolution=(1080, 2412)), "目标湿度70%切换成功")




# touch(Template(r"tpl1723719131401.png", record_pos=(0.229, 0.454), resolution=(1080, 2412)))
 

# touch(Template(r"tpl1723719143872.png", record_pos=(0.014, 0.331), resolution=(1080, 2412)))
# touch(Template(r"tpl1723719150076.png", record_pos=(0.017, 0.731), resolution=(1080, 2412)))

# sleep(3.0)


# #CH-1592
# #timer开关控制
# poco("com.philips.ph.homecare:id/philips_control_timer_btn_id").click()
# poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([-0.0128, -0.0287])
# poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()


# #组合断言
# try:
#     assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"), True, "设备关机")
# except:
#     assert_equal(poco("com.philips.ph.homecare:id/philips_control_power_btn_id").attr("checked"), False, "设备关机")













