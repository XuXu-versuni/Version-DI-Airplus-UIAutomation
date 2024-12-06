# -*- encoding=utf8 -*-
__author__ = "xuxu"
'''

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import os
from airtest.cli.runner import run 

from airtest.core.api import auto_setup
#from airtest.core.api import run_script

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/09181FDD4000E1?ori_method=ADBORI&touch_method=MAXTOUCH&",])

# script content
print("start...")
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
# 假设这些air文件夹都在同一个主目录下
main_folder = "Version - DI - Airplus - UIAutomation"

# 列出所有要执行的air文件夹的名字（这里需要根据实际情况修改）
air_folders = [
    "air+ - install",
    "air+ - device control block",
    "air+ - Checking the profile page(No device)"]


def run_air_scripts():
    for folder in air_folders:
        # 构建air脚本文件的路径
        air_script_path = os.path.join(main_folder, folder, folder + ".air")
        # 使用Airtest的run脚本函数来执行air脚本
        # 这里假设Airtest的相关配置已经正确设置
        run(air_script_path)

if __name__ == "__main__":
    run_air_scripts()
'''
# import random
# print(random.random())
#
# from airtest.core.api import auto_setup
# print(auto_setup)

#
# from airtest.core.api import *
# # 定义一个函数来执行.air文件
# def run_air_file(air_file_path):
#     connect_device("android://127.0.0.1:5037/09181FDD4000E1")  # 连接设备，确保你的设备已经连接并且Airtest IDE能够识别
#     run(air_file_path)  # 执行.air文件
#     print(f"完成运行{air_file_path}")
#     close_device()  # 执行完毕后断开设备连接
#
#
# # 定义一个主函数来控制执行顺序
# def main():
#     # 定义.air文件的路径和执行顺序
#     air_files = [
#         "Version-DI-Airplus-UIAutomation/air+ - install.air",
#         "Version-DI-Airplus-UIAutomation/air+ - device control block.air",
#         "Version-DI-Airplus-UIAutomation/air+ - Checking the profile page(No device).air"
#     ]
#
#     # 遍历列表并执行每个.air文件
#     for air_file in air_files:
#         print(f"Running {air_file}...")
#         run_air_file(air_file)
#         print(f"Finished {air_file}.")
#
#
# if __name__ == "__main__":
#     main()
#
#

#
# from airtest.core.api import *
#
#
# # 定义一个函数来执行.air文件
# def run_air_file(air_file_path):
#     try:
#         # 连接设备
#         connect_device("Android://127.0.0.1:5037/09181FDD4000E1")  # 请根据实际情况替换为你的设备连接URI
#         # 执行.air文件
#         run(air_file_path)
#         print(f"Finished running {air_file_path}")
#     except Exception as e:
#         print(f"Error running {air_file_path}: {e}")
#     finally:
#         # 这里可以放置一些清理代码，例如保存日志、截图等
#         pass
#
#
# # 定义一个主函数来控制执行顺序
# def main():
#     # 定义.air文件的路径和执行顺序
#     air_files = [
#         # "Version-DI-Airplus-UIAutomation/air+ - install.air",
#         # "Version-DI-Airplus-UIAutomation/air+ - device control block.air",
#         "Version-DI-Airplus-UIAutomation/air+ - Checking the profile page(No device).air"
#     ]
#
#     # 遍历列表并执行每个.air文件
#     for air_file in air_files:
#         print(f"Running {air_file}...")
#         run_air_file(air_file)
#
#
# if __name__ == "__main__":
#     main()

import os
import importlib.util
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

"""
导入必要的模块：
    os 模块用于处理文件路径。
    importlib.util 模块用于动态加载和执行脚本。
    airtest.core.api 模块用于调用 Airtest 的相关功能。
    poco.drivers.android.uiautomation 模块用于初始化 Poco 对象。
定义脚本路径：
    SCRIPTS 列表中包含所有需要运行的脚本路径。你可以根据需要调整这个列表的顺序。
定义 run_script 函数：
    这个函数接受一个脚本路径作为参数，使用 importlib.util 模块来动态加载和执行该脚本。
    假设每个脚本都有一个名为 main 的函数，如果没有则输出提示信息。
定义 main 函数：
    这个函数遍历 SCRIPTS 列表中的每个脚本路径，并调用 run_script 函数来运行它们。
主入口点：
    if __name__ == "__main__": 确保当直接运行 main.py 时，会调用 main 函数。
"""


# 定义脚本路径
SCRIPTS = [
    # "air+ - install.air/air+ - install.py",
    # "air+ - device control block.air/air+ - device control block.py",
    "air+ - Checking the profile page(No device).air/air+ - Checking the profile page(No device).py"
]


def run_script(script_path):
    """运行单个脚本"""
    print(f"Running script: {script_path}")
    try:
        # 动态加载脚本
        spec = importlib.util.spec_from_file_location("module.name", script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # 假设每个脚本都有一个名为 `main` 的函数
        if hasattr(module, 'main'):
            module.main()
        else:
            print(f"Script {script_path} does not have a main function.")
    except Exception as e:
        print(f"Error running script {script_path}: {e}")


def main():
    """主函数，按顺序运行所有脚本"""
    for script in SCRIPTS:
        run_script(script)


if __name__ == "__main__":
    main()