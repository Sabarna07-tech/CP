#Naive Reccursive approach
# def maxProfit(arr,b,e):
#     if(e<=b):
#         return 0
#     profit = 0
#     for i in range(b,e):
#         for j in range(i+1,j+1):
#             if(arr[j]>arr[i]):
#                 curr_profit = arr[j]-arr[i]+maxProfit(arr, b, i-1)+maxProfit(arr, j+1, e)
#                 profit = max(profit, curr_profit)
#     return profit
#Optimized approach
def maxProfit(arr):
    profit = 0
    for i in range(1, len(arr)):
        if(arr[i]>arr[i-1]):
            profit += (arr[i]-arr[i-1])
    return profit
arr = [100, 180, 260, 310, 40, 535, 695]
print(maxProfit(arr))
                