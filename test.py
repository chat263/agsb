#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import threading
import signal
from pathlib import Path
import requests
from datetime import datetime

# 配置
TMATE_URL = "https://github.com/zhumengkang/agsb/raw/main/tmate"
UPLOAD_API = "https://file.zmkk.fun/api/upload"
USER_HOME = Path.home()
SSH_INFO_FILE = "ssh.txt"  # 可以自定义文件名

def main():
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
  
