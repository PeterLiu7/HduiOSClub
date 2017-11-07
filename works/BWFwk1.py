#!/usr/bin/python3
# -*- coding: UTF-8 -*-
print ("Hello,World!");   #输出hello world

sum = 0;    #1-100的和
sum = ((1+100)*100)/2;
print (sum);

def FBNQ(n):    #斐波那契数列
    if n <= 0:
        return 0;
    elif n == 1:    
        return 1;
    else:
        return FBNQ(n-1) + FBNQ(n-2);

print (FBNQ(5));

def yanghui():  #杨辉三角
    b = [1];
    while True:
        yield b;
        b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1];
 
 
n = 0
for t in yanghui():
    print(t);
    n += 1;
    if n == 10:
        break;

def panduan(year,month,day):    #判断年月日
    a = [31,28,31,30,31,30,31,31,30,31,30,31];
    b = [31,29,31,30,31,30,31,31,30,31,30,31];
    sum = 0;
    
    if(year%4 == 0):
        if(year%100 == 0):
            for i in range(0,month-1):
                sum += b[i];
            sum = sum + day;
            print ("today is %d day" % (sum));
        
        elif(year%400 == 0):
            for i in range(0,month-1):
                sum += a[i];
            sum = sum + day;
            print ("today is day" % (sum));
        else:
            for i in range(0,month-1):
                sum += b[i];
            sum = sum + day;
            print ("today is %d day" % (sum));

panduan(2008,4,1);

