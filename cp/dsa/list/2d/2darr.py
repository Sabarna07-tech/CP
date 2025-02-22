# arr = [[1,2,3],[4,5,6,7,8]]
# for r in arr:
#     for x in r:
#         print(x,end=" ")
#     print()
    
# print("Number of rows", len(arr))

# print("Count in the first row", len(arr[0]))
# print("Count in the second row", len(arr[1]))
# print("Count in the third row", len(arr[2]))

# arr = [[1,2,3],[4,5,6,7,8]]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j], end=" ")
#     print() 
# rows = 3
# cols = 4

# arr = [[ 0 for i in range(cols)] for j in range(rows)]
# arr[0][0] = 2
# for r in arr:
#     print(r)
def printMatrix(mat):
    M = len(mat)
    N = len(mat[0])
    for i in range(M):
        for j in range(N):
            print(mat[i][j], end=" ")
        print()
        
if __name__ == '_main_':
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]
    printMatrix(mat)