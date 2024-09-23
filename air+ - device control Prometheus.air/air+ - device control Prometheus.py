# -*- encoding=utf8 -*-
__author__ = "xfdzl"

from airtest.core.api import *



from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


auto_setup(__file__)


#prometheus设备的配网过程参考另外的脚本
#这里只做功能和逻辑验证。



















