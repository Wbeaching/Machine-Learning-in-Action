# K-近邻算法
## 目标
1. 了解K—近邻算法
2. 学会如何在其他系统上使用K-近邻算法
3. 如何使用距离测量的方法分类物品
4. 学习使用python从文本文件中导入并解析数据
5. 当存在多种数据源的时候，如何避免计算距离时碰到的一些常见的错误
6. k-近邻算法在系统运用中不断的改进

### 1、K-近邻算法概述
* 优点
1. 精度高
2. 对异常值不敏感
3. 无数据输入假定

* 缺点
1. 计算复杂度高
2. 空间复杂度高

* 适用数据范围
1. 数值型
2. 标称型

* K-近邻算法 工作原理

```
存在一个训练样本集，并且样本数据集合中每个数据都存在标签，

输入没有标签的新数据之后 将新数据的每个特征于样本集中数据对应的特征进行比较，然后算法提取样本集中最相似数据的分类标签。

一般来说，只选择样本数据集中前K个最相似的数据，这就是knn 算法的出处，通常k是不大于20的整数

选择k个最相似数据中出现次数最多的分类，最为新数据

```
k-近邻算法的一般流程
1. 收集数据：可以使用任何方法
2. 准备数据：距离计算所需要的数值，最好是结构化的数据格式
3. 分析数据：可以使用任何方法
4. 训练算法：不适合k-近邻算法
5. 测试算法: 计算错误率
6. 使用算法：首先需要输入样本数据和结构化的输出结果，然后运行k-近邻算法判定输入数据分别术语哪个分类，最后应用对计算的分类执行后续的处理

---

### 2、使用python导入数据

1. 计算已知类别数据集中的每个点与当前点的距离
2. 按照距离递增次序排序
3. 选取与当前带你距离最小的k个点
4. 确定前k个点所在的类别的出现频率
5. 返回前k个点出现频率最高的类别作为当前点的预测分类


```python
# -*- coding: utf-8 -*-
"""
@author: lishulong
@contact: lishulong.never@gmail.com
@time: 2017/11/13 下午11:21
"""

import numpy as np
import operator


def create_data_set():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0.1], [0, 0]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


# 使用python导入数据
g, l = create_data_set()
print(g)
print(l)


# 实施KNN分类算法 欧式距离公式

def classify0(inX, data_set, labels, k):
    data_set_size = data_set.shape[0]
    diff_mat = np.tile(inX, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distance = sq_diff_mat.sum(axis=1)
    distance = sq_distance ** 0.5

    sorted_distance = distance.argsort()

    class_count = {}

    for i in range(k):
        vortel_label = labels[sorted_distance[i]]
        class_count[vortel_label] = class_count.get(vortel_label, 0) + 1
        pass
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


result = classify0([1, 1], g, l, 3)
print(result)
result = classify0([0, 1], g, l, 3)
print(result)

"""
[[ 1.   1.1]
 [ 1.   1. ]
 [ 0.   0.1]
 [ 0.   0. ]]
['A', 'A', 'B', 'B']
A
B
"""
```
## 3. 如何测试分类器
> 不同的算法在不同的数据集上的表现可能完全不同

通过大量的测试数据得到算法分类器的错误率
