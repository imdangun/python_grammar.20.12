#4.io.py

## input
a = int(input())
b = list(map(int, input().split()))
b.sort(reverse=True)

print(a, b)
'''
3 입력
1 2 3 입력
3 [3, 2, 1]
'''

#
'''
a = map(int, input().split())
print(a) # <map object at 0x0000024E868AF2B0>

a, b, c = map(int, input().split())
print(a, b, c)
'''
'''
1 2 3 입력
1 2 3
'''

#
'''
import sys
a = sys.stdin.readline().rstrip()
print('|' + a + '|')
'''
'''
 hello world 
| hello world|
'''

## output
# print(3 + '살입니다.') # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(3) + '살입니다.') # 3살입니다.
print(3, '살입니다.') # 3 살입니다.

age = 3
print(f'{age}살입니다.') # 3살입니다.