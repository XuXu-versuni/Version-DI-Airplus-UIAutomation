# -*- encoding=utf8 -*-
__author__ = "xuxu"

import os
import importlib.util
from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)



from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

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