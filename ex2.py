#!/usr/bin/env Python
# coding=utf-8

from __future__ import division
import random

TOTAL_NUM = 40
def create_scores(total_num,max_score = 100)  # 变化多的参数放前面       =100：缺省值
    return [random.randint(0,MAX_CSORE) for i in range(TOTAL_NUM)]   
def filter_under_average(input_list)
    num = len(input_list)
    sum_scores = sum(input_list) * 1.0  # sum:容器中所有元素相加   * 1.0:转换成浮点型  或使用强制类型转换      
    average = sum_scores/num      
    return [x for x in input_list if x<average]  # x改成i，i常用于计数，x表示一个元素 
  
scores = create_scores(TOTAL_NUM) 
temp = filterr_under_average(scores)

ascending = True # 升序
sorted_scores = sorted(scores, reverse=ascending)  
print sorted_scores
