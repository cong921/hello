# -*- coding: utf-8 -*-
'''
Created on 2018年4月13日

@author: Bob
'''
import itertools
def pi(N):
    #' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    ns=itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns=list(itertools.takewhile(lambda x:x<=2*N,ns))
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    print(ns)
    sum=0
    for i,value in enumerate(ns):
        if i%2==1:
            ns[i]=-value
    print(ns)
    for i in ns:
        sum+=float(4/i)
    # step 4: 求和:
    return sum
print(pi(10))