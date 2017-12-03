from __future__ import division
import numpy as np
import scipy as sp
import csv

class Item_based_C:
    def __init__(self, X):
        self.X = np.array(X)
        # print(self.X.dtype)
        print("the input data size is "+ str(self.X.shape))
        self.movie_user = {}
        self.user_movie = {}
        self.ave = np.mean(self.X[:, 2])
        # print(self.X[:, 2])
        for i in range(self.X.shape[0]):
            uid = self.X[i][0]
            mid = self.X[i][1]
            rat = self.X[i][2]
            self.movie_user.setdefault(mid, {})
            self.user_movie.setdefault(uid, {})
            # if(i<150):
            #     print(self.movie_user)
            self.movie_user[mid][uid] = rat
            self.user_movie[uid][mid] = rat
            # print(self.movie_user)
        self.similarity = {}
        pass

    def sim_cal(self, m1, m2):
        self.similarity.setdefault(m1, {})
        self.similarity.setdefault(m2, {})
        self.movie_user.setdefault(m1, {})
        self.movie_user.setdefault(m2, {})
        self.similarity[m1].setdefault(m2, -1)
        self.similarity[m2].setdefault(m1, -1)

        if self.similarity[m1][m2] != -1:
            return self.similarity[m1][m2]
        si = {}
        # 看过m1的人看过m2
        for user in self.movie_user[m1]:
            if user in self.movie_user[m2]:
                si[user] = 1
        n = len(si)
        if (n == 0):
            self.similarity[m1][m2] = 1
            self.similarity[m2][m1] = 1
            return 1
        s1 = np.array([self.movie_user[m1][u] for u in si])
        s2 = np.array([self.movie_user[m2][u] for u in si])
        # 皮尔逊相似度
        sum1 = np.sum(s1)
        sum2 = np.sum(s2)
        sum1Sq = np.sum(s1 ** 2)
        sum2Sq = np.sum(s2 ** 2)
        pSum = np.sum(s1 * s2)
        num = pSum - (sum1 * sum2 / n)
        den = np.sqrt((sum1Sq - sum1 ** 2 / n) * (sum2Sq - sum2 ** 2 / n))
        if den == 0:
            self.similarity[m1][m2] = 0
            self.similarity[m2][m1] = 0
            return 0
        self.similarity[m1][m2] = num / den
        self.similarity[m2][m1] = num / den
        return num / den

    def sim_cal2(self, m1, m2):
        self.similarity.setdefault(m1, {})
        self.similarity.setdefault(m2, {})
        self.movie_user.setdefault(m1, {})
        self.movie_user.setdefault(m2, {})
        self.similarity[m1].setdefault(m2, -1)
        self.similarity[m2].setdefault(m1, -1)

        if self.similarity[m1][m2] != -1:
            return self.similarity[m1][m2]
        si = {}
        # 看过m1的人看过m2
        for user in self.movie_user[m1]:
            if user in self.movie_user[m2]:
                si[user] = 1
        n = len(si)
        if (n == 0):
            self.similarity[m1][m2] = 1
            self.similarity[m2][m1] = 1
            return 1
        s1 = np.array([self.movie_user[m1][u] for u in si])
        s2 = np.array([self.movie_user[m2][u] for u in si])
        # 余弦相似度
        sum1Sq = np.sum(s1 ** 2)
        sum2Sq = np.sum(s2 ** 2)
        pSum = np.sum(s1 * s2)
        num = pSum
        den = np.sqrt(sum1Sq) * (sum2Sq)
        if den == 0:
            self.similarity[m1][m2] = 0
            self.similarity[m2][m1] = 0
            return 0
        self.similarity[m1][m2] = num / den
        self.similarity[m2][m1] = num / den
        return num / den

    def pred(self, uid, mid):
        sim_accumulate = 0.0
        rat_acc = 0.0
        for item in self.user_movie[uid]:
            sim = self.sim_cal(item, mid)   #item电影和mid电影的相似度
            # print(sim)
            if sim < 0: continue
            # print sim,self.user_movie[uid][item],sim*self.user_movie[uid][item]
            rat_acc += sim * self.user_movie[uid][item]
            sim_accumulate += sim
            # print rat_acc,sim_accumulate
        if sim_accumulate == 0:  # no same user rated,return average rates of the data
            return self.ave
        return rat_acc / sim_accumulate

    def test(self, test_X):
        test_X = np.array(test_X)
        output = []
        sums = 0
        print("the test data size is "+str(test_X.shape))
        for i in range(test_X.shape[0]):
            pre = self.pred(test_X[i][0], test_X[i][1])
            output.append(pre)
            # print pre,test_X[i][2]
            sums += (pre - test_X[i][2]) ** 2
        rmse = np.sqrt(sums / test_X.shape[0])
        print("the rmse on test data is " + str(rmse))
        return output

file = open(r'D:\数据 电影\数据 电影\ml-100k\u1.base','r')
list_arr = file.readlines()
l = len(list_arr)
file.close()


result = []

for i in range(l):
    list_arr[i]=list_arr[i].replace("\t",",")
    list_arr[i]=list_arr[i].replace("\n","")
    result.append(list(map(int, list_arr[i].split(','))))

# print(result)

tmp = Item_based_C(result)
# print(np.array(result).shape + "a")

test = []
file = open(r'D:\数据 电影\数据 电影\ml-100k\u1.test','r')
list_arr = file.readlines()
l = len(list_arr)
file.close()

for i in range(l):
    list_arr[i]=list_arr[i].replace("\t",",")
    list_arr[i]=list_arr[i].replace("\n","")
    test.append(list(map(int, list_arr[i].split(','))))

print(tmp.test(test))
# csv_reader = csv.reader(open(r'G:\推荐系统数据\ml-100k\ml-100k\u1.base', encoding='utf-8'))
# for row in csv_reader:
#         print(row)