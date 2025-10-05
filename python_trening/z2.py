a: str = '1234567'

def ret(a):
    return len(a)

print("s =", ret(a))

b: list = [1, 2, 3, 4, 5, 6, 7]

c: list = [1, 2, 3, 4]

def lenth() -> int:
    if len(b) > len(c):
        return len(b)
    else:
        return len(c) 

print(lenth())

d = 100

def add() -> list:
    (c.append(d))
    return c

print(add())

def plus():
    return sum(c)

print(plus())

