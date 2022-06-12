# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).


nums=[5,2,1,2,5,2,5,1]
# input 
# output:8

seen=set()#window keep tracks of the distinct items
i=res=tot=0

for currentIndex in range(len(nums)):
    currentItem=nums[currentIndex]
  
    
    while(i<currentIndex and currentItem in seen):
    
        seen.remove(nums[i])
        tot-=nums[i]
        i+=1
        
    
    seen.add(currentItem)
    tot+=currentItem
    res=max(tot,res)
print(res)

    
