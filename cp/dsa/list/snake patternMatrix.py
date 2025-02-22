def printSnake(mat):
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        if i%2 == 0:
            for j in range(n):
                print(mat[i][j], end = " ")
        else:
            for j in range(n-1,-1,-1):
                print(mat[i][f], end = " ")
                
