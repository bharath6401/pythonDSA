#no of visible people in a queue. queue starts from right to left


queue=[5,1,2,3,10]  #input

canSeeCount=[]
for index in range(len(queue)-1):
    maxHeight=-1
    count=0
    for height in queue[index+1:]:
        if(maxHeight==-1):
            maxHeight=height
            count+=1 
        elif(height>maxHeight and queue[index]>maxHeight):
            maxHeight=height
            count+=1
        
    canSeeCount.append(count)
print(canSeeCount+[0]) #output  [4,1,1,1,0]
