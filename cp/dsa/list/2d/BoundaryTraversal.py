def bTraverse(mat):
    R=len(mat)
    C = len(mat[0])
    if R == 1:
        for i in range(C):
            print(mat[0][i], end=" ")
    elif C == 1:
        for i in range(R):
            print(mat[i][0], end=" ")
    else:
        for i in range(C):
            print(mat[0][i], end=" ")
        for i in range(1, R):
            print(mat[i][C - 1], end=" ")
        for i in range(C - 2, -1, -1):
            print(mat[R - 1][i], end=" ")
        for i in range(R - 2, 0, -1):
            print(mat[i][0], end=" ")
        bTraverse([row[1:-1] for row in mat[1:-1]])
    