# -*- coding: utf-8 -*-
"""
Python 运算符
=============

包含算术、比较、逻辑、位运算等。
"""

# ==================== 算术运算符 ====================

a, b = 10, 3

print(a + b)    # 13  加法
print(a - b)    # 7   减法
print(a * b)    # 30  乘法
print(a / b)    # 3.333...  除法 (总是浮点数)
print(a // b)   # 3   整除
print(a % b)    # 1   取余
print(a ** b)   # 1000  幂运算 (10^3)

# 增强赋值
x = 5
x += 3          # x = x + 3 = 8
x -= 2          # x = x - 2 = 6
x *= 4          # x = x * 4 = 24
x /= 6          # x = x / 6 = 4.0
x //= 2         # x = x // 2 = 2.0

# ==================== 比较运算符 ====================

print(10 > 5)       # True
print(10 < 5)       # False
print(10 >= 10)     # True
print(10 <= 9)      # False
print(10 == 10)     # True  (等于)
print(10 != 5)      # True  (不等于)

# 链式比较 (Python 特有)
print(1 < 2 < 3)               # True
print(1 < 2 > 1)               # True
print(0 < x < 10)              # 判断 x 是否在 0-10 之间

# 字符串比较
print("apple" < "banana")      # True (按字母顺序)
print("Hello" == "hello")      # False (区分大小写)

# ==================== 逻辑运算符 ====================

# and, or, not
print(True and False)     # False
print(True or False)      # True
print(not True)            # False

# 短路求值
# a and b: 如果 a 为 False，直接返回 a，否则返回 b
# a or b:  如果 a 为 True，直接返回 a，否则返回 b

result = None or "default"     # "default"
result = "first" or "second"   # "first"

# ==================== 身份运算符 ====================

# is 和 is not 用于判断是否是同一个对象 (内存地址)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)     # True  (值相等)
print(a is b)     # False (不是同一对象)
print(a is c)     # True  (是同一对象)

# is 主要用于和 None 比较
if x is None:
    print("x 是 None")
if x is not None:
    print("x 不是 None")

# ==================== 成员运算符 ====================

# in 和 not in
numbers = [1, 2, 3, 4, 5]

print(3 in numbers)         # True
print(10 not in numbers)     # True

# 字符串包含
print("py" in "python")      # True
print("java" in "python")   # False

# 字典: 检查键
person = {"name": "Alice", "age": 25}
print("name" in person)      # True
print("Alice" in person)     # False (检查的是键，不是值)

# ==================== 位运算符 ====================

# 用于整数，按二进制位操作
a, b = 5, 3    # 5=101, 3=011

print(a & b)   # 1   (001)  按位与
print(a | b)   # 7   (111)  按位或
print(a ^ b)   # 6   (110)  按位异或
print(~a)      # -6  按位取反
print(a << 1)  # 10  左移 1 位 (乘以 2)
print(a >> 1)  # 2   右移 1 位 (除以 2)

# ==================== 运算符优先级 ====================

# 从高到低: () > ** > 正负号 > */%// > +- > << >> > & > ^ > | > 比较 > not > and > or

# 示例
result = 2 + 3 * 4           # 14 (先乘后加)
result = (2 + 3) * 4        # 20 (先加后乘)
result = 2 ** 3 ** 2         # 512 (右结合, 2**(3**2))
