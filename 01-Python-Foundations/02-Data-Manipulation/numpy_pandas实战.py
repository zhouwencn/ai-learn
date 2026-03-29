#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NumPy/Pandas 数据清洗与分析实战

本脚本通过一个销售数据集,全面演示 NumPy 和 Pandas 的核心知识点。
数据集存在多种数据质量问题,需要清洗后进行分析。
"""

import numpy as np
import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# 第一部分: NumPy 基础操作
# =============================================================================

print("=" * 70)
print("第一部分: NumPy 基础操作")
print("=" * 70)

# 1.1 数组创建
print("\n【1.1 数组创建】")

# 从列表创建
arr_from_list = np.array([1, 2, 3, 4, 5])
print(f"从列表创建: {arr_from_list}")

# 创建特定值的数组
zeros_arr = np.zeros(5)           # 全0数组
ones_arr = np.ones(5)             # 全1数组
full_arr = np.full(5, 3.14)      # 全指定值数组
print(f"全0数组: {zeros_arr}")
print(f"全1数组: {ones_arr}")
print(f"全3.14数组: {full_arr}")

# 创建范围数组
range_arr = np.arange(0, 10, 2)   # 步长为2
linspace_arr = np.linspace(0, 1, 5) # 5个等间距点
print(f"arange(0,10,2): {range_arr}")
print(f"linspace(0,1,5): {linspace_arr}")

# 创建随机数组
np.random.seed(42)
random_arr = np.random.rand(5)        # [0,1)均匀分布
normal_arr = np.random.randn(5)       # 标准正态分布
randint_arr = np.random.randint(1, 10, 5)  # 整数随机数组
print(f"rand(5): {random_arr}")
print(f"randn(5): {normal_arr}")
print(f"randint(1,10,5): {randint_arr}")

# 1.2 数组属性
print("\n【1.2 数组属性】")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"数组:\n{arr}")
print(f"形状 (shape): {arr.shape}")
print(f"维度 (ndim): {arr.ndim}")
print(f"元素总数 (size): {arr.size}")
print(f"数据类型 (dtype): {arr.dtype}")
print(f"元素字节大小 (itemsize): {arr.itemsize}")

# 1.3 数组索引和切片
print("\n【1.3 数组索引和切片】")
arr = np.arange(10)
print(f"原数组: {arr}")
print(f"arr[2:7] (索引2到6): {arr[2:7]}")
print(f"arr[::2] (步长2): {arr[::2]}")
print(f"arr[::-1] (反转): {arr[::-1]}")
print(f"arr[arr > 5] (条件索引): {arr[arr > 5]}")

# 二维数组索引
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n二维数组:\n{arr_2d}")
print(f"arr_2d[1, 2] (第二行第三列): {arr_2d[1, 2]}")
print(f"arr_2d[:, 1] (所有行第二列): {arr_2d[:, 1]}")
print(f"arr_2d[:2, :2] (前2x2子矩阵):\n{arr_2d[:2, :2]}")

# 1.4 数组形状操作
print("\n【1.4 数组形状操作】")
arr = np.arange(12)
print(f"原数组: {arr}")

reshaped = arr.reshape(3, 4)
print(f"reshape(3,4):\n{reshaped}")

flattened = reshaped.flatten()
print(f"flatten(): {flattened}")

# 转置
transposed = reshaped.T
print(f"T (转置):\n{transposed}")

# 1.5 广播机制
print("\n【1.5 广播机制】")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"数组:\n{arr}")
print(f"+ 100 (标量广播):\n{arr + 100}")
print(f"+ [1,2,3] (行向量广播):\n{arr + np.array([1, 2, 3])}")
print(f"+ [[1],[2]] (列向量广播):\n{arr + np.array([[1], [2]])}")

# 1.6 数组运算
print("\n【1.6 数组运算】")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")
print(f"a * b = {a * b}")           # 元素级乘法
print(f"a @ b = {a @ b}")           # 点积
print(f"np.dot(a, b) = {np.dot(a, b)}")

# 统计运算
arr = np.array([1, 2, 3, 4, 5])
print(f"\n数组: {arr}")
print(f"sum: {arr.sum()}")
print(f"mean: {arr.mean()}")
print(f"std: {arr.std()}")
print(f"min: {arr.min()}, max: {arr.max()}")
print(f"argmin: {arr.argmin()}, argmax: {arr.argmax()}")

# 1.7 条件逻辑
print("\n【1.7 条件逻辑】")
arr = np.array([1, 2, 3, 4, 5])
print(f"数组: {arr}")
print(f"np.where(arr > 2, 'big', 'small'): {np.where(arr > 2, 'big', 'small')}")

# 多条件
result = np.where(
    (arr > 2) & (arr < 5),
    arr * 10,
    arr
)
print(f"np.where((arr>2) & (arr<5), arr*10, arr): {result}")

# 1.8 数组拼接和分割
print("\n【1.8 数组拼接和分割】")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"a = {a}, b = {b}")
print(f"np.concatenate([a, b]): {np.concatenate([a, b])}")
print(f"np.hstack([a, b]): {np.hstack([a, b])}")
print(f"np.vstack([a, b]):\n{np.vstack([a, b])}")

arr = np.arange(12).reshape(3, 4)
print(f"\n数组:\n{arr}")
print(f"np.hsplit(arr, 2) (水平分割为2份):")
for part in np.hsplit(arr, 2):
    print(part)
print(f"np.vsplit(arr, 3) (垂直分割为3份):")
for part in np.vsplit(arr, 3):
    print(part)

# 1.9 唯一值和集合运算
print("\n【1.9 唯一值和集合运算】")
arr = np.array([1, 2, 2, 3, 3, 3, 4])
print(f"数组: {arr}")
print(f"np.unique: {np.unique(arr)}")
print(f"np.unique with counts:")
unique, counts = np.unique(arr, return_counts=True)
for u, c in zip(unique, counts):
    print(f"  {u}: {c}次")

# =============================================================================
# 第二部分: Pandas 基础 - Series 和 DataFrame
# =============================================================================

print("\n" + "=" * 70)
print("第二部分: Pandas 基础 - Series 和 DataFrame")
print("=" * 70)

# 2.1 Series 创建
print("\n【2.1 Series 创建】")
s = pd.Series([1, 2, 3, 4, 5])
print(f"基本Series:\n{s}")

# 带索引的Series
s = pd.Series([90, 85, 78], index=['数学', '语文', '英语'])
print(f"\n带索引的Series:\n{s}")
print(f"索引: {s.index.tolist()}")
print(f"值: {s.values}")

# 从字典创建
data = {'苹果': 3, '香蕉': 2, '橙子': 5}
s = pd.Series(data)
print(f"\n从字典创建:\n{s}")

# 2.2 DataFrame 创建
print("\n【2.2 DataFrame 创建】")

# 从字典创建
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 35],
    '城市': ['北京', '上海', '广州']
})
print(f"从字典创建DataFrame:\n{df}")

# 从二维数组创建
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(arr, columns=['A', 'B', 'C'], index=['row1', 'row2', 'row3'])
print(f"\n从数组创建DataFrame:\n{df}")

# 2.3 DataFrame 基本操作
print("\n【2.3 DataFrame 基本操作】")
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 35, 28],
    '工资': [8000, 12000, 15000, 9500],
    '部门': ['技术', '销售', '技术', '人事']
})
print(f"DataFrame:\n{df}")

# 查看数据
print(f"\n前2行:\n{df.head(2)}")
print(f"\n后2行:\n{df.tail(2)}")
print(f"\n形状: {df.shape}")
print(f"\n列名: {df.columns.tolist()}")
print(f"\n数据类型:\n{df.dtypes}")
print(f"\n基本统计:\n{df.describe()}")

# =============================================================================
# 第三部分: 数据读取和写入
# =============================================================================

print("\n" + "=" * 70)
print("第三部分: 数据读取和写入")
print("=" * 70)

# 3.1 读取 CSV
print("\n【3.1 读取 CSV 文件】")
df = pd.read_csv('sales_data.csv')
print(f"读取CSV文件，共 {len(df)} 行")
print(f"列名: {df.columns.tolist()}")

# 3.2 保存到 CSV
print("\n【3.2 保存到 CSV】")
df_sample = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df_sample.to_csv('output_sample.csv', index=False)
print("已保存到 output_sample.csv")

# =============================================================================
# 第四部分: 数据选择和过滤
# =============================================================================

print("\n" + "=" * 70)
print("第四部分: 数据选择和过滤")
print("=" * 70)

df = pd.read_csv('sales_data.csv')

# 4.1 选择单列
print("\n【4.1 选择单列】")
print(f"df['customer_name'] (前5行):\n{df['customer_name'].head()}")

# 4.2 选择多列
print("\n【4.2 选择多列】")
subset = df[['order_id', 'customer_name', 'total_amount']]
print(f"选择 order_id, customer_name, total_amount:\n{subset.head()}")

# 4.3 loc - 基于标签的选择
print("\n【4.3 loc - 基于标签的选择】")
print(f"df.loc[0, 'customer_name']: {df.loc[0, 'customer_name']}")
print(f"df.loc[0:3, ['customer_name', 'total_amount']]:\n{df.loc[0:3, ['customer_name', 'total_amount']]}")

# 4.4 iloc - 基于位置的选择
print("\n【4.4 iloc - 基于位置的选择】")
print(f"df.iloc[0, 1]: {df.iloc[0, 1]}")
print(f"df.iloc[0:3, 1:4]:\n{df.iloc[0:3, 1:4]}")

# 4.5 布尔索引
print("\n【4.5 布尔索引】")
# 单条件
high_value = df[df['total_amount'] > 3000]
print(f"总金额 > 3000 的订单 ({len(high_value)} 条):\n{high_value[['order_id', 'customer_name', 'total_amount']]}")

# 多条件
mask = (df['total_amount'] > 1000) & (df['region'] == '华北')
print(f"\n总金额 > 1000 且地区为华北:\n{df.loc[mask, ['order_id', 'region', 'total_amount']]}")

# 使用 isin
mask = df['category'].isin(['电子产品', '家具'])
print(f"\n类别为电子产品或家具:\n{df.loc[mask, ['order_id', 'category', 'total_amount']].head()}")

# 4.6 查询方法
print("\n【4.6 query 方法】")
result = df.query('total_amount > 3000 and region == "华北"')
print(f"query('total_amount > 3000 and region == \"华北\"'):\n{result[['order_id', 'region', 'total_amount']]}")

# =============================================================================
# 第五部分: 数据清洗
# =============================================================================

print("\n" + "=" * 70)
print("第五部分: 数据清洗")
print("=" * 70)

df = pd.read_csv('sales_data.csv')
print(f"原始数据形状: {df.shape}")
print(f"\n缺失值统计:\n{df.isnull().sum()}")
print(f"\n每列缺失值百分比:\n{(df.isnull().sum() / len(df) * 100).round(2)}%")

# 5.1 处理缺失值
print("\n【5.1 处理缺失值】")

# 识别缺失值
print("识别缺失值:")
print(f"df[df['product'].isnull()] (产品名为空的行):\n{df[df['product'].isnull()]}")
print(f"\ndf[df['total_amount'].isnull()] (总金额为空的行):\n{df[df['total_amount'].isnull()]}")

# 删除缺失值
df_cleaned = df.copy()
df_cleaned = df_cleaned.dropna(subset=['customer_name', 'product'])
print(f"\n删除 customer_name 或 product 缺失的行后: {len(df_cleaned)} 行")

# 填充缺失值 - 数值列用均值填充
mean_price = df_cleaned['total_amount'].mean()
df_cleaned['total_amount'] = df_cleaned['total_amount'].fillna(mean_price)
print(f"total_amount 缺失值用均值 {mean_price:.2f} 填充")

# 分类列用众数或占位符填充
df_cleaned['region'] = df_cleaned['region'].fillna('未知')
df_cleaned['salesperson'] = df_cleaned['salesperson'].fillna('未知')
print(f"region 和 salesperson 缺失值用 '未知' 填充")

# 5.2 处理重复值
print("\n【5.2 处理重复值】")
print(f"重复行数量: {df_cleaned.duplicated().sum()}")
# 查找重复行
print(f"\n重复的行(基于customer_name和product):")
duplicates = df_cleaned[df_cleaned.duplicated(subset=['customer_name', 'product'], keep=False)]
print(duplicates)

# 删除重复行
df_cleaned = df_cleaned.drop_duplicates(subset=['customer_name', 'product'], keep='first')
print(f"\n删除重复行后: {len(df_cleaned)} 行")

# 5.3 处理异常值
print("\n【5.3 处理异常值】")

# 数量异常(负数或零)
print("数量异常检测 (quantity <= 0):")
abnormal_qty = df_cleaned[df_cleaned['quantity'] <= 0]
print(abnormal_qty[['order_id', 'product', 'quantity']])

# 将异常数量设为 NaN 或修正
df_cleaned.loc[df_cleaned['quantity'] <= 0, 'quantity'] = np.nan

# 总金额异常(负数)
print("\n总金额异常检测 (total_amount < 0):")
abnormal_amt = df_cleaned[df_cleaned['total_amount'] < 0]
print(abnormal_amt[['order_id', 'product', 'total_amount']])

# 修正总金额 (根据 quantity * unit_price * (1-discount))
mask = df_cleaned['total_amount'] < 0
df_cleaned.loc[mask, 'total_amount'] = (
    df_cleaned.loc[mask, 'quantity'] *
    df_cleaned.loc[mask, 'unit_price'] *
    (1 - df_cleaned.loc[mask, 'discount'])
)
print("已根据 quantity * unit_price * (1-discount) 修正")

# 使用 IQR 方法检测金额异常值
print("\n使用 IQR 方法检测金额异常值:")
Q1 = df_cleaned['total_amount'].quantile(0.25)
Q3 = df_cleaned['total_amount'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df_cleaned[(df_cleaned['total_amount'] < lower_bound) | (df_cleaned['total_amount'] > upper_bound)]
print(f"Q1={Q1:.2f}, Q3={Q3:.2f}, IQR={IQR:.2f}")
print(f"正常范围: [{lower_bound:.2f}, {upper_bound:.2f}]")
print(f"异常值 ({len(outliers)} 条):\n{outliers[['order_id', 'total_amount']]}")

# 5.4 字符串清洗
print("\n【5.4 字符串清洗】")

# 清洗 email 格式
def clean_email(email):
    if pd.isna(email):
        return '未知'
    email = str(email).strip().lower()
    if '@' not in email or '.' not in email:
        return '无效邮箱'
    return email

df_cleaned['email'] = df_cleaned['email'].apply(clean_email)
print(f"清洗后的 email:\n{df_cleaned['email'].head(10)}")

# 去除前后空格
df_cleaned['customer_name'] = df_cleaned['customer_name'].str.strip()
df_cleaned['product'] = df_cleaned['product'].str.strip()

# 5.5 数据类型转换
print("\n【5.5 数据类型转换】")
print(f"转换前类型:\n{df_cleaned.dtypes}")

# 转换日期
df_cleaned['order_date'] = pd.to_datetime(df_cleaned['order_date'], errors='coerce')
print(f"\n转换日期后:\n{df_cleaned['order_date'].dtype}")

# 转换数值列
df_cleaned['quantity'] = pd.to_numeric(df_cleaned['quantity'], errors='coerce').astype('Int64')
df_cleaned['unit_price'] = pd.to_numeric(df_cleaned['unit_price'], errors='coerce')
df_cleaned['total_amount'] = pd.to_numeric(df_cleaned['total_amount'], errors='coerce')
df_cleaned['discount'] = pd.to_numeric(df_cleaned['discount'], errors='coerce')

# 转换分类列为 category 类型
df_cleaned['category'] = df_cleaned['category'].astype('category')
df_cleaned['region'] = df_cleaned['region'].astype('category')
df_cleaned['status'] = df_cleaned['status'].astype('category')

print(f"\n转换后类型:\n{df_cleaned.dtypes}")

# =============================================================================
# 第六部分: 数据转换和映射
# =============================================================================

print("\n" + "=" * 70)
print("第六部分: 数据转换和映射")
print("=" * 70)

df = pd.read_csv('sales_data.csv')

# 6.1 apply - 沿轴应用函数
print("\n【6.1 apply 方法】")

# 应用到单列
def classify_amount(amount):
    if pd.isna(amount):
        return '未知'
    if amount < 500:
        return '低'
    elif amount < 2000:
        return '中'
    else:
        return '高'

df['amount_level'] = df['total_amount'].apply(classify_amount)
print(f"应用 classify_amount 函数:\n{df[['order_id', 'total_amount', 'amount_level']].head()}")

# 应用到每行
def row_check(row):
    expected = row['quantity'] * row['unit_price'] * (1 - row['discount'])
    actual = row['total_amount']
    if pd.isna(actual):
        return '缺失'
    diff = abs(expected - actual) / expected if expected != 0 else 0
    return '正确' if diff < 0.01 else '错误'

df['amount_check'] = df.apply(row_check, axis=1)
print(f"\n行级检查金额是否正确:\n{df[['order_id', 'quantity', 'unit_price', 'discount', 'total_amount', 'amount_check']].head()}")

# 6.2 map - 映射变换
print("\n【6.2 map 方法】")

# 地区映射
region_map = {
    '华北': 'Northern',
    '华东': 'Eastern',
    '华南': 'Southern',
    '华中': 'Central'
}
df['region_en'] = df['region'].map(region_map)
print(f"地区映射:\n{df[['order_id', 'region', 'region_en']].head()}")

# 6.3 replace - 替换值
print("\n【6.3 replace 方法】")
print(f"状态唯一值: {df['status'].unique()}")
df['status_clean'] = df['status'].replace({
    '已完成': 'Completed',
    '已取消': 'Cancelled',
    '已退款': 'Refunded',
    '处理中': 'Processing'
})
print(f"状态替换:\n{df[['order_id', 'status', 'status_clean']].head()}")

# 6.4 assign - 添加新列
print("\n【6.4 assign 方法】")
df = df.assign(
    year=lambda x: pd.to_datetime(x['order_date']).dt.year,
    month=lambda x: pd.to_datetime(x['order_date']).dt.month,
    day_of_week=lambda x: pd.to_datetime(x['order_date']).dt.dayofweek
)
print(f"添加 year, month, day_of_week:\n{df[['order_id', 'order_date', 'year', 'month', 'day_of_week']].head()}")

# =============================================================================
# 第七部分: 分组聚合
# =============================================================================

print("\n" + "=" * 70)
print("第七部分: 分组聚合")
print("=" * 70)

df_clean = pd.read_csv('sales_data.csv')
df_clean['total_amount'] = pd.to_numeric(df_clean['total_amount'], errors='coerce')
df_clean['quantity'] = pd.to_numeric(df_clean['quantity'], errors='coerce')

# 7.1 基本 groupby
print("\n【7.1 基本 groupby】")

# 按单列分组
grouped = df_clean.groupby('category')
print(f"按 category 分组:\n{grouped.size()}")

# 分组统计
category_stats = df_clean.groupby('category').agg({
    'total_amount': ['sum', 'mean', 'count'],
    'quantity': 'sum'
}).round(2)
category_stats.columns = ['总金额', '平均金额', '订单数', '总数量']
print(f"\n分类统计:\n{category_stats}")

# 7.2 多列分组
print("\n【7.2 多列分组】")
region_category = df_clean.groupby(['region', 'category']).agg({
    'total_amount': 'sum',
    'order_id': 'count'
}).round(2)
region_category.columns = ['总金额', '订单数']
print(f"按地区和分类统计:\n{region_category}")

# 7.3 分组后过滤
print("\n【7.3 分组后过滤】")
# 找出订单数大于3的分类
valid_categories = df_clean.groupby('category').filter(lambda x: len(x) > 3)
print(f"订单数 > 3 的分类数据 ({len(valid_categories)} 行):")
print(valid_categories[['order_id', 'category', 'total_amount']].head())

# 7.4 分组转换
print("\n【7.4 分组转换】")
# 计算每个分类的金额占比
df_clean['category_total'] = df_clean.groupby('category')['total_amount'].transform('sum')
df_clean['category_ratio'] = (df_clean['total_amount'] / df_clean['category_total'] * 100).round(2)
print(f"金额占比:\n{df_clean[['order_id', 'category', 'total_amount', 'category_total', 'category_ratio']].head()}")

# 7.5 分组后排序
print("\n【7.5 分组后排序】")
for category, group in df_clean.groupby('category'):
    top_orders = group.nlargest(2, 'total_amount')
    print(f"\n{category} Top 2 订单:")
    print(top_orders[['order_id', 'customer_name', 'total_amount']])

# =============================================================================
# 第八部分: 合并与连接
# =============================================================================

print("\n" + "=" * 70)
print("第八部分: 合并与连接")
print("=" * 70)

# 8.1 创建演示数据
df_orders = pd.DataFrame({
    'order_id': ['ORD001', 'ORD002', 'ORD003', 'ORD004'],
    'customer_id': [101, 102, 103, 104],
    'amount': [1000, 2000, 1500, 3000]
})

df_customers = pd.DataFrame({
    'customer_id': [101, 102, 105],
    'name': ['张三', '李四', '王五'],
    'vip_level': ['gold', 'silver', 'bronze']
})

print("订单表:\n{df_orders}")
print("\n客户表:\n{df_customers}")

# 8.2 merge - 数据库风格的合并
print("\n【8.2 merge 方法】")

# 内连接 (inner) - 只保留两边都有的键
inner_merged = pd.merge(df_orders, df_customers, on='customer_id', how='inner')
print(f"内连接:\n{inner_merged}")

# 左连接 (left) - 保留左边所有键
left_merged = pd.merge(df_orders, df_customers, on='customer_id', how='left')
print(f"\n左连接:\n{left_merged}")

# 外连接 (outer) - 保留所有键
outer_merged = pd.merge(df_orders, df_customers, on='customer_id', how='outer')
print(f"\n外连接:\n{outer_merged}")

# 8.3 concat - 拼接
print("\n【8.3 concat 拼接】")
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df3 = pd.DataFrame({'C': [9, 10], 'D': [11, 12]})

print(f"拼接两个相同列的DataFrame:")
print(pd.concat([df1, df2], ignore_index=True))

print(f"\n横向拼接不同列的DataFrame:")
print(pd.concat([df1, df3], axis=1))

# =============================================================================
# 第九部分: 数据重塑
# =============================================================================

print("\n" + "=" * 70)
print("第九部分: 数据重塑")
print("=" * 70)

# 9.1 pivot - 透视
print("\n【9.1 pivot 透视表】")
df_sales = pd.DataFrame({
    '日期': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    '产品': ['A', 'B', 'A', 'B'],
    '销售额': [100, 200, 150, 250],
    '数量': [10, 20, 15, 25]
})
print(f"原始数据:\n{df_sales}")

pivot_df = df_sales.pivot(index='日期', columns='产品', values='销售额')
print(f"\n透视表 (日期为行, 产品为列, 销售额为值):\n{pivot_df}")

# 9.2 melt - 逆透视
print("\n【9.2 melt 逆透视】")
melted = pivot_df.reset_index().melt(id_vars='日期', value_name='销售额')
print(f"逆透视:\n{melted}")

# 9.3 stack 和 unstack
print("\n【9.3 stack 和 unstack】")

# 使用 set_index + unstack 创建透视表的另一种方式
df_stack = pd.DataFrame({
    '年份': ['2023', '2023', '2024', '2024'],
    '城市': ['北京', '上海', '北京', '上海'],
    '销量': [100, 150, 200, 250]
})
print(f"原始数据:\n{df_stack}")

# unstack 将城市从行索引转为列
unstacked = df_stack.set_index(['年份', '城市'])['销量'].unstack()
print(f"\nunstack (将城市从行转为列):\n{unstacked}")

# stack 将列转为行索引
stacked = unstacked.stack()
print(f"\nstack (将列转为行):\n{stacked}")

# 9.4 crosstab - 交叉表
print("\n【9.4 crosstab 交叉表】")
df_cross = pd.DataFrame({
    '性别': ['男', '女', '男', '女', '男'],
    '部门': ['技术', '技术', '销售', '销售', '技术']
})
print(pd.crosstab(df_cross['性别'], df_cross['部门']))

# =============================================================================
# 第十部分: 时间序列处理
# =============================================================================

print("\n" + "=" * 70)
print("第十部分: 时间序列处理")
print("=" * 70)

# 10.1 日期类型转换
print("\n【10.1 日期类型转换】")
dates = ['2024-01-01', '2024-02-15', '2024-03-20']
ts = pd.to_datetime(dates)
print(f"字符串转日期:\n{ts}")

# 从多个字段组合日期
df = pd.DataFrame({
    'year': [2024, 2024, 2024],
    'month': [1, 2, 3],
    'day': [15, 20, 25]
})
df['date'] = pd.to_datetime(df)
print(f"\n组合字段转日期:\n{df}")

# 10.2 日期索引
print("\n【10.2 日期索引】")
df = pd.DataFrame({
    'value': [100, 200, 300, 400]
}, index=pd.date_range('2024-01-01', periods=4, freq='D'))
print(f"日期索引:\n{df}")

# 10.3 日期属性访问
print("\n【10.3 日期属性】")
df['date'] = pd.date_range('2024-01-01', periods=4, freq='D')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.day_name()
df['quarter'] = df['date'].dt.quarter
print(df)

# 10.4 日期重采样
print("\n【10.4 重采样】")
df = pd.DataFrame({
    'value': np.random.randn(10) * 10 + 100
}, index=pd.date_range('2024-01-01', periods=10, freq='D'))
print(f"日数据:\n{df}")

monthly = df.resample('ME').mean()
print(f"\n月度重采样:\n{monthly}")

# =============================================================================
# 第十一部分: 字符串操作
# =============================================================================

print("\n" + "=" * 70)
print("第十一部分: 字符串操作")
print("=" * 70)

df = pd.DataFrame({
    'name': ['  张三  ', '李四', 'wang wei'],
    'email': ['zhang@email.com', 'li@EMAIL.COM', 'wang@test.cn'],
    'phone': ['138-0000-0001', '139-0000-0002', '137-0000-0003']
})

# 11.1 字符串 accessor
print("\n【11.1 字符串 accessor】")
print(f"原始数据:\n{df}")

# 小写/大写
df['email_lower'] = df['email'].str.lower()
df['email_upper'] = df['email'].str.upper()
print(f"\n大小写转换:\n{df[['email', 'email_lower', 'email_upper']]}")

# 去除空白
df['name_stripped'] = df['name'].str.strip()
print(f"\n去除空白:\n{df[['name', 'name_stripped']]}")

# 11.2 字符串查找和替换
print("\n【11.2 字符串查找和替换】")
df = pd.DataFrame({
    'text': ['hello world', 'python is great', 'data science']
})

# 包含判断
print(f"包含 'python':\n{df['text'].str.contains('python')}")

# 替换
print(f"\n替换 'is' 为 '==' :\n{df['text'].str.replace('is', '==')}")

# 分割
print(f"\n分割为列表:\n{df['text'].str.split(' ')}")

# 11.3 字符串提取
print("\n【11.3 字符串提取】")
df = pd.DataFrame({
    'info': ['订单号: ORD001', '订单号: ORD002', '订单号: ORD003']
})
df['order_id'] = df['info'].str.extract(r'ORD(\d+)')
print(f"提取订单号:\n{df}")

# =============================================================================
# 第十二部分: 统计分析
# =============================================================================

print("\n" + "=" * 70)
print("第十二部分: 统计分析")
print("=" * 70)

df = pd.DataFrame({
    'A': np.random.randn(100),
    'B': np.random.randn(100) * 2,
    'C': np.random.randn(100) + 3
})

# 12.1 描述性统计
print("\n【12.1 描述性统计】")
print(df.describe())

# 12.2 相关系数
print("\n【12.2 相关系数】")
print(df.corr())

# 12.3 累计计算
print("\n【12.3 累计计算】")
print(f"A列累计和:\n{df['A'].cumsum().head()}")

# 12.4 排名
print("\n【12.4 排名】")
df_rank = pd.DataFrame({'score': [90, 85, 95, 80]})
df_rank['rank'] = df_rank['score'].rank(ascending=False)
print(f"排名:\n{df_rank}")

# 12.5 滚动计算
print("\n【12.5 滚动计算】")
df_rolling = pd.DataFrame({'value': range(1, 11)})
df_rolling['rolling_mean_3'] = df_rolling['value'].rolling(window=3).mean()
df_rolling['rolling_sum_3'] = df_rolling['value'].rolling(window=3).sum()
print(f"滚动窗口(3)计算:\n{df_rolling}")

# =============================================================================
# 第十三部分: 综合数据分析实战
# =============================================================================

print("\n" + "=" * 70)
print("第十三部分: 综合数据分析实战")
print("=" * 70)

print("\n【销售数据分析】\n")

# 读取并清洗数据
df = pd.read_csv('sales_data.csv')
df['total_amount'] = pd.to_numeric(df['total_amount'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['discount'] = pd.to_numeric(df['discount'], errors='coerce')
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# 过滤有效订单
df_valid = df.dropna(subset=['total_amount', 'quantity'])
df_valid = df_valid[df_valid['total_amount'] > 0]

print(f"有效订单数: {len(df_valid)}")

# 1. 整体销售概况
print("\n1. 整体销售概况:")
total_revenue = df_valid['total_amount'].sum()
total_orders = len(df_valid)
avg_order_value = df_valid['total_amount'].mean()
print(f"   总销售额: ¥{total_revenue:,.2f}")
print(f"   总订单数: {total_orders}")
print(f"   平均订单金额: ¥{avg_order_value:,.2f}")

# 2. 按时段分析
print("\n2. 月度销售趋势:")
df_valid['month'] = df_valid['order_date'].dt.month
monthly = df_valid.groupby('month').agg({
    'total_amount': 'sum',
    'order_id': 'count'
}).round(2)
monthly.columns = ['销售额', '订单数']
monthly['客单价'] = (monthly['销售额'] / monthly['订单数']).round(2)
print(monthly)

# 3. 按地区分析
print("\n3. 地区销售排名:")
region_stats = df_valid.groupby('region').agg({
    'total_amount': ['sum', 'mean', 'count']
}).round(2)
region_stats.columns = ['销售额', '平均金额', '订单数']
region_stats = region_stats.sort_values('销售额', ascending=False)
print(region_stats)

# 4. 按产品分类分析
print("\n4. 产品分类分析:")
category_stats = df_valid.groupby('category').agg({
    'total_amount': ['sum', 'mean'],
    'quantity': 'sum',
    'order_id': 'count'
}).round(2)
category_stats.columns = ['销售额', '平均金额', '总销量', '订单数']
category_stats['平均客件数'] = (category_stats['总销量'] / category_stats['订单数']).round(2)
print(category_stats)

# 5. Top 10 产品
print("\n5. Top 10 产品:")
product_stats = df_valid.groupby('product').agg({
    'total_amount': 'sum',
    'quantity': 'sum',
    'order_id': 'count'
}).round(2)
product_stats.columns = ['销售额', '销量', '订单数']
top_products = product_stats.sort_values('销售额', ascending=False).head(10)
print(top_products)

# 6. 销售员业绩
print("\n6. 销售员业绩排名:")
salesperson_stats = df_valid.groupby('salesperson').agg({
    'total_amount': ['sum', 'mean', 'count']
}).round(2)
salesperson_stats.columns = ['销售额', '平均金额', '订单数']
salesperson_stats = salesperson_stats.sort_values('销售额', ascending=False)
print(salesperson_stats)

# 7. 折扣分析
print("\n7. 折扣分析:")
discount_analysis = df_valid.groupby('discount').agg({
    'total_amount': 'sum',
    'order_id': 'count'
})
discount_analysis.columns = ['销售额', '订单数']
print(discount_analysis)

# 8. 订单状态分布
print("\n8. 订单状态分布:")
status_dist = df['status'].value_counts()
status_pct = (df['status'].value_counts(normalize=True) * 100).round(2)
status_df = pd.DataFrame({
    '数量': status_dist,
    '占比(%)': status_pct
})
print(status_df)

# =============================================================================
# 第十四部分: 数据保存
# =============================================================================

print("\n" + "=" * 70)
print("第十四部分: 数据保存")
print("=" * 70)

# 保存清洗后的数据
df_valid.to_csv('sales_data_cleaned.csv', index=False, encoding='utf-8-sig')
print("清洗后的数据已保存到 sales_data_cleaned.csv")

# 保存分析结果
summary = pd.DataFrame({
    '指标': ['总销售额', '总订单数', '平均订单金额', '平均折扣'],
    '数值': [
        f"¥{total_revenue:,.2f}",
        total_orders,
        f"¥{avg_order_value:,.2f}",
        f"{df_valid['discount'].mean():.2%}"
    ]
})
summary.to_csv('sales_summary.csv', index=False, encoding='utf-8-sig')
print("销售汇总已保存到 sales_summary.csv")

print("\n" + "=" * 70)
print("实战练习完成!")
print("=" * 70)
