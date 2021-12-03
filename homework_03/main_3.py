# string_list = ['hello','world','apple','earch','world']#Уникальность так же и с выводом простых чисел
# set(string_list)
# list(set(string_list))
# known_strings =set()
# for string in string_list:
#      if string in known_strings:
#          continue
#      print('found a new string',string)
#      known_strings.add(string)
# power =0
def show_numbers(*numbers):
    for num in numbers:
        if num % num == 0:
            print(num)
        else:
         break
show_numbers(1,2,3,10,12,15,0)

