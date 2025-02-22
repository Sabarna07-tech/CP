n = int(input())

nums = list(map(int, input().split()))
sums = n*(n+1)//2
add = 0 
for i in range(0,len(nums)):

    add = add + nums[i]
    
print( sums - add)
