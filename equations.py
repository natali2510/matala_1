def azeret(x):
    a=1
    for i in range (1,x+1):
     a=a*i
    return a

def hezka(x,n):
    result=1
    for i in range (1,n+1):
        result = result*x
    return result

def absu(x):
    if x<0:
        x=x*(-1)
    return x

def Ln(x):
   if x<=0 :
        return 0.0
   yn = x-1 
   yn1=yn + 2*(x-exponent(yn))/(x+exponent(yn))
   while (absu(yn-yn1)>0.001):
       yn=yn1
       yn1=yn + 2*(x-exponent(yn))/(x+exponent(yn))
   return yn1

def exponent(x):
    ex = 1
    for n in range (1,140):
      ex = ex + hezka(x,n)/azeret(n)
    return ex
    
def XtimesY(x,y):
    if x<=0 :
        return 0.0
    return exponent(y*Ln(x))
       
def sqrt(x,y):
    if x==0 :
        return 0.0
    return XtimesY(y, 1/x)

def calculate(x):
    return exponent(x)*XtimesY(7, x)*XtimesY(x, -1)*sqrt(x,x)
    
print (calculate(0))

