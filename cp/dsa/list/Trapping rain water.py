def getWater(arr,n):
    res = 0
    lmax = [0]*n
    rmax = [0]*n
    lmax[0] = arr[0]
    for i in range(1,n):
        lmax = max(arr[i], lmax[i-1])
    rmax[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        rmax = max(arr[i], rmax[i+1])
    for i in range(1,n-1):
        res = res + (min(lmax[i],rmax[i])-arr[i])
    return res        