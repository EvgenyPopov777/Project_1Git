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

