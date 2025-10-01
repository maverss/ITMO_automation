def task_1() -> tuple:
    a: int = 1
    b: float = 2.5
    c: str = 'три'
    d: list = [5, 6, 7]
    e: bool = True
    return (type(a), type(b), type(c), type(d), type(e))
        
print (task_1())
print (type(task_1())) #- проверка типа данных функции task_1


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21] #- список
    return a[0:3]

print(task_2())
print (type(task_2())) #- проверка типа данных функции task_2


def  task_3(x: int) -> int:
    return x * x

print(task_3(3))
print (type(task_3(3))) #- проверка типа данных функции task_3