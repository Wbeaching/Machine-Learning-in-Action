# -*- coding:utf-8 -*-  

__author__ = 'lishulong.never@gmail.com'
__time__ = '2017/11/12'
__msg__ = '学不可以已'

from numpy import array

mm = array((1, 1, 1, 1, 1))
nn = array((2, 3, 4, 5, 6))

print(mm + nn)
print(mm - nn)
print(mm * 2)
print(mm / nn)
print(nn ** 2)

# numpy 支持多维数组
jj = array([[1, 2, 3], [4, 5, 6]])
print(jj)

print(jj[0, 1])
print(jj[0, 2])
print(jj[1, 2])

# matrix

from numpy import matrix, mat, shape

kk = matrix([[1, 2, 3], [1, 2, 3]])
print(kk)
ll = mat([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(ll)

print(shape(kk))
print(shape(ll))

# python list 转换为矩阵

list_demo = [1, 2, 3]
ma = matrix(list_demo)
print(matrix(list_demo))

# 做矩阵的列数必须喝右边矩阵的行数相等
print('==============')
print(ma * ll)

