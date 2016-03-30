#!/bin/bash
# -*- coding: utf-8 -*-  
'''
 * ClassName: test
 * Author: he_hu@founder.com.cn
 * Description: 
 * CreateDate: 2016/3/28
 * Version: 1.0
'''

from numpy import *

a = zeros((2, 3))
a[1][1] = 3
b = ones((2, 3))
print(a**2)
print(a.sum())
print(2**0.5)

c = {'a':1,'b':2}
print(sort(iter(c.items())))
