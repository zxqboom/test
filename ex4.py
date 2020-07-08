#!/usr/bin/env Python
# coding=utf-8

a, b = 0, 1

for i in range(10):   
    a, b = b, a+b

print a