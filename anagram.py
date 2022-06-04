# check if strings s and t are anagrams to each other

s="anagram"
t="naagrma"
sMap={}
tMap={}
for char in s:
    if(char in sMap):
        sMap[char]+=1 
    else:
        sMap[char]=1 
        
for char in t:
    if(char in tMap):
        tMap[char]+=1 
    else:
        tMap[char]=1 
print(sMap==tMap)

# method2 sort both and try comparing them
