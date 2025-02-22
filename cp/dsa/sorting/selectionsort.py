def selection_sort(arr):
    n = len(arr)
    # Selection sort
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        # Swap the found minimum element with the first element
        arr[i], arr[mini] = arr[mini], arr[i]

    print("After selection sort:")
    for i in range(n):
        print(arr[i], end=" ")
    print()

def main():
    arr = [13, 46, 24, 52, 20, 9]
    print("Before selection sort:")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    selection_sort(arr)

if __name__ == "__main__":
    main()
