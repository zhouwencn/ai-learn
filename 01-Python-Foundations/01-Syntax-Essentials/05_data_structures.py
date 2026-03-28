# -*- coding: utf-8 -*-
"""
Python 数据结构
================

列表 (list)、元组 (tuple)、字典 (dict)、集合 (set)。
"""

# ==================== 列表 (list) ====================

# 创建
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []
initialized = [0] * 5           # [0, 0, 0, 0, 0]

# 索引和切片
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[0])       # 0   第一个元素
print(numbers[-1])      # 5   最后一个元素
print(numbers[1:4])     # [1, 2, 3]   切片
print(numbers[::2])     # [0, 2, 4]   步长为 2
print(numbers[::-1])    # [5, 4, 3, 2, 1, 0]   反转

# 修改
numbers[0] = 10         # 修改元素
numbers.append(6)       # 末尾添加
numbers.insert(0, -1)  # 指定位置插入
numbers.extend([7, 8])  # 扩展列表
numbers.remove(10)     # 删除第一个匹配的元素
popped = numbers.pop() # 弹出并返回最后一个元素
popped = numbers.pop(0) # 弹出指定位置的元素
numbers.clear()        # 清空列表

# 查找
numbers = [1, 2, 3, 2, 4]
print(numbers.index(2))     # 1   第一个匹配的位置
print(numbers.count(2))     # 2   出现的次数
print(3 in numbers)         # True   是否存在

# 排序和反转
numbers = [3, 1, 4, 1, 5]
numbers.sort()             # 原地排序
sorted_nums = sorted(numbers)  # 返回新列表
numbers.reverse()          # 原地反转

# ==================== 元组 (tuple) ====================

# 创建 (不可变)
point = (3, 4)
single = (42,)            # 单元素元组需要逗号
empty = ()

# 打包和解包
coordinates = (1, 2, 3)
x, y, z = coordinates     # 解包
print(x, y, z)            # 1 2 3

# 交换变量
a, b = 1, 2
a, b = b, a              # 无需临时变量

# 命名元组
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)          # 3 4

# ==================== 字典 (dict) ====================

# 创建
person = {"name": "Alice", "age": 25}
person = dict(name="Alice", age=25)
fromkeys = dict.fromkeys(['a', 'b', 'c'], 0)

# 访问
print(person["name"])            # Alice
print(person.get("name"))        # Alice
print(person.get("gender", "Unknown"))  # Unknown (默认值)

# 添加和修改
person["city"] = "Beijing"       # 添加新键值对
person["age"] = 26              # 修改已有键

# 删除
del person["city"]
popped = person.pop("age")       # 弹出并返回值
person.clear()                  # 清空

# 遍历
person = {"name": "Alice", "age": 25, "city": "Beijing"}
for key in person:              # 遍历键
    print(key)

for value in person.values():    # 遍历值
    print(value)

for key, value in person.items():  # 遍历键值对
    print(f"{key}: {value}")

# 视图对象
keys = person.keys()            # dict_keys(['name', 'age', 'city'])
values = person.values()        # dict_values(['Alice', 25, 'Beijing'])
items = person.items()          # dict_items([('name', 'Alice'), ...])

# ==================== 集合 (set) ====================

# 创建
fruits = {"apple", "banana", "cherry"}
empty = set()                   # 注意: {} 是空字典，不是空集合
from_list = set([1, 2, 2, 3, 3])  # {1, 2, 3} 自动去重

# 添加和删除
fruits.add("orange")             # 添加单个元素
fruits.update(["grape", "mango"])  # 添加多个元素
fruits.remove("banana")         # 删除，不存在会报错
fruits.discard("banana")        # 删除，不存在不报错
popped = fruits.pop()           # 随机弹出一个元素

# 集合运算
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)          # {1, 2, 3, 4, 5, 6}  并集
print(a & b)          # {3, 4}              交集
print(a - b)          # {1, 2}              差集
print(a ^ b)          # {1, 2, 5, 6}        对称差集

# 子集和超集
print({1, 2}.issubset({1, 2, 3}))     # True
print({1, 2, 3}.issuperset({1, 2}))   # True

# ==================== 列表作为栈和队列 ====================

stack = []
stack.append(1)       # 入栈
stack.append(2)
stack.pop()           # 出栈

from collections import deque
queue = deque()
queue.append(1)        # 入队
queue.append(2)
queue.popleft()        # 出队

# ==================== 列表推导式回顾 ====================

# 基本
squares = [x**2 for x in range(5)]

# 带条件
evens = [x for x in range(10) if x % 2 == 0]

# 嵌套
matrix = [[i*j for j in range(3)] for i in range(3)]

# 集合推导式
square_set = {x**2 for x in range(5)}

# 字典推导式
word = "hello"
char_count = {c: word.count(c) for c in set(word)}
