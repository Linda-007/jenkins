import os
import signal
import subprocess

import pytest

from UIframework.page.logger import log_init


@pytest.fixture(scope="module",autouse=True)
def record():
    log_init()
    #用例运行前做一些事情
    #os.system('chcp 65001')
    cmd ="scrcpy -Nr tmp.mp4"
    p = subprocess.Popen(cmd,shell=True)
    yield
    #用例运行后做一些事情
    os.kill(p.pid,signal.CTRL_C_EVENT)