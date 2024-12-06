# -*- encoding=utf8 -*-
__author__ = "XXu"

from airtest.core.api import *
from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device

poco = AndroidUiautomationPoco(use_airtest_input= True,screenshot_each_action = False)
auto_setup(__file__)


#在测试oneid 时候，先注意
#这里根据需求设定，和具体Android实现，“打开app时候根据系统选择的语言”来展示显示还是不显示account这个function
#这里如果用汉字用以下脚本
# screen1 = Template(r"tpl1719470620506.png", record_pos=(-0.254, 0.006), resolution=(1080, 2340))
# screen2 = Template(r"tpl1719543010106.png", record_pos=(-0.071, -0.363), resolution=(1080, 2340))

# assert_exists(screen1,"判断oneid的Philips Account 是不是在切换指定逻辑区域之后存在")
# try:
#     assert_exists(screen2,"oneid的Philips Account 在切换指定逻辑区域之后存在")
# except Exception as b1:
#     print(str(b1))
# assert_not_exists(screen1,"检查unicorn设备开关状态没有影响其他button")

#如果系统是英语或者其他语言，用以下脚本
screen1 = Template(r"tpl1719470620506.png", record_pos=(-0.254, 0.006), resolution=(1080, 2340))
screen2 =  Template(r"tpl1719471510088.png", threshold = 1,record_pos=(-0.052, -0.267), resolution=(1080, 2340))

assert_exists(screen1,"判断oneid的Philips Account 是不是在切换指定逻辑区域之后存在。")
try:
    assert_exists(screen1,"oneid的Philips Account 在切换指定逻辑区域之后存在，结果正确！")
except Exception as b2:
                  print(str(b2))
assert_not_exists(screen2,"oneid的Philips Account 在切换指定逻辑区域之后不存在，结果正确！")

poco("com.philips.ph.homecare:id/settings_philips_account_id").click()
poco(text("Account Log-in ")).click()
sleep(1.0)
poco("com.philips.ph.homecare:id/user_philips_login_btn").click()
sleep(3.0)


# #没有账号，注册一个
# poco("android.widget.EditText").click()
# text("xu.xu@versuni.com")
# #这个时候要手动输入注册邮箱收到的验证码
# #比如
# text("861674")
# poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.FrameLayout").offspring("com.android.chrome:id/compositor_view_holder").offspring("android.webkit.WebView")[1].child("android.view.View")[0].child("android.view.View")[2].click()
# sleep(2.0)


#使用刚注册号的账号登录
#这里的流程走Flow 4：Sign out的branch,上面的shell要注释掉
#这里的功能也可以不用跑，要调用另外一个“air+ - email”的shell，但是目前outlook的认证需要Authenticator来认证，麻烦
# poco(text="Continue with e-mail").click()
# #poco('ssion').get_text()
# text("592108")
# sleep(1.0)
# poco(focused="True").click()



#可以查看readmore的连接文档是否正常，
#测试环境无法测试，因为homeid的二级域名是acc.accounts.home.id的,正式环境是account.home.id的域名。
#poco("Read more").click()
#sleep(3.0)

#有谷歌账号
try:
    poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.FrameLayout").offspring("com.android.chrome:id/compositor_view_holder").offspring("android.webkit.WebView")[1].child("android.view.View")[0].child("android.view.View")[1].child("android.view.View")[2].click()
except:
    poco(text="Switch to other account").click()
try:    
    poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.FrameLayout").offspring("com.android.chrome:id/compositor_view_holder").offspring("android.webkit.WebView")[1].child("android.view.View")[0].child("android.view.View")[2].child("android.view.View")[0].click()
except:
    poco(text="Google Continue with Google").click()
sleep(10.0)    
poco("com.android.chrome:id/account_picker_continue_as_button").click()
sleep(2.0)
try:
    poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.FrameLayout").offspring("com.android.chrome:id/compositor_view_holder").offspring("android.webkit.WebView")[1].child("android.view.View").child("android.view.View")[0].child("android.view.View")[2].child("android.view.View").offspring("android.widget.ListView").child("android.view.View")[0]

except:
    poco("xu xu xuxuversuni@gmail.com").click()
sleep(1.0)
try:
    poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.FrameLayout").offspring("com.android.chrome:id/compositor_view_holder").offspring("android.webkit.WebView")[1].child("android.view.View")[0].child("android.view.View").child("android.view.View")[3].click()
except:
    poco(text="Continue").click()

sleep(3.0)


poco(text="Subscribe").click()
sleep(3.0)

assert_exists(Template(r"tpl1719822548987.png", record_pos=(-0.27, -0.712), resolution=(1080, 2340)),"页面显示正常！")

swipe([500,1700],[500,700])
swipe([500,1700],[500,700])
try:
    touch(Template(r"tpl1719822734374.png", record_pos=(-0.453, -0.901), resolution=(1080, 2340)))
except:
    poco("com.android.chrome:id/close_button").click()
poco("Navigate up").click()

#这里要注意登录完毕之后，要sign out一下，不然会报错，以上逻辑走不到

#自此整个oneid的页面功能验证完毕。



#有facebook账号
#留作业，做出facebook的登录逻辑和苹果账号的逻辑


#有苹果账号













