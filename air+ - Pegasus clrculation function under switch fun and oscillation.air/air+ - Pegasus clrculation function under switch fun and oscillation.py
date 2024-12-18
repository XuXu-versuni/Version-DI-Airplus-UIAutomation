# -*- encoding=utf8 -*-
__author__ = "Mengjie"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device
#poco初始化脚本
poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)

"""
整个脚本中，注意修改断言阈值，就是threshold的值，另外注意touch的元素的唯一值可用值是否合适。
#Oneplus10
#Pegasus 3in1 device(CH-1560-CH-1561)
#进入设备控制页面

"""
#这两个元素图片的名字在 view树中是一样的，这里需要取其他的参数值来判断不然给别人用的时候就会报错
#poco("com.philips.ph.homecare:id/dashboard_device_cover").click()
poco(desc = "https://air-matters.com/app/philips/dark_mode/AMF870_15.png").click()


assert_equal(poco("com.philips.ph.homecare:id/purifier_control_readings_title").get_text(),"Air Quality","进入设备控制页面成功")
swipe(Template(r"tpl1730166215530.png", record_pos=(0.035, 0.281), resolution=(1080, 2412)), vector=[0.0, -0.3377])


sleep(3.0)
#当功能切换为“Circulation”时，设置风速为1成功，并且oscillation设置成功
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728972713217.png", record_pos=(-0.206, 0.33), resolution=(1080, 2412)),"选择Circulation成功")

sleep(3.0)
#设置风速为1成功
#touch(Template(r"tpl1728974420055.png", record_pos=(0.213, 0.679), resolution=(1080, 2412)))
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()

poco("com.philips.ph.homecare:id/philips_control_sheet_picker").swipe([0.5, 0.5])
touch(Template(r"tpl1728974361700.png", record_pos=(0.017, 0.344), resolution=(1080, 2412)))
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1730276563618.png", threshold = 0.96, record_pos=(0.214, 0.146), resolution=(1080, 2340)),"设置风速为1成功")
#tpl1729481262797.png
sleep(3.0)
#设置Oscillation=45°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([189,1808],[189,1808])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729060942347.png", threshold = 0.98, record_pos=(0.001, 0.047), resolution=(1080, 2412)),"设置Oscillation=45°成功")

#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729061125453.png", record_pos=(-0.302, 0.573), resolution=(1080, 2412)), vector=[-0.0735, 0.0029])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=90°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728987904437.png", threshold = 0.98, record_pos=(-0.004, 0.978), resolution=(1080, 2412)),"设置Oscillation=90°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")
#设置Oscillation=180°成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([517,1811],[517,1811])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729063008272.png", threshold = 0.98, record_pos=(0.017, 0.696), resolution=(1080, 2412)),"设置Oscillation=180°成功")
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729063144748.png", record_pos=(-0.005, 0.573), resolution=(1080, 2412)), vector=[-0.4281, -0.0157])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=350°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([0.841, -0.0052])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1728975091959.png", threshold = 0.98, record_pos=(0.008, 0.985), resolution=(1080, 2412)),"设置Oscillation=350°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")


#(CH-1562-CH-1563)
#当功能切换为“Circulation”时，设置风速为2成功，并且oscillation设置成功
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728972713217.png", record_pos=(-0.206, 0.33), resolution=(1080, 2412)),"选择Circulation成功")

sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1728980059561.png", threshold = 0.98, record_pos=(0.066, 0.415), resolution=(1080, 2412)), vector=[-0.0173, -0.0259])
sleep(6.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()


sleep(3.0)
assert_exists(Template(r"tpl1728991840545.png", threshold = 0.98, record_pos=(0.213, 0.686), resolution=(1080, 2412)), "设置风速为2成功")


sleep(3.0)
#设置Oscillation=45°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([189,1808],[189,1808])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729060942347.png", threshold = 0.98, record_pos=(0.001, 0.047), resolution=(1080, 2412)),"设置Oscillation=45°成功")

#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729061125453.png", record_pos=(-0.302, 0.573), resolution=(1080, 2412)), vector=[-0.0735, 0.0029])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=90°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728987904437.png", threshold = 0.98, record_pos=(-0.004, 0.978), resolution=(1080, 2412)),"设置Oscillation=90°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")
#设置Oscillation=180°成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([517,1811],[517,1811])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729063008272.png", threshold = 0.98, record_pos=(0.017, 0.696), resolution=(1080, 2412)),"设置Oscillation=180°成功")
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729063144748.png", record_pos=(-0.005, 0.573), resolution=(1080, 2412)), vector=[-0.4281, -0.0157])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=350°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([0.841, -0.0052])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1728975091959.png", threshold = 0.98, record_pos=(0.008, 0.985), resolution=(1080, 2412)),"设置Oscillation=350°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")


# (CH-1564-CH-1565)
#当功能切换为“Circulation”时，设置风速为3成功，并且oscillation设置成功
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728972713217.png", record_pos=(-0.206, 0.33), resolution=(1080, 2412)),"选择Circulation成功")

sleep(3.0)
#风速重置到风速1
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729045363213.png", record_pos=(0.09, 0.412), resolution=(1080, 2412)), vector=[-0.0202, 0.0285])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729045729271.png",threshold = 0.98, record_pos=(0.219, 0.685), resolution=(1080, 2412)),"风速重置为1成功")
#设置风速为3成功
sleep(3.0)

poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729486248752.png", threshold = 0.98, record_pos=(0.099, 0.469), resolution=(1080, 2412)), vector=[-0.0428, -0.0658])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()




assert_exists(Template(r"tpl1729482075708.png", threshold = 0.98, record_pos=(0.216, 0.654), resolution=(1080, 2412)),"风速重置为3成功")


sleep(3.0)
#设置Oscillation=45°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([189,1808],[189,1808])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729060942347.png", threshold = 0.98, record_pos=(0.001, 0.047), resolution=(1080, 2412)),"设置Oscillation=45°成功")

#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729061125453.png", record_pos=(-0.302, 0.573), resolution=(1080, 2412)), vector=[-0.0735, 0.0029])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=90°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728987904437.png", threshold = 0.98, record_pos=(-0.004, 0.978), resolution=(1080, 2412)),"设置Oscillation=90°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")
#设置Oscillation=180°成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([517,1811],[517,1811])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729063008272.png", threshold = 0.98, record_pos=(0.017, 0.696), resolution=(1080, 2412)),"设置Oscillation=180°成功")
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729063144748.png", record_pos=(-0.005, 0.573), resolution=(1080, 2412)), vector=[-0.4281, -0.0157])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=350°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([0.841, -0.0052])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1728975091959.png", threshold = 0.98, record_pos=(0.008, 0.985), resolution=(1080, 2412)),"设置Oscillation=350°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")


#(CH-1566-CH-1567)
#当功能切换为“Circulation”时，设置风速为4成功，并且oscillation设置成功
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728972713217.png", record_pos=(-0.206, 0.33), resolution=(1080, 2412)),"选择Circulation成功")

sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729048337594.png", record_pos=(0.202, 0.271), resolution=(1080, 2412)), vector=[-0.0134, 0.0524])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1729048413238.png", threshold = 0.98, record_pos=(0.21, 0.679), resolution=(1080, 2412)),"风速重置为1成功")

#风速设置为4成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729048607344.png", threshold = 0.98, record_pos=(0.242, 0.469), resolution=(1080, 2412)), vector=[-0.0602, -0.0943])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729048780051.png", threshold = 0.98, record_pos=(0.223, 0.681), resolution=(1080, 2412)),"风速设置为4成功")

sleep(3.0)
#设置Oscillation=45°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([189,1808],[189,1808])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729060942347.png", threshold = 0.98, record_pos=(0.001, 0.047), resolution=(1080, 2412)),"设置Oscillation=45°成功")

#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729061125453.png", record_pos=(-0.302, 0.573), resolution=(1080, 2412)), vector=[-0.0735, 0.0029])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=90°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728987904437.png", threshold = 0.98, record_pos=(-0.004, 0.978), resolution=(1080, 2412)),"设置Oscillation=90°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")
#设置Oscillation=180°成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([517,1811],[517,1811])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729063008272.png", threshold = 0.98, record_pos=(0.017, 0.696), resolution=(1080, 2412)),"设置Oscillation=180°成功")
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729063144748.png", record_pos=(-0.005, 0.573), resolution=(1080, 2412)), vector=[-0.4281, -0.0157])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=350°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([0.841, -0.0052])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1728975091959.png", threshold = 0.98, record_pos=(0.008, 0.985), resolution=(1080, 2412)),"设置Oscillation=350°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")



#(CH-1569-CH-1570)
#当功能切换为“Circulation”时，设置风速为5成功，并且oscillation设置成功
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728972713217.png", record_pos=(-0.206, 0.33), resolution=(1080, 2412)),"选择Circulation成功")

#风速重置为1成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729057473333.png", record_pos=(0.168, 0.27), resolution=(1080, 2412)), vector=[0.0447, 0.0901])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1729048413238.png", threshold = 0.98, record_pos=(0.21, 0.679), resolution=(1080, 2412)),"风速重置为1成功")

#风速设置为5成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729057594359.png", threshold = 0.98, record_pos=(0.184, 0.526), resolution=(1080, 2412)), vector=[-0.0319, -0.1259])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1729057705446.png",threshold = 0.98, record_pos=(0.225, 0.689), resolution=(1080, 2412)),"风速设置为5成功")

sleep(3.0)
#设置Oscillation=45°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([189,1808],[189,1808])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729060942347.png", threshold = 0.98, record_pos=(0.001, 0.047), resolution=(1080, 2412)),"设置Oscillation=45°成功")

#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729061125453.png", record_pos=(-0.302, 0.573), resolution=(1080, 2412)), vector=[-0.0735, 0.0029])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=90°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728987904437.png", threshold = 0.98, record_pos=(-0.004, 0.978), resolution=(1080, 2412)),"设置Oscillation=90°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")
#设置Oscillation=180°成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([517,1811],[517,1811])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729063008272.png", threshold = 0.98, record_pos=(0.017, 0.696), resolution=(1080, 2412)),"设置Oscillation=180°成功")
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729063144748.png", record_pos=(-0.005, 0.573), resolution=(1080, 2412)), vector=[-0.4281, -0.0157])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=350°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([0.841, -0.0052])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1728975091959.png", threshold = 0.98, record_pos=(0.008, 0.985), resolution=(1080, 2412)),"设置Oscillation=350°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")


#(CH-1571-CH-1572)
#当功能切换为“Circulation”时，设置风速为6成功，并且oscillation设置成功
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728972713217.png", record_pos=(-0.206, 0.33), resolution=(1080, 2412)),"选择Circulation成功")

#风速重置为1成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729059225417.png", record_pos=(0.181, 0.232), resolution=(1080, 2412)), vector=[0.0927, 0.1187])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1729048413238.png", threshold = 0.98, record_pos=(0.21, 0.679), resolution=(1080, 2412)),"风速重置为1成功")

#风速设置为6成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729062493790.png", threshold = 0.98, record_pos=(0.196, 0.5), resolution=(1080, 2412)), vector=[-0.0511, -0.1488])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1729058368490.png", threshold = 0.98, record_pos=(0.219, 0.68), resolution=(1080, 2412)),"风速设置为6成功")

sleep(3.0)
#设置Oscillation=45°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([189,1808],[189,1808])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729060942347.png", threshold = 0.98, record_pos=(0.001, 0.047), resolution=(1080, 2412)),"设置Oscillation=45°成功")

#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729061125453.png", record_pos=(-0.302, 0.573), resolution=(1080, 2412)), vector=[-0.0735, 0.0029])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=90°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728987904437.png", threshold = 0.98, record_pos=(-0.004, 0.978), resolution=(1080, 2412)),"设置Oscillation=90°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")
#设置Oscillation=180°成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([517,1811],[517,1811])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729063008272.png", threshold = 0.98, record_pos=(0.017, 0.696), resolution=(1080, 2412)),"设置Oscillation=180°成功")
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729063144748.png", record_pos=(-0.005, 0.573), resolution=(1080, 2412)), vector=[-0.4281, -0.0157])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=350°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([0.841, -0.0052])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1728975091959.png", threshold = 0.98, record_pos=(0.008, 0.985), resolution=(1080, 2412)),"设置Oscillation=350°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")


#(CH-1573-CH-1574)
#当功能切换为“Circulation”时，设置风速为7成功，并且oscillation设置成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728972713217.png", record_pos=(-0.206, 0.33), resolution=(1080, 2412)),"选择Circulation成功")

#风速重置为1成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729152546313.png", record_pos=(0.135, 0.241), resolution=(1080, 2412)), vector=[0.0319, 0.154])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1729048413238.png", threshold = 0.98, record_pos=(0.21, 0.679), resolution=(1080, 2412)),"风速重置为1成功")

#风速设置为7成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729156273352.png", threshold = 0.98, record_pos=(0.196, 0.548), resolution=(1080, 2412)), vector=[0.0286, -0.1759])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1729132557111.png", threshold = 0.98, record_pos=(0.218, 0.292), resolution=(1080, 2412)),"风速设置为7成功")

sleep(3.0)
#设置Oscillation=45°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([189,1808],[189,1808])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729060942347.png", threshold = 0.98, record_pos=(0.001, 0.047), resolution=(1080, 2412)),"设置Oscillation=45°成功")

#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729061125453.png", record_pos=(-0.302, 0.573), resolution=(1080, 2412)), vector=[-0.0735, 0.0029])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=90°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728987904437.png", threshold = 0.98, record_pos=(-0.004, 0.978), resolution=(1080, 2412)),"设置Oscillation=90°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")
#设置Oscillation=180°成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([517,1811],[517,1811])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729063008272.png", threshold = 0.98, record_pos=(0.017, 0.696), resolution=(1080, 2412)),"设置Oscillation=180°成功")
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729063144748.png", record_pos=(-0.005, 0.573), resolution=(1080, 2412)), vector=[-0.4281, -0.0157])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=350°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([0.841, -0.0052])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1728975091959.png", threshold = 0.98, record_pos=(0.008, 0.985), resolution=(1080, 2412)),"设置Oscillation=350°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")


#(CH-1575-CH-1576)
#当功能切换为“Circulation”时，设置风速为8成功，并且oscillation设置成功
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728972713217.png", record_pos=(-0.206, 0.33), resolution=(1080, 2412)),"选择Circulation成功")

#风速重置为1成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729135388683.png", record_pos=(0.242, 0.237), resolution=(1080, 2412)), vector=[-0.0344, 0.1816])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1729048413238.png", threshold = 0.98, record_pos=(0.21, 0.679), resolution=(1080, 2412)),"风速重置为1成功")

#风速设置为8成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729135590281.png", threshold = 0.98, record_pos=(0.335, 0.492), resolution=(1080, 2412)), vector=[-0.0859, -0.2077])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1729135666370.png", threshold = 0.98, record_pos =(0.233, -0.061), resolution=(1080, 2412)),"风速且设置为8成功")

sleep(3.0)
#设置Oscillation=45°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([189,1808],[189,1808])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729060942347.png", threshold = 0.98, record_pos=(0.001, 0.047), resolution=(1080, 2412)),"设置Oscillation=45°成功")

#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729061125453.png", record_pos=(-0.302, 0.573), resolution=(1080, 2412)), vector=[-0.0735, 0.0029])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=90°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728987904437.png", threshold = 0.98, record_pos=(-0.004, 0.978), resolution=(1080, 2412)),"设置Oscillation=90°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")
#设置Oscillation=180°成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([517,1811],[517,1811])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729063008272.png", threshold = 0.98, record_pos=(0.017, 0.696), resolution=(1080, 2412)),"设置Oscillation=180°成功")
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729063144748.png", record_pos=(-0.005, 0.573), resolution=(1080, 2412)), vector=[-0.4281, -0.0157])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=350°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([0.841, -0.0052])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1728975091959.png", threshold = 0.98, record_pos=(0.008, 0.985), resolution=(1080, 2412)),"设置Oscillation=350°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")


#(CH-1577-CH-1578)
#当功能切换为“Circulation”时，设置风速为9成功，并且oscillation设置成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728972713217.png", record_pos=(-0.206, 0.33), resolution=(1080, 2412)),"选择Circulation成功")

sleep(3.0)
# 风速重置为1成功
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729152921217.png", threshold = 0.98, record_pos=(0.16, 0.224), resolution=(1080, 2412)), vector=[-0.0035, 0.1969])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1729048413238.png", threshold = 0.98, record_pos=(0.21, 0.679), resolution=(1080, 2412)),"风速重置为1成功")

#风速切换为9成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729153120908.png", threshold = 0.98, record_pos=(0.16, 0.529), resolution=(1080, 2412)), vector=[0.0142, -0.2286])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1729153388544.png", threshold = 0.98, record_pos=(0.208, 0.443), resolution=(1080, 2412)),"风速切换为9成功")

sleep(3.0)
#设置Oscillation=45°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([189,1808],[189,1808])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729060942347.png", threshold = 0.98, record_pos=(0.001, 0.047), resolution=(1080, 2412)),"设置Oscillation=45°成功")

#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729061125453.png", record_pos=(-0.302, 0.573), resolution=(1080, 2412)), vector=[-0.0735, 0.0029])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=90°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728987904437.png", threshold = 0.98, record_pos=(-0.004, 0.978), resolution=(1080, 2412)),"设置Oscillation=90°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")
#设置Oscillation=180°成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([517,1811],[517,1811])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729063008272.png", threshold = 0.98, record_pos=(0.017, 0.696), resolution=(1080, 2412)),"设置Oscillation=180°成功")
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729063144748.png", record_pos=(-0.005, 0.573), resolution=(1080, 2412)), vector=[-0.4281, -0.0157])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=350°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([0.841, -0.0052])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1728975091959.png", threshold = 0.98, record_pos=(0.008, 0.985), resolution=(1080, 2412)),"设置Oscillation=350°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")


#(CH-1579-CH-1580)
#当功能切换为“Circulation”时，设置风速为10成功，并且oscillation设置成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_pegasus_function_btn").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_picker").click()
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728972713217.png", record_pos=(-0.206, 0.33), resolution=(1080, 2412)),"选择Circulation成功")

sleep(3.0)
# 风速重置为1成功
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1729153667872.png", threshold = 0.98, record_pos=(0.213, 0.252), resolution=(1080, 2412)), vector=[0.0106, 0.235])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1729048413238.png", threshold = 0.98, record_pos=(0.21, 0.679), resolution=(1080, 2412)),"风速重置为1成功")

sleep(3.0)
# 风速切换为10成功
poco("com.philips.ph.homecare:id/philips_control_fanspeed_btn_id").click()
swipe(Template(r"tpl1730168601989.png", record_pos=(0.196, 0.53), resolution=(1080, 2412)), vector=[0.0222, -0.2967])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1729153830359.png", threshold = 0.98, record_pos=(0.226, 0.443), resolution=(1080, 2412)),"风速切换为10成功")

sleep(3.0)
#设置Oscillation=45°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([189,1808],[189,1808])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729060942347.png", threshold = 0.98, record_pos=(0.001, 0.047), resolution=(1080, 2412)),"设置Oscillation=45°成功")

#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729061125453.png", record_pos=(-0.302, 0.573), resolution=(1080, 2412)), vector=[-0.0735, 0.0029])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=90°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1728984949422.png", record_pos=(-0.297, 0.582), resolution=(1080, 2340)), vector=[0.0823, 0.0109])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728987904437.png", threshold = 0.98, record_pos=(-0.004, 0.978), resolution=(1080, 2412)),"设置Oscillation=90°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")
#设置Oscillation=180°成功
sleep(3.0)
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe([517,1811],[517,1811])
sleep(3.0)
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1729063008272.png", threshold = 0.98, record_pos=(0.017, 0.696), resolution=(1080, 2412)),"设置Oscillation=180°成功")
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
swipe(Template(r"tpl1729063144748.png", record_pos=(-0.005, 0.573), resolution=(1080, 2412)), vector=[-0.4281, -0.0157])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")

sleep(3.0)
#设置Oscillation=350°成功
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([0.841, -0.0052])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()

assert_exists(Template(r"tpl1728975091959.png", threshold = 0.98, record_pos=(0.008, 0.985), resolution=(1080, 2412)),"设置Oscillation=350°成功")
sleep(3.0)
#Oscillation重置成功，显示为off
poco("com.philips.ph.homecare:id/philips_control_oscillation_btn_id").click()
poco("com.philips.ph.homecare:id/philips_control_sheet_seekbar").swipe([-0.8526, -0.0091])
poco("com.philips.ph.homecare:id/dialog_control_sheet_apply").click()
assert_exists(Template(r"tpl1728975923625.png", threshold = 0.98, record_pos=(-0.001, 0.978), resolution=(1080, 2412)),"Oscillation重置成功,显示为off")



