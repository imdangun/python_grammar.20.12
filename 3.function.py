#3.function.py

def add(a, b):
    return a + b

print(add(1, 2)) # 3

#
def add2(a, b):
    print(a + b)

add2(1, 2) # 3

#
print(add(b = 2, a = 1)) # 3

#
a  = 0
def func():
    global a
    a += 1

for i in range(10):
    func()

print(a) # 10

#
print((lambda a, b: a + b)(1, 2)) # 3