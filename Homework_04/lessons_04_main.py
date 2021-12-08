#-----------------------Задание №1
def power_numbers(*number):
    u =[]
    for i in number:
        i=i**3
        u.append(i)
    return u
print(power_numbers(1,2,3,4,5,6))