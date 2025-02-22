dna_sequence = input()
longest_repetition = 0
current_count = 1

for i in range(1, len(dna_sequence)):
    if dna_sequence[i] == dna_sequence[i - 1]:
        current_count += 1
    else:
        longest_repetition = max(longest_repetition, current_count)
        current_count = 1

longest_repetition = max(longest_repetition, current_count)
print(longest_repetition)
