# -*- coding: utf-8 -*-
"""
Python 类与对象
===============

类的定义、继承、特殊方法、属性等。
"""

# ==================== 基本定义 ====================

class Person:
    """人类"""

    # 类属性 (所有实例共享)
    species = "Human"
    count = 0

    # 初始化方法
    def __init__(self, name, age):
        self.name = name      # 实例属性
        self.age = age
        Person.count += 1

    # 实例方法
    def greet(self):
        return f"Hello, I'm {self.name}"

    # 字符串表示
    def __str__(self):
        return f"Person({self.name}, {self.age})"

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

# 创建实例
person = Person("Alice", 25)
print(person.name)           # Alice
print(person.greet())        # Hello, I'm Alice
print(person)                # Person(Alice, 25)
print(repr(person))          # Person(name='Alice', age=25)

# ==================== 访问控制 ====================

class Student:
    def __init__(self, name, grade):
        self.name = name           # 公开属性
        self._protected = grade     # 受保护属性 (约定)
        self.__private = []        # 私有属性 (名称重整)

    def add_score(self, score):
        self.__private.append(score)

    def get_average(self):
        if self.__private:
            return sum(self.__private) / len(self.__private)
        return 0

student = Student("Bob", 3)

print(student.name)                 # Bob
print(student._protected)           # 3 (虽然能访问，但不推荐)
# print(student.__private)          # 错误！无法直接访问
student.add_score(90)               # 通过方法访问私有属性
print(student.get_average())        # 90.0

# 访问私有属性的方式 (不推荐)
print(student._Student__private)    # [90]

# ==================== 类方法和静态方法 ====================

class Math:
    # 类方法
    @classmethod
    def class_info(cls):
        print(f"This is class {cls.__name__}")

    # 静态方法
    @staticmethod
    def add(a, b):
        return a + b

Math.class_info()                   # This is class Math
print(Math.add(2, 3))              # 5

# ==================== 继承 ====================

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("子类必须实现 speak 方法")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())                 # Buddy says Woof!
print(cat.speak())                 # Whiskers says Meow!

# 多继承
class Flyable:
    def fly(self):
        return "Flying!"

class Bird(Animal, Flyable):
    def speak(self):
        return f"{self.name} says Tweet!"

bird = Bird("Tweety")
print(bird.speak())                # Tweety says Tweet!
print(bird.fly())                  # Flying!

# ==================== 多态 ====================

def make_them_speak(animals):
    for animal in animals:
        print(animal.speak())

animals = [Dog("Rex"), Cat("Tom"), Bird("Birdy")]
make_them_speak(animals)

# ==================== 特殊方法 (魔术方法) ====================

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 运算符重载
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # 一元运算符
    def __neg__(self):
        return Vector(-self.x, -self.y)

    # 长度
    def __len__(self):
        return 2

    # 索引访问
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Index out of range")

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)                     # Vector(4, 6)
print(v1 - v2)                     # Vector(-2, -2)
print(v1 * 3)                      # Vector(3, 6)
print(-v1)                         # Vector(-1, -2)
print(len(v1))                    # 2
print(v1[0], v1[1])               # 1 2
print(v1 == Vector(1, 2))         # True

# ==================== @property ====================

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

circle = Circle(5)
print(circle.radius)              # 5 (像访问属性一样)
print(circle.area)                # 78.54...
circle.radius = 10               # 像设置属性一样
# circle.radius = -5             # 抛出异常

# ==================== 描述符 ====================

class Range:
    def __init__(self, min_val=None, max_val=None):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"{self.name} must be >= {self.min_val}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"{self.name} must be <= {self.max_val}")
        obj.__dict__[self.name] = value

class Player:
    age = Range(0, 150)
    score = Range(0, 100)

player = Player()
player.age = 25                   # 正常
player.score = 95                 # 正常
# player.age = 200               # 抛出异常

# ==================== 数据类 (dataclass) ====================

from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Circle:
    center: Point
    radius: float
    color: str = "red"           # 默认值
    tags: list = field(default_factory=list)  # 可变默认

p = Point(1.0, 2.0)
c = Circle(p, 5.0, tags=["circle", "shape"])
print(c)

# ==================== __slots__ ====================

# 限制实例属性，减少内存使用
class Restricted:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

# 尝试添加 __slots__ 中没有的属性会报错
r = Restricted("Alice", 25)
# r.address = "Beijing"          # AttributeError!
