#5.library.py

## standard
result = sum([1, 2, 3])
print(result) # 6

#
result = min([1, 2, 3])
print(result) # 1

#
result = max([1, 2, 3])
print(result) # 3

#
result = eval('(1 + 2) * 3')
print(result) # 9

#
result = sorted([3, 1, 2])
print(result) # [1, 2, 3]

result = sorted([3, 1, 2], reverse=True)
print(result) # [3, 2, 1]

result = sorted([('최한석', 12), ('한아름', 32)],
                key = lambda x: x[1],
                reverse = True)
print(result) # [('한아름', 32), ('최한석', 12)]

a = [3, 1, 2]
a.sort()
print(a) # [1, 2, 3]


## itertools
#
a = ['a', 'b', 'c']

from itertools import permutations

result = list(permutations(a, 2))
print(result) # [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

#
from itertools import combinations

result = list(combinations(a, 2))
print(result) # [('a', 'b'), ('a', 'c'), ('b', 'c')]

#
from itertools import product

result = list(product(a, repeat=2))
print(result)
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]

#
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(a, 2))
print(result) # [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]


## heapq



