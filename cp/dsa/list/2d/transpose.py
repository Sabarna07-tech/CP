# def transpose(mat):
#     N = len(mat)
#     temp = [[0]*N for i in range(N)]
#     for i in range(N):
#         for j in range(N):
#             temp[i][j] = mat[j][i]
#             return temp
def transpose(mat):
    N = len(mat)
    for i in range(N):
        for j in range(i+1,N):
            mat [i][j], mat[j][i] = mat[j][i], mat[i][j]