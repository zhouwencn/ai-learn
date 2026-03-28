# -*- coding: utf-8 -*-
"""
Python 函数
===========

函数定义、参数、返回值、装饰器等。
"""

# ==================== 基本定义 ====================

def greet():
    """简单的问候函数"""
    print("Hello, World!")

greet()

# 带参数
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 带返回值
def add(a, b):
    return a + b

result = add(3, 5)
print(result)          # 8

# ==================== 默认参数 ====================

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                      # Hello, Alice!
greet("Bob", "Hi")                  # Hi, Bob!

# 默认参数陷阱: 不要使用可变对象作为默认参数！
# 错误示例:
# def func(items=[]):   # 永远使用同一个列表
#     items.append(1)
#     return items

# 正确做法:
def func(items=None):
    if items is None:
        items = []
    items.append(1)
    return items

# ==================== 关键字参数 ====================

def power(base, exponent):
    return base ** exponent

power(2, 3)           # 位置参数
power(base=2, exponent=3)   # 关键字参数
power(exponent=3, base=2)  # 顺序无所谓

# ==================== 可变参数 ====================

# *args - 接收任意数量的位置参数
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))       # 6
print(sum_all(1, 2, 3, 4, 5)) # 15

# **kwargs - 接收任意数量的关键字参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Beijing")

# 组合使用
def func(*args, **kwargs):
    print(f"位置参数: {args}")
    print(f"关键字参数: {kwargs}")

func(1, 2, 3, name="Alice", age=25)

# ==================== 特殊参数 ====================

# / 分隔位置参数和关键字参数
def func(pos1, pos2, /, pos_or_kw, *, kw1, kw2):
    """pos1, pos2 只能是位置参数
       kw1, kw2 只能是关键字参数"""
    print(f"pos1={pos1}, pos2={pos2}, pos_or_kw={pos_or_kw}, kw1={kw1}, kw2={kw2}")

func(1, 2, 3, kw1=4, kw2=5)   # 正确
# func(1, 2, pos_or_kw=3, kw1=4, kw2=5)  # 错误!

# ==================== 返回值 ====================

# 多返回值
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(10, 3)
print(f"商={q}, 余数={r}")  # 商=3, 余数=1

# 隐式返回 None
def no_return():
    pass

result = no_return()
print(result)          # None

# ==================== 变量作用域 ====================

x = "全局"

def func():
    x = "局部"          # 创建局部变量，不影响全局
    print(x)            # 局部

def func2():
    global x            # 声明使用全局变量
    x = "修改全局"
    print(x)

# ==================== 闭包 ====================

def outer():
    x = "外层变量"

    def inner():
        print(x)        # 访问外层函数的变量
    return inner

closure = outer()
closure()               # 输出: 外层变量

# ==================== lambda 表达式 ====================

# 匿名函数，单行表达式
square = lambda x: x ** 2
print(square(5))        # 25

add = lambda a, b: a + b
print(add(3, 4))        # 7

# 配合内置函数使用
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
filtered = list(filter(lambda x: x % 2 == 0, numbers))
from functools import reduce
total = reduce(lambda a, b: a + b, numbers)

# ==================== 装饰器 ====================

def my_decorator(func):
    """装饰器: 在函数执行前后添加额外逻辑"""
    def wrapper(*args, **kwargs):
        print("函数开始执行")
        result = func(*args, **kwargs)
        print("函数执行结束")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

# 带参数的装饰器
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")

greet()

# ==================== 生成器 ====================

# yield 关键字使函数成为生成器
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(5)
print(list(gen))        # [1, 2, 3, 4, 5]

# 生成器表达式
gen = (x**2 for x in range(5))
print(list(gen))        # [0, 1, 4, 9, 16]
