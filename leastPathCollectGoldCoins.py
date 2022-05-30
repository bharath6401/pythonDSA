#problem: given a matrix. find the path from source with index 0,0 to destination by collecting all the gold coins in the middle with least possible path.



def findPath(matrix,row=0,col=0,tup=[]):
  global outLength
  if(row<0 or col<0 or row>=len(matrix) or col>=len(matrix[0]) or (row,col) in tup or matrix[row][col]==1):
    return
  if(matrix[row][col]==3):

    pathmid=tuple(tup+[(row,col)])

    setgoldMatrix=set(goldMatrix)

    setPath=set(pathmid)

    outMatrix.append(pathmid)

    if(setgoldMatrix.issubset(pathmid)):

      if(len(pathmid)<outLength and outLength!=-1):

        outLength=len(pathmid)

      else:

        outLength=len(pathmid)

      print(pathmid)

  ret=findPath(matrix,row+1,col,tup+[(row,col)])

  ret1=findPath(matrix,row-1,col,tup+[(row,col)])

  ret3=findPath(matrix,row,col+1,tup+[(row,col)])

  ret4=findPath(matrix,row,col-1,tup+[(row,col)])



matrix=[[0,2,0],[1,1,1],[1,1,0]]

outLength=-1

outMatrix=[]

x=2 

y=2

goldMatrix=[]

for row in range(len(matrix)):

  for col in range(len(matrix[0])):

    if(matrix[row][col]==2):

      goldMatrix+=[(row,col)]

matrix[x][y]=3

findPath(matrix,row=0,col=0,tup=[])

print(outLength-1 if(outLength!=-1) else outLength)
