# NumPy 与 Pandas 用法总结

## 目录

- [NumPy 基础](#numpy-基础)
- [Pandas 基础](#pandas-基础)
- [数据清洗](#数据清洗)
- [数据转换](#数据转换)
- [分组聚合](#分组聚合)
- [合并与连接](#合并与连接)
- [数据重塑](#数据重塑)
- [时间序列](#时间序列)
- [字符串操作](#字符串操作)
- [统计分析](#统计分析)

---

## NumPy 基础

### 数组创建

```python
import numpy as np

# 从列表创建
arr = np.array([1, 2, 3, 4, 5])

# 特殊数组
np.zeros(5)           # 全0数组
np.ones(5)            # 全1数组
np.full(5, 3.14)      # 全指定值
np.arange(0, 10, 2)    # 范围数组，步长2 → [0 2 4 6 8]
np.linspace(0, 1, 5)   # 等间距数组 → [0   0.25 0.5  0.75 1.  ]

# 随机数组
np.random.rand(5)          # [0,1)均匀分布
np.random.randn(5)         # 标准正态分布
np.random.randint(1, 10, 5) # 整数随机数组
```

### 数组属性

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr.shape      # (2, 3) - 形状
arr.ndim       # 2 - 维度
arr.size       # 6 - 元素总数
arr.dtype      # int64 - 数据类型
```

### 索引和切片

```python
arr = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]

arr[2:7]      # [2 3 4 5 6] - 索引2到6
arr[::2]      # [0 2 4 6 8] - 步长2
arr[::-1]     # [9 8 7 6 5 4 3 2 1 0] - 反转
arr[arr > 5]  # [6 7 8 9] - 条件索引

# 二维数组
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_2d[1, 2]      # 6 - 第二行第三列
arr_2d[:, 1]       # [2 5 8] - 所有行第二列
arr_2d[:2, :2]     # [[1 2] [4 5]] - 前2x2子矩阵
```

### 形状操作

```python
arr = np.arange(12)

arr.reshape(3, 4)   # 改变形状为3行4列
arr.flatten()        # 展平为一维
arr.T                # 转置
```

### 广播机制

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr + 100            # [[101 102 103] [104 105 106]]
arr + [1, 2, 3]     # [[2 4 6] [5 7 9]] - 行向量广播
arr + [[1], [2]]    # [[2 3 4] [6 7 8]] - 列向量广播
```

### 数组运算

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b          # [5 7 9] - 元素级加法
a * b          # [ 4 10 18] - 元素级乘法
a @ b          # 32 - 点积
np.dot(a, b)   # 32 - 点积

# 统计函数
arr.sum()      # 总和
arr.mean()     # 均值
arr.std()      # 标准差
arr.min()      # 最小值
arr.max()      # 最大值
arr.argmin()   # 最小值索引
arr.argmax()   # 最大值索引
```

### 条件逻辑

```python
arr = np.array([1, 2, 3, 4, 5])

np.where(arr > 2, 'big', 'small')
# ['small' 'small' 'big' 'big' 'big']

np.where((arr > 2) & (arr < 5), arr * 10, arr)
# [ 1  2 30 40  5]
```

### 拼接和分割

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.concatenate([a, b])   # [1 2 3 4 5 6]
np.hstack([a, b])        # 水平拼接
np.vstack([a, b])        # 垂直拼接 → [[1 2 3] [4 5 6]]

arr = np.arange(12).reshape(3, 4)
np.hsplit(arr, 2)        # 水平分割为2份
np.vsplit(arr, 3)        # 垂直分割为3份
```

---

## Pandas 基础

### Series

```python
import pandas as pd

# 基本创建
s = pd.Series([1, 2, 3, 4, 5])

# 带索引
s = pd.Series([90, 85, 78], index=['数学', '语文', '英语'])

# 从字典创建
data = {'苹果': 3, '香蕉': 2, '橙子': 5}
s = pd.Series(data)
```

### DataFrame

```python
# 从字典创建
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 35],
    '城市': ['北京', '上海', '广州']
})

# 查看数据
df.head()           # 前5行
df.tail()           # 后5行
df.shape             # (行数, 列数)
df.columns           # 列名
df.dtypes           # 数据类型
df.describe()        # 描述性统计
```

### 数据选择

```python
# 选择单列
df['姓名']

# 选择多列
df[['姓名', '年龄']]

# loc - 基于标签
df.loc[0, '姓名']                    # 获取单个值
df.loc[0:3, ['姓名', '年龄']]         # 行切片 + 列选择

# iloc - 基于位置
df.iloc[0, 1]                         # 第一行第二列
df.iloc[0:3, 1:4]                     # 行切片 + 列切片

# 布尔索引
df[df['年龄'] > 25]                   # 单条件
df[(df['年龄'] > 25) & (df['城市'] == '北京')]  # 多条件
df[df['姓名'].isin(['张三', '李四'])]  # isin 过滤

# query 方法
df.query('年龄 > 25 and 城市 == "北京"')
```

---

## 数据清洗

### 缺失值处理

```python
# 检测缺失值
df.isnull()                # 返回布尔数组
df.isnull().sum()          # 每列缺失值数量
df.notnull()                # 非缺失值

# 删除缺失值
df.dropna()                           # 删除含有缺失值的行
df.dropna(subset=['列名'])             # 只看指定列的缺失值

# 填充缺失值
df['列名'].fillna(0)                   # 用0填充
df['列名'].fillna(df['列名'].mean())   # 用均值填充
df['列名'].fillna('未知')              # 用指定值填充
df.fillna(method='ffill')             # 前向填充
df.fillna(method='bfill')             # 后向填充
```

### 重复值处理

```python
df.duplicated()                       # 返回布尔数组，标记重复行
df.duplicated(subset=['列名'])         # 基于指定列判断重复

df.drop_duplicates()                  # 删除重复行
df.drop_duplicates(subset=['列名'], keep='first')  # 保留第一个
```

### 异常值处理

```python
# IQR 方法检测
Q1 = df['列名'].quantile(0.25)
Q3 = df['列名'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['列名'] < lower) | (df['列名'] > upper)]

# 将异常值替换
df.loc[df['列名'] < 0, '列名'] = np.nan
```

### 数据类型转换

```python
# 转换日期
df['日期'] = pd.to_datetime(df['日期'])

# 转换数值
df['数量'] = pd.to_numeric(df['数量'], errors='coerce')

# 转换分类
df['类别'] = df['类别'].astype('category')

# 转换字符串
df['邮编'] = df['邮编'].astype(str)
```

---

## 数据转换

### apply - 沿轴应用函数

```python
# 应用到单列
df['金额级别'] = df['金额'].apply(lambda x: '高' if x > 1000 else '低')

# 应用到每行
df['检验'] = df.apply(lambda row: row['数量'] * row['单价'], axis=1)
```

### map - 映射变换

```python
地区映射 = {'华北': 'North', '华东': 'East', '华南': 'South'}
df['region_en'] = df['region'].map(地区映射)
```

### replace - 替换值

```python
df['状态'] = df['状态'].replace({
    '已完成': 'Completed',
    '已取消': 'Cancelled'
})
```

### assign - 添加新列

```python
df = df.assign(
    year=lambda x: x['日期'].dt.year,
    month=lambda x: x['日期'].dt.month
)
```

---

## 分组聚合

### 基本 groupby

```python
# 单列分组
df.groupby('分类')

# 多列分组
df.groupby(['地区', '分类'])

# 分组统计
df.groupby('分类').agg({
    '金额': ['sum', 'mean', 'count'],
    '数量': 'sum'
})
```

### 分组后过滤

```python
# 保留订单数大于3的分类
df.groupby('分类').filter(lambda x: len(x) > 3)
```

### 分组转换

```python
# 计算每组的金额占比
df['组内占比'] = df.groupby('分类')['金额'].transform('sum')
df['占比'] = df['金额'] / df['组内占比']
```

### 分组排序

```python
for 分类, 组 in df.groupby('分类'):
    top = 组.nlargest(3, '金额')
```

---

## 合并与连接

### merge - 数据库风格合并

```python
# 内连接 - 只保留两边都有的键
pd.merge(df1, df2, on='key', how='inner')

# 左连接 - 保留左边所有键
pd.merge(df1, df2, on='key', how='left')

# 右连接 - 保留右边所有键
pd.merge(df1, df2, on='key', how='right')

# 外连接 - 保留所有键
pd.merge(df1, df2, on='key', how='outer')
```

### concat - 拼接

```python
# 纵向拼接
pd.concat([df1, df2], ignore_index=True)

# 横向拼接
pd.concat([df1, df3], axis=1)
```

---

## 数据重塑

### pivot - 透视表

```python
df.pivot(index='日期', columns='产品', values='销售额')
```

### melt - 逆透视

```python
df.melt(id_vars='日期', value_name='销售额')
```

### stack 和 unstack

```python
# unstack - 将内层索引转为列
df.set_index(['年份', '城市'])['销量'].unstack(level='城市')

# stack - 将列转为索引
df.stack()
```

### crosstab - 交叉表

```python
pd.crosstab(df['性别'], df['部门'])
```

---

## 时间序列

### 日期转换

```python
# 字符串转日期
pd.to_datetime(df['日期'])

# 从字段组合
pd.to_datetime(df[['year', 'month', 'day']])
```

### 日期属性

```python
df['日期'].dt.year        # 年
df['日期'].dt.month       # 月
df['日期'].dt.day         # 日
df['日期'].dt.day_name()  # 星期名
df['日期'].dt.quarter     # 季度
```

### 重采样

```python
df.resample('D').mean()   # 日度重采样
df.resample('ME').mean()  # 月度重采样 (新版本用 ME)
df.resample('QE').mean()  # 季度重采样
```

---

## 字符串操作

```python
df['name'].str.lower()           # 小写
df['name'].str.upper()           # 大写
df['name'].str.strip()           # 去除空白
df['text'].str.contains('python')  # 包含判断
df['text'].str.replace('is', '==')  # 替换
df['text'].str.split(' ')        # 分割
df['text'].str.extract(r'ORD(\d+)')  # 提取
```

---

## 统计分析

### 描述性统计

```python
df.describe()           # 数值列描述统计
df['列名'].value_counts()  # 频次统计
```

### 相关性

```python
df.corr()               # 相关系数矩阵
```

### 累计计算

```python
df['累计和'] = df['金额'].cumsum()
df['累计占比'] = df['金额'].cumsum() / df['金额'].sum()
```

### 排名

```python
df['排名'] = df['分数'].rank(ascending=False)
```

### 滚动计算

```python
df['滚动均值'] = df['值'].rolling(window=3).mean()
df['滚动和'] = df['值'].rolling(window=3).sum()
```

---

## 常用函数速查

### NumPy

| 函数 | 说明 |
|------|------|
| `np.array()` | 从列表创建数组 |
| `np.zeros()`, `np.ones()` | 创建全0/全1数组 |
| `np.arange()`, `np.linspace()` | 创建范围数组 |
| `np.random.rand()`, `randn()`, `randint()` | 随机数组 |
| `arr.reshape()` | 改变形状 |
| `arr.sum()`, `mean()`, `std()` | 统计函数 |
| `np.where()` | 条件逻辑 |
| `np.unique()` | 唯一值 |
| `np.concatenate()`, `hstack()`, `vstack()` | 拼接 |
| `np.dot()` | 点积 |

### Pandas

| 函数 | 说明 |
|------|------|
| `pd.Series()`, `pd.DataFrame()` | 创建 Series/DataFrame |
| `df.head()`, `tail()` | 查看数据 |
| `df.loc()`, `iloc()` | 索引选择 |
| `df.isnull()`, `notnull()` | 缺失值检测 |
| `df.dropna()`, `fillna()` | 缺失值处理 |
| `df.drop_duplicates()` | 重复值处理 |
| `df.groupby()` | 分组 |
| `df.agg()`, `transform()`, `filter()` | 分组操作 |
| `pd.merge()`, `concat()` | 合并拼接 |
| `df.pivot()`, `melt()` | 数据重塑 |
| `pd.to_datetime()` | 日期转换 |
| `df.str_accessor` | 字符串操作 |
| `df.describe()`, `corr()` | 统计分析 |
