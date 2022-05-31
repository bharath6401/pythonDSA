#trapping rain water 

def getRightOrLeftmax(arr,i,r=True):
    if(r):
        return(max(arr[i:]))
    else:
        return(max(arr[i::-1]))
        
trapWater=[3,0,0,2,0,4]
n=6
diffArr=[]

for index in range(n):
    leftMax=getRightOrLeftmax(trapWater,index)
    rightMax=getRightOrLeftmax(trapWater,index,False)
    diffArr.append(min(leftMax,rightMax)-trapWater[index])
print(sum(diffArr))
