# -*- encoding=utf8 -*-
__author__ = "xfdzl"

from airtest.core.api import *
from airtest.core.api import connect_device,shell_exec
auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco


#以下是python脚本安装apk包，用于覆盖安装测试等
# def fun1(threadName, apkPath):
#     print(f'start install apk by airtest , thread name: {com.philips.ph.homecare}, apkPath:{"C:\Users\xfdzl\Downloads\Version 3.11.0.919 (87).apk"}')
#     install(apkPath)
init_device("Android")
t = threading.Thread(target=fun1, args=("thread-install-apk", "Version 3.11.0.919 (87).apk"))
t.start()
# 根据个人情况调整
sleep(12)
touch(Template(r"tpl1673425386842.png", record_pos=(-0.004, 0.956), resolution=(1080, 2400)))
t.join()
print("install apk by Airtest finished!!")



#以下还是python脚本安装覆盖apk的写法
# 连接设备
device = connect_device("Android")
# APK 文件的路径
apk_path = "C:/Users/xfdzl/Downloads/Version 3.11.0.919 (87).apk"
# 安装 APK 的 ADB 命令
install_cmd = f"adb -s {device.serialno} install -r {apk_path}"
# 执行 ADB 命令
result = shell_exec(install_cmd)
# 打印结果
print("Installation result:", result)


#以下是另外一种,使用lua脚本来直接调用adb安装，也是用于覆盖安装测试

# local adb  = require("adb")
# adb.install("C:\Users\xfdzl\Downloads\Version 3.11.0.919 (87).apk")





