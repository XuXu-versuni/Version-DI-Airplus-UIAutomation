#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Main_linkage_script.py    
@Version:  python3.7 
@Software: PyCharm 
@Contact :   xfdzl5256@126.com
@Author  :   xfdzl
@Modify Time            @Version    @Desciption
------------            --------    -----------
2024/11/11 下午2:24         1.0         None
"""

import os
import importlib.util
from airtest.core.api import *
from airtest.report.report import simple_report
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
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android://127.0.0.1:5037",])


def connect_to_device(device_id):
    """
    连接指定设备并检查连接状态
    
    尝试连接到给定设备ID的设备。如果连接失败，将打印错误信息并返回False。
    如果连接成功，将打印连接信息并返回True。
    
    参数:
    device_id (str): 设备的唯一标识符
    
    返回:
    bool: 如果成功连接到设备，则为True；否则为False
    """
    try:
        # 尝试连接到设备
        connect_device(f"Android:///{device_id}")
        # 如果没有抛出异常，表示连接成功
        print(f"Connected to device: {device_id}")
    except Exception as e:
        # 连接失败，打印错误信息
        print(f"Failed to connect to device {device_id}: {e}")
        # 返回False表示连接失败
        return False
    # 返回True表示连接成功
    return True



    # 定义脚本路径,这里需要确保你已经安装了 airtest 和 poco 模块。
    # 如果没有安装airtest和pooc库可以使用pip安装。并保证pycharm调用的enev的库有他们。
    # 遍历主目录下的所有  .air  目录文件夹，不是文件。
SCRIPTS = [
    # "air+ - install.air/air+ - install.py",
    # "air+ - device control block.air/air+ - device control block.py",
    "air+ - Prometheus device power on&off and mode control.air",
    "air+ - Checking the profile page(No device).air/air+ - Checking the profile page(No device).py"
]



# 以下是主函数的业务逻辑运行路线图
#     A[开始] --> B[打印正在运行的脚本路径]
#     B --> C[动态加载脚本]
#     C --> D{模块有 main 函数吗?}
#     D -->|Yes| E[调用 main 函数]
#     D -->|No| F[打印没有 main 函数的信息]
#     C --> G{发生异常吗?}
#     G -->|Yes| H[打印错误信息]
#     H --> I[创建报告目录]
#     I --> J[生成报告文件]
#     J --> K[打印报告路径]
#     G -->|No| L[结束]


def run_script(script_path):
    """
    运行单个脚

    参数:
    script_path (str): 脚本的路径
    
    返回:
    无
    """
    print(f"Running script: {script_path}")
    try:
        # 动态加载脚本
        spec = importlib.util.spec_from_file_location("module.name", script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # 假设每个脚本都有一个"main"的函数
        if hasattr(module, 'main'):
            module.main()
        else:
            print(f"Script {script_path} does not have a main function.")
    except Exception as e:
        print(f"Error running script {script_path}: {e}")
        # 生成报告
        report_dir = os.path.join(os.path.dirname(script_path), "report")
        os.makedirs(report_dir, exist_ok=True)
        report_path = os.path.join(report_dir, f"{os.path.basename(script_path)}.html")
        simple_report(script_path, logpath=report_dir, logfile=report_path)
        print(f"Report generated at: {report_path}")
    except Exception as e:
        print(f"Error running script {script_path}: {e}")


def parse_args():
    """
    解析命令行参数并返回解析结果。 
 
    该函数初始化一个参数解析器，添加所需的命令行参数， 
    并返回解析后的参数。它用于处理命令行参数 
    按指定顺序运行Airtest脚本。 
 
    返回: 
    命名空间（Namespace）：一个包含已解析命令行参数的对象。
    """
    #使用描述初始化参数解析器
    parser = argparse.ArgumentParser(description="Run Airtest scripts in specified order")

    #为连接的设备ID添加一个必需的参数
    parser.add_argument("device_id", help="Device ID to connect")

    #为有序运行的脚本列表添加一个必需的参数
    # nargs="+"表示此参数可以接受一个或多个值
    parser.add_argument("scripts", nargs="+", help="List of scripts to run in order")
    #解析添加的参数并返回解析后的结果
    return parser.parse_args()


def main():
    """
    主函数，按顺序运行所有脚本
    本函数首先解析命令行参数，获取设备ID和脚本列表
    然后尝试连接到指定设备，如果连接成功，则依次执行脚本列表中的每个脚本
    """
    # 解析命令行参数
    args = parse_args()
    # 获取设备ID
    DEVICE_ID = args.device_id
    # 获取脚本列表
    SCRIPTS = args.scripts

    # 尝试连接到设备，如果连接失败，则终止后续操作
    if not connect_to_device(DEVICE_ID):
        return

    # 依次执行脚本列表中的每个脚本
    for script in SCRIPTS:
        run_script(script)


if __name__ == "__main__":
    main()


