def TransposeMatrix(n):
    for i in range(len(n)):
        for j in range(len(n[0])):
            result[j][i] = n[i][j]

X=[[1 , 2 ,3] ,
    [4 , 5 ,6],
    [7 ,8 ,9]]

result=[[0 , 0 , 0],
        [0 , 0 , 0],
        [0 , 0 , 0]]

TransposeMatrix (X)

for r in result:
    print(r)

        


