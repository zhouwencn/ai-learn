# -*- coding: utf-8 -*-
"""
Python 字符串
=============

字符串操作、格式化、常用方法。
"""

# ==================== 字符串创建 ====================

s1 = '单引号'
s2 = "双引号"
s3 = """多行
字符串"""
s4 = '''也可以
这样'''

# 转义字符
path = "C:\\Users\\name"      # C:\Users\name
quote = "他说: \"你好\""       # 他说: "你好"
newline = "第一行\n第二行"

# 原始字符串
path = r"C:\newfolder\file"  # 不转义

# ==================== 字符串索引和切片 ====================

s = "Hello, World!"

print(s[0])        # H
print(s[-1])        # !
print(s[0:5])       # Hello
print(s[7:12])      # World
print(s[::2])       # Hlo ol! (步长 2)
print(s[::-1])      # !dlroW ,olleH (反转)

# ==================== 字符串格式化 ====================

name = "Alice"
age = 25

# f-string (Python 3.6+)
print(f"我叫{name}, 今年{age}岁")

# 表达式
print(f"明年{age + 1}岁")
print(f"{name}是{'成年人' if age >= 18 else '未成年人'}")

# 格式化选项
pi = 3.14159
print(f"π约等于{pi:.2f}")      # 3.14 (保留两位小数)
print(f"{pi:.2e}")             # 3.14e+00 (科学计数法)
print(f"{1000:,}")             # 1,000 (千位分隔符)

# format() 方法
template = "我叫{}, 今年{}岁"
print(template.format(name, age))

template = "我叫{0}, 今年{1}岁。{0}是好人"
print(template.format(name, age))

template = "我叫{name}, 今年{age}岁"
print(template.format(name=name, age=age))

# % 格式化 (旧式)
print("我叫%s, 今年%d岁" % (name, age))

# ==================== 字符串方法 ====================

s = "  Hello, World!  "

# 大小写
print(s.upper())              # 全部大写
print(s.lower())              # 全部小写
print(s.capitalize())         # 首字母大写
print(s.title())              # 每个单词首字母大写
print(s.swapcase())           # 大小写互换

# 去除空白
print(s.strip())              # 去除两端空白
print(s.lstrip())             # 去除左边空白
print(s.rstrip())             # 去除右边空白

# 查找和替换
s = "Hello, World!"
print(s.find("World"))        # 7 (位置)，找不到返回 -1
print(s.index("World"))       # 7 (位置)，找不到报错
print(s.count("l"))          # 3 (出现次数)
print(s.replace("World", "Python"))  # Hello, Python!

# 判断
s = "hello123"
print(s.isalpha())            # False (不全为字母)
print(s.isdigit())            # False (不全为数字)
print(s.isalnum())            # True (字母或数字)
print(s.islower())            # True
print(s.isupper())            # False
print(s.isspace())            # False
print(s.startswith("hello"))  # True
print(s.endswith("123"))      # True

# 分割和连接
s = "apple,banana,cherry"
print(s.split(","))           # ['apple', 'banana', 'cherry']
print(s.split(",", 1))        # ['apple', 'banana,cherry'] (限制次数)

lines = ["第一行", "第二行", "第三行"]
print("\n".join(lines))      # 用换行符连接

# 对齐
s = "hello"
print(s.ljust(10))           # 'hello     ' (左对齐)
print(s.rjust(10))           # '     hello' (右对齐)
print(s.center(10))          # '  hello   ' (居中)

# ==================== 字符串拼接 ====================

# 加号
s1 = "Hello" + " " + "World"

# join (推荐)
parts = ["Hello", "World"]
s = " ".join(parts)

# 重复
s = "abc" * 3                 # "abcabcabc"

# ==================== 字符串与其他类型转换 ====================

# 字符串转列表
s = "hello"
print(list(s))               # ['h', 'e', 'l', 'l', 'o']

# 字符串转数字
num = int("123")
num = float("3.14")

# 数字转字符串
s = str(123)

# bytes 和字符串
s = "hello"
b = s.encode("utf-8")        # 字符串 -> bytes
s = b.decode("utf-8")       # bytes -> 字符串

# ==================== 常用技巧 ====================

# 判断是否为空
s = ""
if s:                        # False
    pass
if not s:                    # True
    print("字符串为空")

# 字符串包含判断
if "hello" in "hello world":  # True

# 统计字符出现次数
s = "hello"
print(s.count("l"))          # 2

# 首字母大写，其余小写
s = "heLLo"
print(s.capitalize())        # Hello

# 去除重复字符 (保持顺序)
s = "abbacbd"
print("".join(dict.fromkeys(s)))  # "abcd"
