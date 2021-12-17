class Exceptions():
    def get_room_number():
        while True:
            try:
                num = int(input("Введите номер комнаты: "))
                print(f"Комната {num} успешно забронирована!")
            except ValueError:
                print("Исключение: Вы ввели буквы, а нужно число. Повторите ввод:")

