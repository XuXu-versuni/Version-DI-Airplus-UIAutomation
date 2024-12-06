# -*- coding: utf-8 -*-  
""" 
@time :    2024/10/15  0:02 
@File:     APP_update.py 
@Software: PyCharm 
@Author :  xfdzl 
@Version:  python3.7 
"""  
#import sys
import os  
import subprocess  
import time  
#reload (sys)
#sys.setdefaultencoding('utf-8')
  
def run_adb_command(command):
    """
    运行ADB命令并返回输出
    参数:
    command (str): 要执行的ADB命令字符串
    返回:
    str: ADB命令的输出结果
    异常:
    当ADB命令执行失败时抛出Exception异常
    """
    # 使用subprocess.run执行ADB命令
    # 该方法允许我们捕获命令的输出并对其进行处理
    # 这里使用了多个参数配置来确保能够正确执行命令并捕获输出
    result = subprocess.run(['command'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,encoding='utf-8',shell=True)
    
    # 检查命令是否执行成功
    # 如果执行失败（返回码不为0），则抛出异常并包含错误信息
    if result.returncode != 0:
        raise Exception(f"ADB 命令 失效: {result.stderr}")
    # if result.returncode != 0:
    #     raise.Exception(f"ADB command failed: {result.stderr}")")
    
    # 如果执行成功，则返回命令的输出结果
    return result.stdout
def install_apk_from_local(apk_path, package_name):
    """
    从本地路径安装APK
    参数:
        apk_path (str): APK文件的本地路径
        package_name (str): 要安装的应用的包名

    参数 Raises:
        FileNotFoundError: 如果指定路径的APK文件不存在
    """
    # 检查APK文件是否存在
    if not os.path.isfile(apk_path):
        raise FileNotFoundError(f"APK 文件 {apk_path} 不存在.")

    # 输出安装信息
    print(f"Installing {apk_path}...")
    # 执行ADB命令安装APK
    run_adb_command(f'adb install -r "{apk_path}"')
    # 输出安装成功信息
    print(f"Successfully installed {package_name}")
  
def check_app_functionality(package_name):  
    """检查应用功能"""  
    print("检查应用功能/Checking app functionality...")  
    # 这里可以添加更多的功能检查，例如：  
    # 1. 检查特定界面是否加载成功  
    # 2. 检查数据是否正确显示  
    # 3. 检查网络请求是否成功  
  

    # 检查应用主界面是否加载成功  
    output = run_adb_command('adb shell dumpsys activity')  
    if f"mFocusedActivity={package_name}" in output:  
        print("检查应用主界面是否加载成功/Main activity is focused, app seems to be working.")  
    else:  
        print("Main activity is not focused, there might be an issue.")  
  

def check_data_integrity(package_name):  
    """检查数据完整性"""  
    print("检查历史数据库/Checking data integrity...")  
    # 这里可以添加具体的检查逻辑，例如：  
    # 1. 检查数据库中的数据是否完整  
    # 2. 检查用户设置是否保留  
  
    # 检查用户设置是否保留  
    output = run_adb_command(f'adb shell pm dump {package_name}')  
    if "User data directory" in output:  
        print("检查用户设置是否保留/User data directory exists, data seems to be intact.")  
    else:  
        print("检查用户设置数据丢失/User data directory not found, data might be lost.")  
  
  
#这里的path修改成你们本地的apk存放路径  
def main():  
    apk_path = r'/Users/xuxu/Downloads/Philips Air+_3.11.0_APKPure.apk'  
    package_name = 'com.philips.ph.homecare'  
  
    try:  
        # 安装APK  
        install_apk_from_local(apk_path, package_name)  
  
        # 启动应用  
        launch_app(package_name)  
  
        # 检查应用功能  
        check_app_functionality(package_name)  
  
        # 检查数据完整性  
        check_data_integrity(package_name)  
  
        print("目标检查通过/All checks passed successfully.")  
    except Exception as e:  
        print(f"An error occurred: {e}")  
  
  
if __name__ == "__main__":   
    main()

