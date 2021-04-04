from math import *
from sympy import *
def par():
    a=float(input("enter the a :="))
    b=float(input("enter the  b:="))
    c=int(input("enter the no of partitions:="))
    if(c%3!=0):
        print(" we can't do with odd no of intervals ")
        c=int(input("enter the no of partitions again:="))
    d=round((b-a)/c,4)
    xn=[]
    while(c+1!=0):
        xn.append(a)
        a=a+d
        c-=1
    #xn[len(xn)-1]=round(xn[len(xn)-1],1)
    return xn  
def lit(xn):#list of f(x) creating
    q=input("enter the expression:-")
    l=len(xn)
    b=[]
    for i in range(l):
        x=xn[i]
        b.append(eval(q))
    return b
def intg(a,b):
    l=len(b)-1
    #print(b)
    j=b[0]
    for i in range(1,l-1):
        if(i%3==0):
            j=2*b[i]
        else:
            j=j+3*b[i]
    j=j+b[l-1]
    h=(a[1]-a[0])*(3/8)
    j=j*h
    print(j)
while 1:
    a=par()
    print(a)
    b=lit(a)
    intg(a,b)

