#2.control.py

## if
a = 15
if a > 10:
    print(a) # 15

#
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'D'

print(grade) # B

#
if 90 <= score < 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
else: grade = 'C'

#
if score >= 80:
    pass
else:
    print('분발하세요.')
print('끝.') # 끝.

# conditional expression
result = '성공' if score >= 80 else '실패'
print(result) # 성공


## 반복문

# while
weight = 90

while weight > 60:
    weight -= 10

print(weight) # 60

# for
y = 0
for i in range(1, 10):
    y += i
print(y) # 45

#
y = 0
for i in range(1, 10):
    if i % 2 == 1:
        continue
    y += i
print(y) # 20

#
for i in range(2, 4):
    for j in range(1, 10):
        print(i, 'x', j, '=', i * j)
    print()
'''
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
'''


