# -*- coding: utf-8 -*-
"""
Python 流程控制
===============

包含条件语句、循环、break/continue/else 等。
"""

# ==================== if 条件语句 ====================

# 基本语法
age = 18

if age >= 18:
    print("成年人")
elif age >= 13:
    print("青少年")
else:
    print("儿童")

# 单行 if (三元表达式)
status = "成年" if age >= 18 else "未成年"

# 多个条件
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# ==================== 循环 ====================

# for 循环 - 遍历序列
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# 使用 range()
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):        # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 3):    # 0, 3, 6, 9 (步长为 3)
    print(i)

# 遍历字典
person = {"name": "Alice", "age": 25, "city": "Beijing"}

for key in person:           # 遍历键
    print(key)

for value in person.values():  # 遍历值
    print(value)

for key, value in person.items():  # 遍历键值对
    print(f"{key}: {value}")

# while 循环
count = 0

while count < 5:
    print(count)
    count += 1

# ==================== break 和 continue ====================

# break - 跳出循环
for i in range(10):
    if i == 5:
        break           # 找到 5 就停止
    print(i, end=" ")   # 输出: 0 1 2 3 4

print()

# continue - 跳过当前迭代
for i in range(5):
    if i == 2:
        continue        # 跳过 2
    print(i, end=" ")   # 输出: 0 1 3 4

print()

# ==================== else 子句 ====================

# 循环的 else: 循环正常结束时执行 (不是 break 退出时)
for i in range(5):
    print(i)
else:
    print("循环正常结束")

# 配合 break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("不会执行，因为被 break 了")

# ==================== 嵌套循环 ====================

for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()

# ==================== 列表推导式 ====================

# 基本语法
squares = [x**2 for x in range(5)]
print(squares)          # [0, 1, 4, 9, 16]

# 带条件
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)     # [0, 4, 16, 36, 64]

# 嵌套列表推导式
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)          # [[0,0,0], [0,1,2], [0,2,4]]

# ==================== pass 语句 ====================

# 空代码块需要 pass 占位
if True:
    pass               # 什么都不做

for i in range(10):
    pass               # 以后再实现

# ==================== enumerate 函数 ====================

# 同时获取索引和值
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# ==================== zip 函数 ====================

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name}: {age}")

# ==================== 迭代器解包 ====================

# 解包赋值
a, b, c = [1, 2, 3]
print(a, b, c)          # 1 2 3

# 使用 * 解包剩余元素
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)   # 1 [2, 3, 4] 5

# 使用 * 解包可迭代对象
print(*[1, 2, 3])       # 1 2 3
