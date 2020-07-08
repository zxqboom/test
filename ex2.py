#!/usr/bin/env Python
# coding=utf-8

from __future__ import division
import random

MAX_SCORE = 100
TOTAL_NUM = 40
scores = [random.randint(0,MAX_CSORE) for i in range(TOTAL_NUM)]   
print scores

# num = len(scores)
sum_scores = sum(scores) * 1.0  # sum:容器中所有元素相加   * 1.0:转换成浮点型  或使用强制类型转换      
average_num = sum_scores/TOTAL_NUM       
num_under_average = len([x for x in scores if x<ave_num])  # x改成i，i常用于计数，x表示一个元素  
print "the average scores is:%.1f" % average_num
print "There are %d students less than average." % num_under_average

ascending = True # 升序
sorted_scores = sorted(scores, reverse=ascending)  
print sorted_scores
