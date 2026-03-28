# -*- coding: utf-8 -*-
"""
Python 变量与数据类型
=====================

Python 是动态类型语言，无需声明变量类型，直接赋值即可。
"""

# ==================== 变量基础 ====================

# 基本赋值
name = "Alice"          # 字符串
age = 25                # 整数
height = 1.68           # 浮点数
is_student = True       # 布尔值

# 多个变量同时赋值
x, y, z = 1, 2, 3

# 同一值赋给多个变量
a = b = c = 0

# ==================== 数据类型 ====================

# 整数 (int)
count = 42
negative = -10
hex_num = 0xFF          # 十六进制 (255)
binary = 0b1010        # 二进制 (10)

# 浮点数 (float)
price = 19.99
scientific = 1.5e-3    # 科学计数法 (0.0015)

# 复数 (complex)
complex_num = 3 + 4j

# 字符串 (str)
single = 'hello'
double = "world"
multi = """这是
多行字符串"""

# 原始字符串 (不转义)
path = r"C:\newfolder\file.txt"

# ==================== 类型转换 ====================

num_str = "123"
num_int = int(num_str)           # 字符串 -> 整数
num_float = float(num_str)       # 字符串 -> 浮点数
back_to_str = str(123)           # 整数 -> 字符串

# 强制转换
bool(1)          # True
bool(0)          # False
bool("")         # False
bool(None)       # False

# ==================== 类型查看 ====================

type(123)                # <class 'int'>
type(3.14)              # <class 'float'>
type("hello")           # <class 'str'>

# 类型检查
isinstance(123, int)    # True
isinstance("abc", str)  # True

# ==================== 变量命名规范 ====================

# 变量名只能包含字母、数字、下划线，不能以数字开头
valid_name = "ok"
_name = "ok"
name2 = "ok"

# 常用命名风格
snake_case = "variable_name"     # Python 推荐
camelCase = "variableName"        # 不推荐
CONSTANT_VALUE = 100             # 常量约定

# 不能使用的名字 (关键字)
# class = 1     # 错误！
# if = 2        # 错误！

# ==================== None 类型 ====================

empty = None          # 表示空值
result = None

# 判断 None
if empty is None:
    print("变量为空")

# ==================== 布尔运算 ====================

# False 值: 0, 0.0, "", [], {}, None, False
# True 值: 其他所有值

# 短路运算
a = True and print("yes")   # 会执行 print
b = False and print("no")  # 不会执行
c = True or print("maybe")  # 不会执行
d = False or print("yes")   # 会执行 print
