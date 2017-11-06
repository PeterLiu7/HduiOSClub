# -*- coding: utf-8 -*-
__author__ = 'Zhao'

import re

# 输出Hello world
print("Hello World")

# 1-100求和
sum = 0
for i in range(1, 100):
    sum += i
print("The sum of 1 to 100 is %d." % sum)

# 裴波纳契数列
init1 = 1
init2 = 1
num = int(input("Pleas input the index of the number:\n"))
for i in range(3, num+1):
    number = init1 + init2
    init1 = init2
    init2 = number
print("The %dth number is %d." % (i, number))

# 杨辉三角
line = int(input("Please input the number of lines.\n"))
for i in range(0, line):
    for k in range(0, i):
        print(" ", end="")
    for j in range(0, line-i):
        print("* ", end="")
    print("\n")

# 对于给定格式的年月日 判断这是这一年的第几天 比如给定字符串2008/4/1 ,求是这一年的第几天
date = input("Please input a date:____,such as 2017/10/1\n")
year = int(date.split("/", 1)[0])
month = int(date.split("/", 2)[1])
day = int(date.split("/", 2)[2])

month_lenth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 4) == 0 and (year % 100) != 0:
    month_lenth[1] = 29
elif year % 400 == 0:
    month_lenth[1] = 29

sum = 0
for i in range(0, month-1):
    sum += month_lenth[i]

print("It's %dth day in this year." % (sum + day))
