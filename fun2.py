def drawline (num,x):

    print(x*num)


def sq (z):
    for i in range(z):
        print("* "*z)   
    
def sq2 (q,w,char):
    for i in range(q):
        print(str(char)*w)
        

def sqs (q,w,char1,char2):
    print(str(char1)*w)
    for i in range(q-2):
        
        print(str(char1)+str(char2)*(w-2)+str(char1))
    print(str(char1)*w)


def fib1 (num):
    c=1
    b=1
    z=b
    for i in range(0,num):
        c=z
        z=z+c
        
    return(z)


def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a


def fact (k):
    z=0
    c=0
    for i in range (1,k+1):
        c=c+1
        z=z+(c+1)*c
    return (z)
