# -*- coding: utf-8 -*-
"""
Python 模块与导入
================

import、from...import、相对导入、包管理等。
"""

# ==================== 基本导入 ====================

import os
import sys
import math

# 使用模块中的内容
print(os.getcwd())
print(sys.path)
print(math.pi)

# ==================== from...import ====================

from os import getcwd, chdir
print(getcwd())

# 导入所有 (不推荐)
from math import *
print(pi)
print(sin(0))

# 使用别名
import numpy as np
import pandas as pd
from datetime import datetime as dt

# ==================== 导入顺序 ====================

# 1. 标准库
import os
import sys
from collections import defaultdict

# 2. 第三方库
import requests
from flask import Flask

# 3. 本地应用/库
from mymodule import MyClass

# 每组之间空一行

# ==================== 模块的 __name__ ====================

# 当模块直接运行时，__name__ == "__main__"
# 当模块被导入时，__name__ == 模块名

# if __name__ == "__main__":
#     # 只有直接运行此文件时才执行
#     main()

# ==================== 包 (Package) ====================

# mypackage/
#     __init__.py      # 包初始化文件
#     module1.py       # 模块文件
#     module2.py
#     subpackage/
#         __init__.py
#         module3.py

# ==================== 相对导入 ====================

# 在包内使用相对导入
# from . import module1          # 导入同一包中的模块
# from .. import parent_module   # 导入上级包中的模块
# from ..subpackage import module3

# 注意: 相对导入不能在主模块 (直接运行的 .py 文件) 中使用

# ==================== 重新加载模块 ====================

import importlib
import mymodule

importlib.reload(mymodule)   # 重新加载，调试时有用

# ==================== 模块搜索路径 ====================

import sys
print(sys.path)    # 当前目录 -> PYTHONPATH -> 安装目录

# 添加搜索路径
sys.path.append("/path/to/my/modules")

# ==================== 查看模块内容 ====================

import math

print(dir(math))             # 所有属性和方法
print(math.__name__)         # "math"
print(math.__file__)         # 模块文件路径
print(math.__doc__)          # 文档字符串

# ==================== 常用标准库 ====================

# os - 操作系统接口
import os
os.listdir(".")
os.mkdir("newdir")
os.remove("file.txt")
os.path.join("dir", "file")

# sys - 系统相关
import sys
sys.argv              # 命令行参数
sys.exit(0)          # 退出程序

# collections - 容器数据类型
from collections import Counter, defaultdict, OrderedDict
Counter("abracadabra")    # 计数器
defaultdict(list)         # 默认值字典

# datetime - 日期时间
from datetime import datetime, date, time, timedelta
dt = datetime.now()
print(dt.strftime("%Y-%m-%d %H:%M:%S"))

# json - JSON 处理
import json
json.dumps({"a": 1})           # dict -> JSON 字符串
json.loads('{"a": 1}')          # JSON 字符串 -> dict

# re - 正则表达式
import re
re.match(r"\d+", "123abc")
re.findall(r"\d+", "a1b2c3")

# itertools - 迭代器工具
import itertools
list(itertools.chain([1, 2], [3, 4]))   # [1, 2, 3, 4]
list(itertools.product([1, 2], [3, 4])) # 笛卡尔积

# functools - 高阶函数
from functools import reduce, lru_cache
@lru_cache(maxsize=100)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

# ==================== __all__ 变量 ====================

# 在模块中定义 __all__ 控制 from module import * 的行为
# __all__ = ['func1', 'Class1']  # 只导出这两个

# ==================== 主模块概念 ====================

# 每个 .py 文件都是一个模块
# 主模块 (入口) 是你直接运行的第一个文件
# 主模块的 __name__ 永远是 "__main__"

# if __name__ == "__main__":
#     main()
