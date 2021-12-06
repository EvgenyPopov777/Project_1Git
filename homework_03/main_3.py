#---------------------------------------------------Задание № 1
def is_prime(num):
    if num == 2 or num == 3: return True
    if num % 2 == 0 or num < 2: return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
def fl(*numbers):
    return list(filter(is_prime, numbers))
    print(numbers)
result =fl(2,3,4,5,6,7,8,9,10)
print(result)




#---------------------------------------------------Задание № 2
def fl_ly (string_list):
    print(string_list)
    set(string_list)
    list(set(string_list))
    known_strings =set()
    for string in string_list:
        if string in known_strings:
            continue
        print(string)
        known_strings.add(string)
fl_ly(['hello','hello','my','world'])


