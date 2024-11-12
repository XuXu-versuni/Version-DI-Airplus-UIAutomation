# -*- encoding=utf8 -*-
__author__ = "xuxu"

import os
import importlib.util
from airtest.core.api import *
from airtest.cli.parser import cli_setup


# # 如果cli_setup函数返回False，则表明CLI环境未正确设置，需要进行自动设置
# if not cli_setup():
#     # 调用auto_setup函数，使用当前文件路径进行设置，并指定日志目录和设备连接信息
#     auto_setup(__file__, logdir=True, devices=["Android://127.0.0.1:5037",])
    
# 脚本从这里开始执行，表示程序的开始
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco



if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android://127.0.0.1:5037",])

    
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

        spec = importlib.util.spec_from_file_location("module.name", script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, 'main'):
            module.main()
        else:
            print(f"Script {script_path} does not have a main function.")
    except Exception as e:
        print(f"Error running script {script_path}: {e}")

def main():
    for script in SCRIPTS:
        run_script(script)


if __name__ == "__main__":
    main()