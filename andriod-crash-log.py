# -*- coding: utf-8 -*-
"""
#  author: xfdzl                                          #
#  @Time:2024/7/10 上午1:06                               #
"""
'''
/**
 *                             _ooOoo_
 *                            o8888888o
 *                            88" . "88
 *                            (| -_- |)
 *                            O\  =  /O
 *                         ____/`---'\____
 *                       .'  \\|     |//  `.
 *                      /  \\|||  :  |||//  \
 *                     /  _||||| -:- |||||-  \
 *                     |   | \\\  -  /// |   |
 *                     | \_|  ''\---/''  |   |
 *                     \  .-\__  `-`  ___/-. /
 *                   ___`. .'  /--.--\  `. . __
 *                ."" '<  `.___\_<|>_/___.'  >'"".
 *               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
 *               \  \ `-.   \_ __\ /__ _/   .-` /  /
 *          ======`-.____`-.___\_____/___.-`____.-'======
 *                             `=---='
 *          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 *                     佛祖保佑        永无BUG
 *            佛曰:
 *                   写字楼里写字间，写字间里程序员；
 *                   程序人员写程序，又拿程序换酒钱。
 *                   酒醒只在网上坐，酒醉还来网下眠；
 *                   酒醉酒醒日复日，网上网下年复年。
 *                   但愿老死电脑间，不愿鞠躬老板前；
 *                   奔驰宝马贵者趣，公交自行程序员。
 *                   别人笑我忒疯癫，我笑自己命太贱；
 *                   不见满街漂亮妹，哪个归得程序员？
*/




'''

import subprocess
import os
import time


# 本脚本适用于mac系统，以及配置文件以macos为基础。

def find_adb():
	# Check common installation paths for adb
	possible_paths = [
		# 以下是macos的配置选项
		# '/usr/local/bin/adb',
		# '/usr/bin/adb',
		# '~/Library/Android/sdk/platform-tools/adb',  # Adjust this path based on your Android SDK installation
		# '~/Android/sdk/platform-tools/adb'  # Additional path commonly used

		# 以下是win系统的配置选项，二者只能选其一
		'C:/platform-tools/adb.exe'
	]

	for path in possible_paths:
		expanded_path = os.path.expanduser(path)
		if os.path.isfile(expanded_path):
			return expanded_path

	return None


def connect_to_device(adb_path):
	# Check if adb is accessible
	if not adb_path or not os.path.isfile(adb_path):
		print("adb not found. Please install Android SDK Platform Tools呀.")
		return False

	# Connect to the device
	connect_cmd = [adb_path, 'devices']
	devices_output = subprocess.check_output(connect_cmd).decode('utf-8').strip().split('\n')

	if len(devices_output) < 2:
		print("No devices connected.")
		return False

	# Assuming the first device in the list is the one we want to connect to
	device_info = devices_output[1].split('\t')
	device_id = device_info[0]
	print(f"Connecting to device: {device_id}")

	# Check if device is unauthorized
	if 'unauthorized' in device_info[1]:
		print("Device is unauthorized. Please check your device and authorize the connection.")
		return False

	return device_id


def capture_crash_logs(device_id, package_name, adb_path):
	# Create a directory to store logs
	log_dir = 'android_logs'
	if not os.path.exists(log_dir):
		os.makedirs(log_dir)

	# Get current time for log file naming
	current_time = time.strftime("%Y%m%d-%H%M%S")
	log_file = os.path.join(log_dir, f'crash_logs_{current_time}.txt')

	# Command to capture logs
	log_cmd = [adb_path, '-s', device_id, 'logcat', '-d', '-b', 'crash']

	# Run adb command to get logs
	try:
		with open(log_file, 'w') as f:
			subprocess.run(log_cmd, stdout=f, stderr=subprocess.PIPE, check=True)
		print(f"Crash logs saved to: {log_file}")
	except subprocess.CalledProcessError as e:
		print(f"Error capturing crash logs: {e}")


if __name__ == "__main__":
	adb_path = find_adb()
	if not adb_path:
		print(
			"…………………………………&&&&&&&&&&&&&&&&&………………………………………………\n\nadb not found. \nPlease install Android SDK Platform Tools\n啊，完蛋了，\n你这里跑不去了，\n赶紧来拜我！！！ \n\n…………………………………&&&&&&&&&&&&&&&&&………………………………………………")
	#                      _ooOoo_
	#                      o8888888o
	#                      88" . "88
	#                      (| ^_^ |)
	#                      O\  =  /O
	#                   ____/`---'\____
	#                 .'  \\|     |//  `.
	#                /  \\|||  :  |||//  \
	#               /  _||||| -:- |||||-  \
	#               |   | \\\  -  /// |   |
	#               | \_|  ''\---/''  |   |
	#               \  .-\__  `-`  ___/-. /
	#             ___`. .'  /--.--\  `. . ___
	#           ."" '<  `.___\_<|>_/___.'  >'"".
	#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
	#         \  \ `-.   \_ __\ /__ _/   .-` /  /
	#   ========`-.____`-.___\_____/___.-`____.-'========
	#                        `=---='
	#   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	#      佛祖保佑       永无BUG     永不修改")
	else:
		device_id = connect_to_device(adb_path)
		if device_id:
			package_name = "com.philips.ph.homecare"
			capture_crash_logs(device_id, package_name, adb_path)
