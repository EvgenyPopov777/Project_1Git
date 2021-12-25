list_of_strings = "The quick brown fox jumps over the  lazy dog" # В переменную  сложена в строчка.
for elem in list_of_strings.split(): # В цикле прошёлся по результату выполнения метода split
    print(elem)# Вывожу каждое слово на новой строчке на консоли.




Type_list_numbers = list(range(100))#Создал переменную, в которой хранятся все числа
print('Проверяем, что тип переменной Type_list_numbers = типу list: :')
print(type(Type_list_numbers))# Переменная  Type_list_numbers типа list.
# print(Type_list_numbers)


new_list_num =[]#создаю пустой список, чтобы туда закинуть  результат квадрата значений
for i in Type_list_numbers: # прохожусь по циклу
    Type_list_numbers = i ** 2 # возвожу значения из списка в квадрат
    new_list_num.append(Type_list_numbers) #добавляю результат квадрата значений списка в новый список.
print('Список всех квадратов чисел: ')
print(list(new_list_num)) # вывожу результат на экран(консольку...)


dict={}#Создаю новый словарь
for key in new_list_num: # прохожусь по списку с квадратами чисел и закидываю значение в переменную key
    str_num = str(key) * 3  # создаю переменную str_num и закидываю в неё строчку состоящую из тройного повторения числа
    dict ={key:str_num} # в результате, в словаре : ключ - это число, а значение, это строка
    print(dict)

# но есть проблема, я не знаю как закинуть в пустой славарь результаты всех ключей и значений). Я понимаю, что строчка dict ={key:str_num} создаёт несколько словарей...
# может быть через такой цикл делается,
# for key,value in dict.items():
#     print(key,value)
# но я не оч понял если честно как это сделать...





























