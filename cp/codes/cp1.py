# Read input from div7.in
with open("div7.in", "r") as f:
    N = int(f.readline().strip())
    cow_ids = [int(f.readline().strip()) for _ in range(N)]

# Prefix sum mod 7
prefix_mod = 0
first_occurrence = {}
max_length = 0

for i in range(N):
    prefix_mod = (prefix_mod + cow_ids[i]) % 7
    
    # If remainder was seen before, update max length
    if prefix_mod in first_occurrence:
        max_length = max(max_length, i - first_occurrence[prefix_mod])
    else:
        first_occurrence[prefix_mod] = i  # Store first occurrence of this remainder

# Write output to div7.out
with open("div7.out", "w") as f:
    f.write(str(max_length) + "\n")
