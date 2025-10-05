x = int(input("Введите номер курса "))
#print(type(x)) - проверка типа введённых данных

"""for x in range (-5, 13): - тестирование всех вариаций
    print(x)
    if x in range (1, 5):
        print('bakalavr')
    elif x > 9 or x < 1:
        print("Ведите корректный год обучения")
    elif x in range (5, 7):
      print('magistr')
    elif x in range (7, 10):
        print('aspirant')"""

if x in range (1, 5):
    print('bakalavr')
elif x > 9 or x < 1:
    print("Ведите корректный год обучения")
elif x in range (5, 7):
    print('magistr')
elif x in range (7, 10):
    print('aspirant')
