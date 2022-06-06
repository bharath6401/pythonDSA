# write a code to find the minimum cost required to make the string from the given list of words . If it is not possible to make the string then just return -1 
# else return the minimum cost
# the cost of each word in the list is give in another list.

ex:
arr=["lock","down","lo","ck"]
cost=[50,50,5,5]
str1="lockdown"

outPut=60 #we get two possibilities here 100 and 60 . we choose 60 as it is the minimum

ex2:arr=["hello","e","lo","ck"]
cost=[50,50,5,5]
str1="helloworld"

output:-1 #cause we cant make str1 with the given arr



def combinationsList(arr,str1,map1,outStr="",outCost=0):
    
    if(str1 in outStr):
        print(outStr,outCost)
        outCostList.append(outCost)
        return
        
    if(len(outStr)>len(str1) or outStr not in str1):#we end if the outStr length greater than the input string or 
    # if we dont have outStr string as a subset of input string cause if the pattern is right then we can just 
    #eliminate in the start of the program itself ex: str1: lockdown , outStr=down . we will just skip next part cause
    #we cant make str1 with outStr . we move to the next iteration
    
        return
    
    for item in arr:#we generate all possible combinations 
        combinationsList(arr,str1,map1,outStr+item,outCost+map1[item])

    
arr=["lock","down","lo","ck"]
cost=[50,50,5,5]
str1="lockdown"
outCostList=[]

map1={arr[i]:cost[i] for i in range(len(cost))}
combinationsList(arr,str1,map1,outStr="",outCost=0)
print("output:",min(outCostList) if(outCostList!=[]) else -1)
