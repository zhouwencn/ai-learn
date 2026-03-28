# -*- coding: utf-8 -*-
"""
Python 文件操作
===============

读写文件、路径处理、目录操作等。
"""

# ==================== 读取文件 ====================

# 基本读取
with open("example.txt", "r") as f:
    content = f.read()           # 读取全部内容

# 按行读取
with open("example.txt", "r") as f:
    lines = f.readlines()        # 返回列表，每行一个元素

# 逐行迭代
with open("example.txt", "r") as f:
    for line in f:
        print(line.rstrip())     # rstrip() 去除换行符

# 限制读取字节数
with open("example.txt", "r") as f:
    chunk = f.read(1024)         # 读取最多 1024 字节

# ==================== 写入文件 ====================

# 写入 (覆盖)
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("第二行")

# 写入 (追加)
with open("output.txt", "a") as f:
    f.write("\n追加的内容")

# 写入多行
lines = ["第一行", "第二行", "第三行"]
with open("output.txt", "w") as f:
    f.write("\n".join(lines))

# 使用 writelines
with open("output.txt", "w") as f:
    f.writelines(line + "\n" for line in lines)

# ==================== 文件模式 ====================

# r   - 读取 (默认)
# w   - 写入 (覆盖)
# x   - 创建并写入 (文件存在则报错)
# a   - 追加
# b   - 二进制模式
# +   - 读写模式

# 示例
with open("file.bin", "wb") as f:     # 二进制写入
    f.write(b"\x00\x01\x02")

with open("file.bin", "rb") as f:     # 二进制读取
    data = f.read()

# ==================== 路径处理 ====================

import os
from pathlib import Path

# os.path 方式
os.path.join("dir", "subdir", "file.txt")   # 组合路径
os.path.dirname("/path/to/file.txt")        # 目录部分
os.path.basename("/path/to/file.txt")       # 文件名
os.path.splitext("file.txt")               # 分离扩展名
os.path.exists("file.txt")                 # 是否存在
os.path.isfile("file.txt")                  # 是否是文件
os.path.isdir("dir")                        # 是否是目录
os.path.getsize("file.txt")                # 文件大小

# pathlib 方式 (推荐, Python 3.4+)
p = Path("dir/subdir/file.txt")

p.parent                    # 父目录 Path 对象
p.name                      # 文件名 (含扩展名)
p.stem                      # 文件名 (不含扩展名)
p.suffix                    # 扩展名 (.txt)
p.exists()                  # 是否存在
p.is_file()                 # 是否是文件
p.is_dir()                  # 是否是目录

# 创建 Path 对象
p = Path(".") / "dir" / "file.txt"

# 路径遍历
for f in Path(".").iterdir():        # 当前目录所有文件/目录
    print(f.name)

for f in Path(".").glob("*.py"):     # 所有 Python 文件
    print(f.name)

# ==================== 目录操作 ====================

import os

# 创建目录
os.mkdir("newdir")                    # 创建单层目录
os.makedirs("path/to/nested/dir")     # 创建多层目录

# Path 版本
from pathlib import Path
Path("newdir").mkdir()
Path("path/to/nested/dir").mkdir(parents=True, exist_ok=True)

# 删除
os.rmdir("emptydir")                  # 删除空目录
os.remove("file.txt")                 # 删除文件

# 递归删除 (慎用！)
import shutil
shutil.rmtree("dir")                  # 删除目录及内容

# 复制
shutil.copy("source.txt", "dest.txt") # 复制文件
shutil.copytree("src", "dst")         # 复制目录

# 移动
shutil.move("source", "dest")         # 移动/重命名

# ==================== 文件操作 ====================

import os
import shutil

# 重命名
os.rename("old.txt", "new.txt")

# 复制
shutil.copy("source.txt", "dest.txt")

# 获取信息
os.stat("file.txt")                   # 文件详细信息

# 临时文件
import tempfile

# 临时文件
with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write("temporary")
    temp_name = f.name

# 临时目录
with tempfile.TemporaryDirectory() as tmpdir:
    print(f"临时目录: {tmpdir}")

# ==================== 文件指针 ====================

with open("example.txt", "r") as f:
    print(f.read(5))       # 读取前 5 个字节
    print(f.tell())        # 当前文件指针位置
    f.seek(0)              # 回到文件开头
    print(f.read(5))       # 再次读取前 5 个字节

# seek(offset, whence)
# whence: 0=文件开头, 1=当前位置, 2=文件末尾
with open("example.txt", "rb") as f:
    f.seek(-10, 2)         # 倒数第 10 个字节
    print(f.read())

# ==================== with 语句原理 ====================

# 文件对象支持上下文管理器协议
class MyFile:
    def __init__(self, name):
        self.name = name
        self.file = None

    def __enter__(self):
        self.file = open(self.name, "r")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

with MyFile("example.txt") as f:
    print(f.read())

# ==================== 编码问题 ====================

# 指定编码
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 处理编码错误
with open("file.txt", "r", encoding="utf-8", errors="replace") as f:
    content = f.read()

# errors 选项:
# ignore    - 忽略错误
# replace   - 用 ? 替换
# strict    - 抛出异常 (默认)

# ==================== 行结束符转换 ====================

# Unix: \n
# Windows: \r\n
# Mac (旧): \r

# 读取时 Python 会自动转换
# 写入时需要指定 newline 参数控制
with open("file.txt", "w", newline="") as f:  # 不转换
    f.write("line1\nline2")
