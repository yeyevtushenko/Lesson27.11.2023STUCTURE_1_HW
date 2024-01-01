def main():
    numbers = []

    while True:
        print("\nМеню:")
        print("1. Додати нове число до списку")
        print("2. Видалити усі входження числа зі списку")
        print("3. Показати вміст списку")
        print("4. Перевірити, чи є значення у списку")
        print("5. Замінити значення у списку")
        print("0. Вийти з програми")

        choice = input("Виберіть опцію (0 вихід з програми): ")
        if choice == "1":
            add_number(numbers)
        elif choice == "2":
            remove_number(numbers)
        elif choice == "3":
            show_list(numbers)
        elif choice == "4":
            check_value(numbers)
        elif choice == "5":
            replace_value(numbers)
        elif choice == "6":
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

def add_number(numbers):
    number = int(input("Введіть число для додавання: "))
    if number not in numbers:
        numbers.append(number)
        print(f"Число {number} додано до списку.")
    else:
        print(f"Число {number} вже існує у списку.")







