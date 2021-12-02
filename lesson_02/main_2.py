list_of_strings = ['The',' ','quick',' ','brown',' ','fox',' ','jumps',' ','over',' ','the',' ','lazy',' ','dog']
for elem in list_of_strings:
    print(elem)


Type_list_numbers = list(range(0,100))
print(Type_list_numbers)


for container in Type_list_numbers:
    Type_list_numbers = container ** 2
    s = str(Type_list_numbers) * 3
    dict = {Type_list_numbers: s}
    print(Type_list_numbers,dict)





















