from collections import OrderedDict

s = "bcabc"

def removeDuplicate(s: str) -> str:
    # Use an OrderedDict to preserve the order of insertion
    seq = OrderedDict()
    
    for index, char in enumerate(s):
        # Add each character to the dictionary, if not already present
        if char not in seq:
            seq[char] = index
    
    print(seq)
#     return ''.join(seq.keys())  # Optional: to return the string without duplicates

removeDuplicate(s)
