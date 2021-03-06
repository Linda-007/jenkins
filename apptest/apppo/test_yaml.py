
# python 自带的日志收集模块
import logging

import yaml

logging.basicConfig(level=logging.INFO,
                    filename='yaml.log',
                    filemode='a',
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    force = True)


def test_yaml():
    logging.info("test_yaml")

    pythonobj = {
        'desirecaps': {'platformName': 'android', 'deviceName': 'SJE0217909002069', 'appPackage': 'com.tencent.wework',
                       'appActivity': '.launch.LaunchSplashActivity', 'noReset': 'true',
                       'skipServerInstallation': 'true',
                       'skipDeviceInitialization': 'true'}, 'server': {'ip': '127.0.0.1', 'port': 4723}}
    print(yaml.safe_dump(pythonobj))
    logging.info(yaml.safe_dump(pythonobj))
