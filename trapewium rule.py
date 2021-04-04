from math import *
from matplotlib import pyplot as pa
from matplotlib import figure as fig
def gph(q,n,h):
    xa=[]
    y=[]
    i=-n
    #for i in range(-int(n),int(n)):
    while(i<=n):
        xa.append(i)
        x=i
        f=eval(q)
        y.append(f)
        i=i+1
    pa.plot(xa,y,"g--",label="function graph")
def tp(q):
    a=float(input("enter the lower interval:="))
    g=a
    b=float(input("enter the higher interval:="))
    xl=[]
    yl=[]
    c=int(input("enter no of partions:="))
    d=(b-a)/c
    print('h=',d)
    l=[]
    fx=[]
    while(c+1!=0):
        l.append(a)
        x=a
        f2=eval(q)
        fx.append(f2)
        a=a+d
        c-=1
    xl.append(g)
    yl.append(0)
    xl.append(g)
    yl.append(fx[0])
    pa.plot(xl,yl,"y-")
    xl=[]
    yl=[]
    xl.append(b)
    yl.append(0)
    xl.append(b)
    yl.append(fx[len(fx)-1])
    pa.plot(xl,yl,"y-")
    #pa.fill(xl,yl)
    return d,l,fx
def trp(h,fx):
    j=0
    l=len(fx)
    for i in range(0,l-1):
        j=j+((1/2)*(fx[i]+fx[i+1]))
    return(j*h)
while 1:
    q=input("enter the euqation :=")
    h,r,t=tp(q)
    print('x=',r,'\ny=',t)
    a=trp(h,t)
    print("integral value=",a)
    pa.plot(r,t,"r-",label="trpezium rule")
    pa.title("trapezium rule")
    pa.xlabel("interval points")
    pa.ylabel("f(x) values")
    pa.legend()
    pa.show()
