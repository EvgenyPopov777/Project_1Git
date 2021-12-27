#-----------------------Задание №1
def power_numbers(*number):
    u =[]
    [u.append(i**3) for i in number ]
    return u
print(power_numbers(1,2,3,4,5,6))



#-----------------------Задание № 2

def is_prime(num):  #функция на простые числа
    if num == 2 or num == 3: return True
    if num % 2 == 0 or num < 2: return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

ODD = "odd"
EVEN = "even"
PRIME = "prime"
#-----------------Итоговая функция
def filter_numbers(*numbers,key):       # создаю отдельную функцию

    en = []                             # создаю пустой массив
    if key == ODD:                    # ставлю условие, если key = ключу ODD
        for i in numbers:               # создаю цикл(прохожусь по каждому значению и выполняю условие)
            if i % 2 == 0:              # если значение(i) делится на 2 без остатка
                en.append(i)            # добавляю его в пустой массив
                                        # (затем снова иду по циклу  до тех пор, пока есть значения в i)
        return en                       # возвращаю результат прохождения цикла в массив()
    if key == EVEN:                   # ставлю условие, если key = ключу EVEN
        for j in numbers:               # создаю цикл(прохожусь по каждому значению и выполняю условие)
            if j % 2 != 0:              # если значение(i) не делится на 2 без остатка
                en.append(j)            # добавляю его в пустой массив
                                        # (затем снова иду по циклу  до тех пор, пока есть значения в i)
        return en                       # возвращаю результат прохождения цикла в массив()
    if key == PRIME :
        return list(filter(is_prime, numbers))
print(filter_numbers(1,2,3,4,5,6,key=PRIME))




