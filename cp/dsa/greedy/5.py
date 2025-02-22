def main():
    d = [100, 20, 10, 5, 1] 

    n = int(input())  
    cnt = 0
    for i in d:
        cnt += (n//i)
        n = n%i

    print(cnt)  

if __name__ == "__main__":
    main()
