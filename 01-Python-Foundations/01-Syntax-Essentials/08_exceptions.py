# -*- coding: utf-8 -*-
"""
Python 异常处理
===============

try/except/finally、抛出异常、自定义异常等。
"""

# ==================== 基本语法 ====================

# try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以零")

# 捕获异常对象
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"错误: {e}")
    print(f"异常类型: {type(e).__name__}")

# 多个 except
try:
    value = int("abc")
    result = 10 / 0
except ValueError as e:
    print(f"值错误: {e}")
except ZeroDivisionError as e:
    print(f"除零错误: {e}")

# 通用 except (不推荐)
try:
    result = 10 / 0
except Exception as e:
    print(f"发生错误: {e}")

# ==================== else 子句 ====================

try:
    result = 10 / 2
except ZeroDivisionError:
    print("除以零")
else:
    print(f"结果是 {result}")    # 只在没有异常时执行

# ==================== finally 子句 ====================

try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("文件不存在")
finally:
    # 无论是否异常都会执行，用于清理
    if 'file' in locals():
        file.close()
    print("清理完成")

# ==================== 抛出异常 ====================

def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)                      # 除数不能为零

# ==================== 自定义异常 ====================

class ValidationError(Exception):
    """验证错误"""
    pass

class PositiveNumberError(ValidationError):
    """必须是正数"""
    def __init__(self, value):
        self.value = value
        super().__init__(f"数值必须是正数，当前值: {value}")

def validate_positive(value):
    if value <= 0:
        raise PositiveNumberError(value)
    return value

try:
    validate_positive(-5)
except PositiveNumberError as e:
    print(e)                      # 数值必须是正数，当前值: -5

# ==================== 常见内置异常 ====================

# SyntaxError          - 语法错误
# IndentationError     - 缩进错误
# NameError            - 名字未定义
# TypeError            - 类型错误
# ValueError           - 值错误
# KeyError             - 字典键不存在
# IndexError           - 序列索引越界
# AttributeError       - 属性不存在
# ImportError          - 导入错误
# FileNotFoundError    - 文件不存在
# PermissionError      - 权限错误
# ZeroDivisionError    - 除零错误
# OverflowError        - 数值溢出
# MemoryError          - 内存错误
# KeyboardInterrupt    - Ctrl+C 中断
# Exception            - 所有异常的基类

# ==================== 异常层次结构 ====================

# BaseException
#   +-- SystemExit
#   +-- KeyboardInterrupt
#   +-- GeneratorExit
#   +-- Exception (大多数异常)
#        +-- StopIteration
#        +-- ArithmeticError
#        |    +-- FloatingPointError
#        |    +-- OverflowError
#        |    +-- ZeroDivisionError
#        +-- LookupError
#        |    +-- IndexError
#        |    +-- KeyError
#        +-- OSError
#        |    +-- FileNotFoundError
#        |    +-- PermissionError
#        +-- TypeError
#        +-- ValueError
#        +-- ...

# ==================== 上下文管理器 ====================

# with 语句自动管理资源
with open("test.txt", "w") as f:
    f.write("Hello")
# 文件自动关闭

# 自定义上下文管理器
class ManagedResource:
    def __enter__(self):
        print("获取资源")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("释放资源")
        if exc_type:
            print(f"处理异常: {exc_val}")
        # 返回 True 可以抑制异常
        return False

with ManagedResource() as resource:
    print("使用资源")
# 输出: 获取资源 -> 使用资源 -> 释放资源

# ==================== 异常链 ====================

try:
    int("abc")
except ValueError as e:
    raise TypeError("新错误") from e

# 使用 raise ... from None 断开异常链
try:
    int("abc")
except ValueError:
    raise TypeError("新错误") from None

# ==================== 捕获所有异常 ====================

# 不好的做法
# try:
#     dangerous_code()
# except:
#     pass

# 更好的做法
try:
    dangerous_code()
except Exception as e:
    print(f"发生错误: {e}")
    raise                    # 重新抛出，让调用者处理

# ==================== 实践建议 ====================

# 1. 精确捕获异常
try:
    d = {"a": 1}
    value = d["b"]
except KeyError:
    value = None

# 2. 清理时使用 finally 或 with
# 3. 异常应有具体类型
# 4. 添加有意义的错误信息
# 5. 不要用异常控制流程
