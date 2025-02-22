n = int(input())
numbers = sorted(map(int, input().split()))
ans = 1
for i in range(1, n):
	# if the current number is different from the previous
	# it is a distinct number so we add 1 to the answer
	if numbers[i] != numbers[i - 1]:
		ans += 1
print(ans)
