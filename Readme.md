#### 分析特征间的关系

1. 散点图：分析特征间的相关关系
   1. 特征之间是否存在数值或者数量的关联趋势（线性的还是非线性的）
   2. 某个点或者某几个点偏离大多数点，离群值，分析这些离群值是否在建模分析中影响很大
2. 折线图：分析自变量特征和因变量特征之间的趋势关系
3. 直方图：了解数据的数量状况
4. 饼图：特征内部数据的占比情况
5. 箱线图：特征内部数据的分散情况



#### 统计方法

1. min
2. max
3. mean
4. median 中位数
5. var 方差
6. sem 标准差
7. skew 样本偏度
8. ptp 极差
9. std 标准差
10. cov 协方差
11. mode 众数
12. kurt 样本峰度
13. count 非空值数目
14. mad 平均绝对离差
15. quantile 四分位数
16. describe 描述统计



### sklearn

#### 转换器、估计器

1. model_selection 模型选择模块
2. processing 数据预处理模块
3. decompisition 特征分解模块 实现数据预处理与模型构建前的数据标准化，二值化，数据集的分割，交叉验证和PCA 降维

##### 数据集的加载函数与任务类型

1. Boston  回归
2. california_housing 回归
3. digits 分类
4. breast_cancer : 分类 聚类
5. iris ：分类聚类
6. wine：分类



##### processing 数据预处理模块 特征变换函数

1. StandardScaler :对特征进行标准差标准化
2. Nomarlizer：对特征进行归一化
3. Binarizer：对定量特征进行二值化处理
4. OneHotEncoder：对定型特征进行独热编码处理
5. MinMaxScaler 离差标准化
6. FunctionTransfomer：对特征进行自定义函数变换
7. 降维算法 PCA 主成成分分析
   1. whiten 白化，true的话，对降维后的数据的每个特征进行归一化，让方差都为1 默认为false
   2. n_components 降低到n个维度

#### 

#### 聚类,分类，回归模型的评价

1. 分类模型评价方法
   1. precision 精确率  1
   2. recall 召回率 1
   3. F1 值 1
   4. cohen's kappa 系数 1
   5. roc曲线，越靠近y轴 越好
2. 聚类
   1. ari评价法 兰德系数 1
   2. ami 评价法 1
   3. v-measure 评分 1
   4. fmi评价法 1
   5. 轮廓系数评价法，畸变程度最大
   6. Calinski-harabasz 指数评价法。最大
3. 回归
   1. 平均绝对误差。 0. Mean_absolute_error
   2. 均方误差：0 mean_squared_error
   3. 中值绝对误差：0。median.absolute_error
   4. 可解释方差值，1 explained_variance_score
   5. R^ 2值。1 r2_score





### 聚类

> 没有给定划分类别的情况下，根据数据的形似度进行样本分组的一种方法
>
> 比如聚类可以帮助商场分析人员从消费者数据库中区分出不同的消费群体
>
> 可以用作预处理，异常值识别，连续性特征离散化
>
> 内部距离最小化，外部距离最大化。

#### 聚类算法

1. K-Means : 参数：簇数 使用范围：可用于样本数目很大，聚类数目中等的场景，距离度量：点之间的距离
2. Speatral clustering: 簇数,可用于样本数目中等，聚类数目较小的场景，图距离
3. ward hierarchiacal clustering 簇数，可用于样本数目很大，聚类数目较大的场景 点之间的距离
4. Agglomerative clustering 簇数，链接类型，距离，可用于样本数目较大，聚类数目较大的场景，任意成对点线间的距离
5. dbscan：半径大小，最低成员数目，可用于样本数目很大，聚类数目中等的场景，最近的点之间的距离
6. birch：分之音字，阈值，可选全局集群，样本数目很大，聚类数目很大的场景，点之间的欧式距离



#### 分类算法



1. 逻辑回归  函数: LogisticRegression 模块：linear_model
2. 支持向量机 SVC, svm
3. k最近邻分类 KNeightborsClassifier , neighbors
4. 高斯朴素贝叶斯 GaussionNB ,naive_bayes
5. 分类决策树 DecisionTreeClassifiler tree 
6. 随机森林 RandomForestClassifiler ensemble
7. 梯度提升树. GradientBoostingClassifier ensemble



#### 回归算法

| 模块名称     | 函数名称                   | 算法名称       |
| ------------ | -------------------------- | -------------- |
| Linear_model | LinearRegression           | 线形回归       |
| svm          | SVR                        | 支持向量回归   |
| neighbors    | KneighborsRegression       | 最近邻回归     |
| tree         | DescisionTreeRegression    | 决策树回归     |
| ensemble     | RandomForestRegression     | 随机森林回归   |
| ensemble     | GradientBoostingRegression | 梯度提升回归树 |



1. 分类和回归的主要区别：在于分类的算法的标签时离散的，回归算法的标签时连续的
2. 回归算法在 交通，金融，物流，社交 都能发挥巨大的作用





