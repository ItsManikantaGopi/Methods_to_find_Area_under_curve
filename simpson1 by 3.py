from math import *
from mpmath import *
from sympy import *
def par():
    a=eval(input("enter the a :="))
    b=eval(input("enter the  b:="))
    c=int(input("enter the no of partitions:="))
    if(c%2!=0):
        print(" we can't do with odd no of intervals ")
        c=int(input("enter the no of partitions again:="))
    d=(b-a)/c
    xn=[]
    while(c+1!=0):
        xn.append(a)
        a=a+d
        c-=1
    return xn

def lit(xn,q):#list of f(x) creating
    
    l=len(xn)
#    print(l)
    b=[]
    for i in range(l):
        x=y=o=xn[i]
        b.append(eval(q))
    return b
def intg(a,b):
    l=len(b)-1
    j=0
    h=(a[1]-a[0])/3
    for i in range(0,l-1,2):
        j=j+h*(b[i]+4*b[i+1]+b[i+2])
    return(j) 
while 1:
    a=par()
    q=input("enter the expression:-")
    #print(a)
    b=lit(a,q)
    aj=intg(a,b)
    print(aj)

