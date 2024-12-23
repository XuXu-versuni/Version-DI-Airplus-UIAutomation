# # -*- encoding=utf8 -*-
# __author__ = "XXu"

# from airtest.core.api import *
# from poco.proxy import UIObjectProxy
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# from airtest.core.api import device
# poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
# auto_setup(__file__)

# # # #如果不需要多台机器联合测试，就可以使用#在代码的最前面给代码屏蔽掉
# # # #设置多机联合执行验证
# # dev1 = connect_device("Android://127.0.0.1:5037/103cdef4")  # 第一台手机，103cdef4是指设备序列号
# # dev2 = connect_device("Android://127.0.0.1:5037/R58N12E57DV")  # 第二台手机
# # print(G.DEVICE_LIST)
# # set_current("103cdef4")

# #底部“文章”

# poco("com.philips.ph.homecare:id/navigation_articles").click()
# sleep(3.0)
# swipe([536,2000],[536,1000])
# swipe([536,1000],[536,2000])
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/articles_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[0].swipe([-0.4325, 0.0279])
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/articles_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[0].swipe([0.4325, 0.0279])

# poco(text="建议").click()
# poco(text="总体").click()
# poco(text="病毒").click()
# # sleep(2.0)
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/articles_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[2].click()
# sleep(1.0)
# poco("com.android.systemui:id/back").click()
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/navigation_articles").offspring("com.philips.ph.homecare:id/navigation_bar_item_icon_view").click()


# #多机的第二部手机
# set_current("R58N12E57DV")
# poco("com.philips.ph.homecare:id/navigation_articles").click()
# sleep(3.0)

# swipe([536,2000],[536,1000])
# swipe([536,1000],[536,2000])
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/articles_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[0].swipe([-0.4325, 0.0279])
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/articles_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[0].swipe([0.4325, 0.0279])
# poco(text="建议").click()
# poco(text="总体").click()
# poco(text="病毒").click()
# sleep(3.0)
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/articles_refresh_id").child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[2].click()
# sleep(1.0)
# poco("com.android.systemui:id/back").click()
# poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring("com.philips.ph.homecare:id/navigation_articles").offspring("com.philips.ph.homecare:id/navigation_bar_item_icon_view").click()


#以上是poco写法
#一下是python语法构建脚本


# import time
# from airtest.core.api import connect_device, sleep, swipe
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# # 初始化 Poco 对象
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# # 点击底部“文章”按钮
# def click_articles_button():
#     poco("com.philips.ph.homecare:id/navigation_articles").click()
#     time.sleep(3)

# # 执行上下滑动

# def perform_swipe():
#     swipe([536, 2000], [536, 1000])  # 向下滑动
#     swipe([536, 1000], [536, 2000])  # 向上滑动

# # 左右滑动

# def perform_horizontal_swipe():
#     article_element = poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring(
#         "com.philips.ph.homecare:id/articles_refresh_id"
#     ).child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[0]
#     article_element.swipe([-0.4325, 0.0279])  # 向左滑动
#     article_element.swipe([0.4325, 0.0279])   # 向右滑动

# # 点击“建议”、“总体”、“病毒”
# def click_suggestions():
#     poco(text="建议").click()
#     poco(text="总体").click()
#     poco(text="病毒").click()
#     time.sleep(2)

# # 点击特定文章并返回
# def click_article_and_go_back():
#     poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring(
#         "com.philips.ph.homecare:id/articles_refresh_id"
#     ).child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[2].click()
#     time.sleep(1)
#     poco("com.android.systemui:id/back").click()

# # 再次点击底部“文章”按钮
# def click_articles_icon():
#     poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring(
#         "com.philips.ph.homecare:id/navigation_articles"").offspring("com.philips.ph.homecare:id/navigation_bar_item_icon_view").click()

# # 执行所有步骤
# def main():
#     click_articles_button()
#     perform_swipe()
#     perform_horizontal_swipe()
#     click_suggestions()
#     click_article_and_go_back()
#     click_articles_icon()

# if __name__ == "__main__":
#     main()




import time
from openpyxl import Workbook
from airtest.core.api import connect_device, sleep, swipe
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# 初始化 Poco 对象
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 初始化测试结果列表
test_results = []

# 点击底部“文章”按钮
def click_articles_button():
    try:
        poco("com.philips.ph.homecare:id/navigation_articles").click()
        time.sleep(3)
        test_results.append({"Step": "Click Articles Button", "Status": "Pass"})
    except Exception as e:
        test_results.append({"Step": "Click Articles Button", "Status": f"Fail: {e}"})

# 执行上下滑动
def perform_swipe():
    try:
        swipe([536, 2000], [536, 1000])  # 向下滑动
        swipe([536, 1000], [536, 2000])  # 向上滑动
        test_results.append({"Step": "Perform Swipe", "Status": "Pass"})
    except Exception as e:
        test_results.append({"Step": "Perform Swipe", "Status": f"Fail: {e}"})

# 左右滑动
def perform_horizontal_swipe():
    try:
        article_element = poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring(
            "com.philips.ph.homecare:id/articles_refresh_id"
        ).child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[0]
        article_element.swipe([-0.4325, 0.0279])  # 向左滑动
        article_element.swipe([0.4325, 0.0279])   # 向右滑动
        test_results.append({"Step": "Perform Horizontal Swipe", "Status": "Pass"})
    except Exception as e:
        test_results.append({"Step": "Perform Horizontal Swipe", "Status": f"Fail: {e}"})

# 点击“建议”、“总体”、“病毒”
def click_suggestions():
    try:
        poco(text="建议").click()
        poco(text="总体").click()
        poco(text="病毒").click()
        time.sleep(2)
        test_results.append({"Step": "Click Suggestions", "Status": "Pass"})
    except Exception as e:
        test_results.append({"Step": "Click Suggestions", "Status": f"Fail: {e}"})

# 点击特定文章并返回
def click_article_and_go_back():
    try:
        poco("android.widget.FrameLayout").child("android.widget.FrameLayout").offspring(
            "com.philips.ph.homecare:id/articles_refresh_id"
        ).child("android.webkit.WebView").child("android.webkit.WebView").child("android.view.View")[2].click()
        time.sleep(1)
        poco("com.android.systemui:id/back").click()
        test_results.append({"Step": "Click Article and Go Back", "Status": "Pass"})
    except Exception as e:
        test_results.append({"Step": "Click Article and Go Back", "Status": f"Fail: {e}"})

# 将测试结果写入 Excel
def export_results_to_excel(results, filename="test_results.xlsx"):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Test Results"

    # 写入表头
    sheet.append(["Step", "Status"])

    # 写入数据
    for result in results:
        sheet.append([result["Step"], result["Status"]])

    # 保存文件
    workbook.save(filename)
    print(f"Results saved to {filename}")

# 主函数
def main():
    click_articles_button()
    perform_swipe()
    perform_horizontal_swipe()
    click_suggestions()
    click_article_and_go_back()
    export_results_to_excel(test_results)

if __name__ == "__main__":
    main()

