# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 23:17:03 2020

@author: user
"""

x=int(input('Enter the 3 digit number:'))
count=0
while x!=0:
    n=x%10
    if n==3:
        count=count+1
    x=x//10
print(count)