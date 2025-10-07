
def maximum(a, b):
    if a > b:
        print(a)
    else:
        print(b)

def difference(c, d):
    if c - d == 135 or d - c == 135:
        print('yes')
    else:
        print('no')

def seasons(month):
    if month in range(1, 3) or month == 12:
        print(month, 'winter')
    elif month in range(3, 6):
        print(month, 'Spring')
    elif month in range(6, 9):
        print(month, 'Summer')
    elif month in range (9, 12):
        print(month, 'Autumn')
    else:
        print(month, 'Wrong month num')

def MoreThan10(e, f, g):
    if e > 10 and f > 10 and g > 10:
        print('yes')
    else:
        print(e, f, g, '-> no')

def PositiveCount(h1, h2, h3, h4, h5):
    x = 0
    if h1 > 0:
        x = x + 1
    if h2 > 0:
        x = x + 1
    if h3 > 0:
        x = x + 1
    if h4 > 0:
        x = x + 1
    if h5 > 0:
        x = x + 1
    print(x)

def days(years, months):
    if years >= 0 and months >= 0:
        print('29 *', months, '+' ,years, '* 12 * 29 =', 29 * months + years * 12 * 29)
    else:
        print('err')
        

maximum(1000, 100)
print('\n')

difference(137, 2)
print('\n')

seasons(10)

'''for month in range (-1, 14): # - проверка
    seasons(month)''' 
print('\n')

MoreThan10(4, 5, 13)

'''for e in range (9, 13): # - проверка
    for f in range (9, 13):
        for g in range (9, 13):
            MoreThan10(e, f, g)'''
print('\n')

PositiveCount(-2, -1, 0, 1, 2)
print('\n')

'''for years in range (-1, 3):
    for months in range (-1, 3): # - проверка
        six(years, months)'''

days(12, 24)