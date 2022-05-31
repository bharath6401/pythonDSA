# def getRightOrLeftmax(arr,i,r=True):
    
#     if(r):
#         initial=arr[i+1]
#         rightMax=arr[i+1]
#         for block in arr[i+2:]:
#             if(block>rightMax):
#                 rightMax=block
#             else:
#                 return(rightMax)
#                 break
#     else:
    
#         initial=arr[i-1]
#         rightMax=arr[i-1]
#         for block in arr[i-2:0]:
#             if(block>rightMax):
#                 rightMax=block
#             else:
#                 return(rightMax)
#                 break
            
            
trapWater=[0,0]+[1,2,4,2,5,6]+[0,0]
outArr=[]
print
# for index in range(2,len(trapWater)-2):
#     outArr.append(getRightOrLeftmax(trapWater,index))
# print(outArr)

