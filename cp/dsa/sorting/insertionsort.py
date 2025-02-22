def insertionsart (l):
    for i in range (1, len(l)):
        x = l[i]
        j=i-1
        while j>0 and x < l[i]:
            l[j+1] = l[i]
            j=j-1
        l[j+1] = x
        
        
#O(n) best case
#O(n^2) worst case
#O(n^2) average case

def selectionsort(l):
    for i in range (len(l)):
        min = i
        for j in range (i+1, len(l)):
            if l[j] < l[min]:
                min = j
        l[i], l[min] = l[min], l[i]
        
#O(n)
#O(n^2)
#O(n^2)

def bubblesort(l):
    for i in range (len(l)):
        for j in range (len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
#O(n^2)
#O(n^2)
#O(n^2)

def mergesort(l):
    if len(l) > 1:
        mid = len(l)//2
        left = l[:mid]
        right = l[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i+=1
            else:
                l[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            l[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            l[k] = right[j]
            j+=1
            k+=1
            
#O(nlogn)
#O(nlogn)
#O(nlogn)

def quicksort(l, low, high):
    if low < high:
        pi = partition(l, low, high)
        quicksort(l, low, pi-1)
        quicksort(l, pi+1, high)