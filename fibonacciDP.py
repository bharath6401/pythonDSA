#fibonacci series using dynamic programming
#here we save the intermediate values to avoid calculating the same again and again . like fib(4)==>fib(3)+fib(2)  again fib(3)=fib(2)+fib(1).
#here we are saving the intermediate results like fib(2) and fib(3) to calculate fib(4) in dynArr. this decreases unnecessary calculation.

n=int(input())
dynArr=[-1]*(n+1)#array stores the intermediate results of the fibonacci tree.
def fib(n):
    res=-1
    if(dynArr[n]==-1):
        if(n==0 or n==1):
            return(n)
        else:
            res=fib(n-1)+fib(n-2)
            
        dynArr[n]=res
    return(dynArr[n])#returns the intermediate data which is saved in arr to the function and no need to find same result again
fib(n)
if(n==1 or n==2):
    print(n-1)

else:
    print(dynArr[-2])#
