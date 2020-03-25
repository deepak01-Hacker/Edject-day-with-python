#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:15:47 2020

@author: root
"""
## valid in only 2000 satabdi
print(" <> Edject day Program -<>")
print("Enter date // month // year : with space .")
dd,mm,yy = map(int,input().split(" "))
month_s = [1,4,4,0,2,5,0,3,6,1,4,0]
month_l = [0,3,4,0,2,5,0,3,6,1,4,0]
##year_code = [1700:4,1800:2,1900:0,2000:6]
day = ['saturday','Sunday','Monday','Tuesday','wednesday','Thursday','friday']
if yy - 1900<101:
    k = 0
elif yy - 2000<101:
    k = 6
##satabd i 2000 = 6
if yy%4 == 0:
    k += month_l[mm-1]
else:
    k += month_s[mm-1]
k += dd
leap_count = (yy%100) // 4
k += leap_count + (yy%100)
print("Day is : " + str(day[k%7]))

