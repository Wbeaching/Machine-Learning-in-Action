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


# 实施KNN分类算法

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