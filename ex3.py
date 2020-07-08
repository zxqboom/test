#!/usr/bin/env Python
# coding=utf-8

string = "I love  python."    
print string               

str_lst = string.split(" ")    
print str_lst

words = [s for s in str_lst if s!=""]    #利用列表解析，将空格检出
print words

new_string = " ".join(words)    #连接单词
print new_string