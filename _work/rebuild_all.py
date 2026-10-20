#!/usr/bin/env python3
"""（旧入口）等价于 `python3 一键重建.py`。保留此文件以免旧命令失效。
重建请用：python3 一键重建.py [归档名...]   （--list 列出归档名，--check 仅核验）
"""
import os, runpy, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(os.path.dirname(HERE), '一键重建.py')
sys.argv = [TARGET] + sys.argv[1:]
runpy.run_path(TARGET, run_name='__main__')
