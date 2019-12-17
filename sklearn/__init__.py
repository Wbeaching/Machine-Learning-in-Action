from sklearn import tree

# 实例化
clf = tree.DecisionTreeClassifier()

x_train = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

y_train = [1, 2, 3]
# 用训练集数据训练数据
clf.fit(x_train, y_train)

r = clf.score([[2, 2, 2]], [3])

print(r)

r = clf.score([[2, 2, 2]], [2])

print(r)

# 0.0
# 1.0
