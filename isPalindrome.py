# check if the given string is palindrome or not in theta(n//2)

def isPalindrome(str1):
    begin=0
    end=len(str1)-1
    
    while(begin<end):#we trace from both ends. so, we just need to check till n//2
        if(str1[begin]!=str1[end]):
            return(False)
        begin+=1
        end-=1
    return(True)


str1="anina"
print(isPalindrome(str1))
