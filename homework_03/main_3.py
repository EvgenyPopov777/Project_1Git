string_list = ['hello','world','apple','earch','world']#Уникальность так же и с выводом простых чисел
set(string_list)
list(set(string_list))
known_strings =set()
for string in string_list:
     if string in known_strings:
         continue
     print('found a new string',string)
     known_strings.add(string)
power =0
def show_numbers(*numbers,power=2):
    for num in numbers:
        print(num**2)
show_numbers(2,4,5,7,8)