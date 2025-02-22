# Reading input
n = int(input())  # Read the first integer n

# Read the next line and split it into integers
x_input = list(map(int, input().split()))
# p = x_input[0]
x_levels = set(x_input[1:])

# Read the next line and split it into integers
y_input = list(map(int, input().split()))
# q = y_input[0]
y_levels = set(y_input[1:])

# Combine the levels Little X and Little Y can pass
combined_levels = x_levels.union(y_levels)

# Check if they can pass all levels
if len(combined_levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
