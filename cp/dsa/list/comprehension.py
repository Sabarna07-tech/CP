n = 5
squared = [x**2 for x in range(1,n+1)]
print(squared)
t = [0 for _ in range(n)]
print(t)
my_string = "cowboy bebop"
nb_occurrences = {letter: 0 for letter in my_string}
print(nb_occurrences)
nb_occurrences = {}
for letter in my_string:
    nb_occurrences[letter] = 0
import math
n = math.sqrt(4)
print(int, n)
float('-inf')
f=3/2
print(str(f))

from collections import Counter
c = {} 
c = Counter()
c['a'] += 1 # the key does not exist, so it is created
Counter({'a': 1})
c = Counter('cowboy bebop')
Counter({'o': 3, 'b': 3, 'c': 1, 'w': 1, 'y': 1, '' : 1, 'e': 1, 'p': 1})
print(c)
from collections import * 
g = defaultdict(list)
g['paris'].append('marellie')
g['paris'].append('lyon')
g
print(g['paris'])
M1 = [[0] * 10 for _ in range(10)]
M2 = [[0 for j in range(10)] for i in range(10)]
print[M1]
print[M2]