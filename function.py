# -*- coding: utf-8 -*-

def func(precess_data, x):
     precess_data = list(range(0, 100, 3))
     low = 0
     high = 34
     guess = int((low + high) / 2)
     
     while precess_data[guess] != x:
         if precess_data[guess] < x:
             low = guess
         elif precess_data[guess] > x:
             high = guess
         else:
             break
         guess = (low + high) // 2
         
     return guess

print(func(list(range(0, 100, 3)), 99))


