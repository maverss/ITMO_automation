
def fir(a, b):
    if a > b:
        print(a)
    else:
        print(b)

def sec(c, d):
    if c - d == 135 or d - c == 135:
        print('yes')
    else:
        print('no')

def thi(month):
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

def fou(e, f, g):
    if e > 10 and f > 10 and g > 10:
        print('yes')
    else:
        print(e, f, g, '-> no')

def fif(h1, h2, h3, h4, h5):
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

def six(years, months):
    print(years, months, '- входные данные')
    if years >= 0 and months >= 0:
        print('29 *', months, '+' ,years, '* 12 * 29 =', 29 * months + years * 12 * 29)
    else:
        print('err')
        

fir(1000, 100)
print('\n')

sec(137, 2)
print('\n')

for month in range (-1, 14):
    thi(month)
print('\n')

for e in range (9, 13):
    for f in range (9, 13):
        for g in range (9, 13):
            fou(e, f, g)
print('\n')

fif(-2, -1, 0, 1, 2)
print('\n')

'''for years in range (-1, 3):
    for months in range (-1, 3): # - проверка
        six(years, months)'''

six(12, 24)