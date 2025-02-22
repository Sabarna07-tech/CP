# Constants
MOD = 1000000007  # A common modulus used in competitive programming problems
INF = float('inf')  # Represents infinity, useful for initial values in min/max problems

# Reading input
a = int(input())  # Reads a single integer
b, c = map(int, input().split())  # Reads two space-separated integers
s = input()  # Reads a string

# Output the result
print(str(a + b + c) + " " + s)