#1.datatype.py

## Integer(정수형)
a = 1; print(a) # 1
a = -1


## Real Number(실수형)
a = 1.0; print(a) # 1.0
a = 1.; print(a)  # 1.0
a = -1.0
a = .1; print(a) # 0.1

a = 1e9; print(a) # 1000000000.0
a = 1.23e1; print(a) # 12.3
a = 1e-1; print(a) # 0.1

a = .3 + .6; print(a) # 0.8999999999999999, floating-point, IEEE754
print(round(a, 1)) # 0.9

# / 의 리턴값은 실수형이다.
a = 7 / 3; print(a) # 2.3333333333333335
a = 7 % 3; print(a) # 1
a = 7 // 3; print(a) # 2
a = 2 ** 2; print(a) # 4


## list
a = [1, 2]; print(a) # [1, 2]
print(a[0]) # 1
a = list(); print(a) # []
a = []; print(a) # []
a = [0] * 2; print(a) # [0, 0]

# indexing: 리스트의 특정 원소에 접근하는 것이다.
a = [1, 2, 3]
print(a[-1]) # 3
print(a[-3]) # 1

a[1] = 20; print(a) # [1, 20, 3]

# slicing
print(a[1 : 2]) # [20]

# list comprehension
a = [i for i in range(10) if i % 2 == 1]
print(a) # [1, 3, 5, 7, 9]

a = [i * i for i in range(1, 10)]
print(a) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

n = 2; m = 3
a = [[0] * m for _ in range(2)]
print(a) # [[0, 0, 0], [0, 0, 0]]

# list method
a = [1, 4, 3]
a.append(2); print(a) # [1, 4, 3, 2]
a.sort(); print(a) # [1, 2, 3, 4]
a.sort(reverse = True); print(a) # [4, 3, 2, 1]
a.reverse(); print(a) # [1, 2, 3, 4]
a.insert(2, 3); print(a) # [1, 2, 3, 3, 4]
print(a.count(3)) # 2
a.remove(1); print(a) # [2, 3, 3, 4]

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result) # [1, 2, 4]


## string
a = 'hello'; print(a) # hello
a = 'Don\'t touch me'; print(a) # Don't touch me
a = 'He said, "I\'m hugry."'; print(a) # He said, "I'm hugry."

a = 'hello'
print(a + ' ' + 'world') # hello world
print(a * 2) # hellohello
print(a[1 : 3]) # el


## tuple
# list 와 달리, 원소값을 못 바꾼다.
# list 와 달리, () 를 사용한다.

a = (1, 2); print(a) # (1, 2)
#a[0] = 10 # TypeError: 'tuple' object does not support item assignment


## dictionary
# 순서가 없다.
a = dict()
a['사과'] = 'apple'
a['포도'] = 'grape'
print(a) # {'사과': 'apple', '포도': 'grape'}

if '사과' in a:
    print('사과가 있습니다.') # 사과가 있습니다.

# dictionary method
print(a.keys()) # dict_keys(['사과', '포도'])
print(a.values()) # dict_values(['apple', 'grape'])

for key in a.keys():
    print(a[key])
'''
apple
grape
'''


## set
# 값 중복이 없다.
# 순서가 없다.
a = set([1, 2, 2, 3, 3, 3]); print(a) # {1, 2, 3}
a = {1, 2, 2, 3, 3, 3}; print(a) # {1, 2, 3}

a = {1 ,2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a | b) # 합집합, {1, 2, 3, 4, 5, 6, 7}
print(a & b) # 교집합, {3, 4, 5}
print(a - b) # 차집합, {1, 2}

# set method
a = {1}
a.add(2); print(a) # {1, 2}
a.update([3, 4]); print(a) # {1, 2, 3, 4}
a.remove(3); print(a) # {1, 2, 4}