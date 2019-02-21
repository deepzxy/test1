# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 09:43:36 2017

@author: Administrator
"""


def fo1(num = 10 ):
    "test for me"
    if(num == 1 or num ==2):
        return 1
    else:
        v1 = v2 =1
        v3 = 0
        for i in range(3,num+1):
            v3 = v1+v2
            v1 = v2
            v2 = v3
        return v3

            
        
def fo(x):
    if(x==1 or x == 2):
        return 1
    y=fo(x-1) + fo(x-2)
    return y        
    

def myfun2():
    "test fun2"
    p = 9
    def mmm():
        nonlocal p
        p *=5
        return p
    return mmm()
     
def hanoi(n,x,y,z):
     if n == 1:
         print(x, "-->",z)
         
     else:
         hanoi(n-1 ,x,z,y) #将前n-1个盘子从x移到y上
         print(x, "-->",z)#将最底下的最后一个盘子从x上移到z上
         hanoi(n-1,y,x,z)#将y上的n-1个盘子移到z上
         
        
hanoi(4,"x","y","z")        
        

ret = fo1(40)
print(ret)

